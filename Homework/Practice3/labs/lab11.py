def give_bits_of_number(n):
    result = []
    for i in range(8):
        result.append(n % 2)
        n //= 2
    result.reverse()
    return result


def give_bits_of_number_advanced(n):
    result = []
    while n != 0:
        result.append(n % 2)
        n //= 2
    result.reverse()
    return result


def from_bytes_to_bits(b):
    result = []
    for e in b:
        bits_of_number = give_bits_of_number(e)
        for bit in bits_of_number:
            result.append(bit)
    return result


def bits_into_signed_number(b):
    sign = b[0]
    result = 0
    for i in range(1, len(b)):
        result *= 2
        if sign == 0:
            result += b[i]
        else:
            result += (1 - b[i])
    result *= (1 if sign == 0 else -1)
    result -= (0 if sign == 0 else 1)
    return result


def bits_into_unsigned_number(b):
    result = 0
    for i in range(len(b)):
        result *= 2
        result += b[i]
    return result


def bits_into_float(b):
    sign = b[0]
    exponent = b[1:9]
    mantis = b[9:]
    power = bits_into_unsigned_number(exponent) - 127
    result = 1 * (2 ** power)
    for i in range(len(mantis)):
        result += mantis[i] * (2 ** (power - i - 1))
    result *= (1 if sign == 0 else -1)
    return result


def get_slice(x, start, length):
    return x[start * 8:(start + length) * 8]


def create_c_structure_array(x, length, address):
    result = []

    for i in range(length):
        result.append(create_c_structure(x, address + i * 2))

    return result


def create_char_array(x, length, address):
    result = ""

    for i in range(length):
        result += chr(bits_into_unsigned_number(get_slice(x, address + i, 1)))

    return result


def create_int_array(x, length, address):
    result = []

    for i in range(length):
        result.append(bits_into_unsigned_number(
            get_slice(x, address + i * 4, 4)))

    return result


def create_b_structure(x, address):
    result = dict()

    result["B1"] = bits_into_unsigned_number(get_slice(x, address, 8))
    result["B2"] = bits_into_signed_number(get_slice(x, address + 8, 4))
    result["B3"] = create_char_array(x, 5, address + 12)
    result["B4"] = \
        create_c_structure_array(x,
                                 bits_into_unsigned_number(
                                     get_slice(x, address + 17, 2)),
                                 bits_into_unsigned_number(
                                     get_slice(x, address + 19, 4)))

    return result


def create_c_structure(x, address):
    result = dict()

    result["C1"] = bits_into_signed_number(get_slice(x, address, 1))
    result["C2"] = bits_into_unsigned_number(get_slice(x, address + 1, 1))

    return result


def create_d_structure(x, address):
    result = dict()

    result["D1"] = bits_into_signed_number(get_slice(x, address, 1))
    result["D2"] = bits_into_float(get_slice(x, address + 1, 4))
    result["D3"] = bits_into_signed_number(get_slice(x, address + 5, 8))
    result["D4"] = bits_into_signed_number(get_slice(x, address + 13, 4))
    result["D5"] = bits_into_unsigned_number(get_slice(x, address + 17, 2))
    result["D6"] = bits_into_signed_number(get_slice(x, address + 19, 2))
    result["D7"] = bits_into_signed_number(get_slice(x, address + 21, 1))

    return result


def main(b):
    x = from_bytes_to_bits(b)
    result = dict()

    result["A1"] = create_b_structure(x,
                                      bits_into_unsigned_number(
                                          get_slice(x, 5, 2)))
    result["A2"] = create_char_array(x, bits_into_unsigned_number(
        get_slice(x, 7, 4)),
                                     bits_into_unsigned_number(
                                         get_slice(x, 11, 4)))
    result["A3"] = bits_into_signed_number(get_slice(x, 15, 4))
    result["A4"] = create_d_structure(x, bits_into_unsigned_number(
        get_slice(x, 19, 2)))
    result["A5"] = bits_into_signed_number(get_slice(x, 21, 2))
    result["A6"] = bits_into_unsigned_number(get_slice(x, 23, 1))
    result["A7"] = create_int_array(x, 6, 24)

    return result


a1 = (b'\xdeIBNP\x004\x00\x00\x00\x06\x00\x00\x00K'
      b'\xdf\xb0\xca\x15\x00Q\x0fw\xcc'
      b'\x0e\xb4?\xb1\xa2J\x19\xc3D\xa1r\xa0\x969;'
      b'\x12\x18p\xdamt\x00\xb4#'
      b'\xf2\x0b\x05\xa8\xbc\xf9\x9e\xda\xd2v\x05'
      b'\xbf\xc40\x8d\x03yayhu\x00\x02\x00'
      b'\x00\x000nepvzy\xc7\xbf/\xe2\xf1\x90\x8c'
      b'\xbd\xdb\xack?\xa4C9\xcf|\x1dO'
      b'\x8fc\x14')
a2 = (b'\xdeIBNP\x004\x00\x00\x00\x06\x00\x00\x00K'
      b'\xf1\x06\x13\x14\x00Q\xaa\x1f\x80'
      b'\xa5\xde\x814\xffoV\xcbI\xf6\x9b6\xb5\xb26'
      b'\x9c\xfa\t+G\xc6_\x11G'
      b'\xde)\xce\x8fI]\x97"\xca\xc1\x97\t\x9c:\x1c'
      b'<jhyyt\x00\x02\x00\x00\x000boggd'
      b'b\x83?\x15\xd11\xdd\xcd\xd6\xb4\xbc\xb8&5'
      b'\x8a\x0b\xb0a$\x04\xec\xa3s')

main(a1)
main(a2)

print(main(a1))
print(main(a2))

a3 = b'\xdeIBNP\x004\x00\x00\x00\x06\x00\x00\x00K\xdf\xb0\xca\x15\x00Q\x0fw\xcc\x0e\xb4?\xb1\xa2J\x19\xc3D\xa1r\xa0\x969;\x12\x18p\xdamt\x00\xb4#\xf2\x0b\x05\xa8\xbc\xf9\x9e\xda\xd2v\x05\xbf\xc40\x8d\x03yayhu\x00\x02\x00\x00\x000nepvzy\xc7\xbf/\xe2\xf1\x90\x8c\xbd\xdb\xack?\xa4C9\xcf|\x1dO\x8fc\x14'
print(main(a3))
