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
    first = b[0]
    result = 0
    for i in range(1, len(b)):
        result *= 2
        result += b[i]
    result *= (1 if first == 0 else -1)
    result -= (0 if first == 0 else 1)
    return result


def bits_into_unsigned_number(b):
    result = 0
    for i in range(len(b)):
        result *= 2
        result += b[i]
    return result


def bits_into_float(b):
    return float.fromhex(hex(bits_into_unsigned_number(b)))


a1 = (b'\xdeIBNP\x004\x00\x00\x00\x06\x00\x00\x00K\xdf\xb0\xca\x15\x00Q\x0fw\xcc'
      b'\x0e\xb4?\xb1\xa2J\x19\xc3D\xa1r\xa0\x969;\x12\x18p\xdamt\x00\xb4#'
      b'\xf2\x0b\x05\xa8\xbc\xf9\x9e\xda\xd2v\x05\xbf\xc40\x8d\x03yayhu\x00\x02\x00'
      b'\x00\x000nepvzy\xc7\xbf/\xe2\xf1\x90\x8c\xbd\xdb\xack?\xa4C9\xcf|\x1dO'
      b'\x8fc\x14')
a2 = (b'\xdeIBNP\x004\x00\x00\x00\x06\x00\x00\x00K\xf1\x06\x13\x14\x00Q\xaa\x1f\x80'
      b'\xa5\xde\x814\xffoV\xcbI\xf6\x9b6\xb5\xb26\x9c\xfa\t+G\xc6_\x11G'
      b'\xde)\xce\x8fI]\x97"\xca\xc1\x97\t\x9c:\x1c<jhyyt\x00\x02\x00\x00\x000boggd'
      b'b\x83?\x15\xd11\xdd\xcd\xd6\xb4\xbc\xb8&5\x8a\x0b\xb0a$\x04\xec\xa3s')

b1 = from_bytes_to_bits(a1)
b2 = from_bytes_to_bits(a2)
c1 = give_bits_of_number_advanced(13617089611002414527)
c2 = give_bits_of_number_advanced(5286547713289197321)
print(b1)
print(c1)
print(len(a1))
print(len(b1)/8)
print(len(c1))
print(bits_into_unsigned_number(give_bits_of_number_advanced(13617089611002414527)))
for i in range(len(b1)):
    for j in range(len(c1)):
        if b1[i] != c1[j]:
            break
    else:
        print(i)

# print(bits_into_unsigned_number(b[92:156]))
