def create_segment(x, original_position, length, new_position):
    mask = 2**(original_position + length) - 2**original_position
    segment = x & mask
    if original_position < new_position:
        return segment << (new_position - original_position)
    else:
        return segment >> (original_position - new_position)


def main(x):
    result = 0
    result |= create_segment(x, 0, 11, 5)
    result |= create_segment(x, 11, 2, 0)
    result |= create_segment(x, 13, 1, 3)
    result |= create_segment(x, 14, 6, 23)
    result |= create_segment(x, 20, 7, 16)
    result |= create_segment(x, 27, 1, 2)
    result |= create_segment(x, 28, 3, 29)
    result |= create_segment(x, 31, 1, 4)
    return result


main(0x7e19b9bd)
main(0x8091b459)

print(hex(main(0x7e19b9bd)))
print(hex(main(0x8091b459)))
