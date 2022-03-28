def pass_string_segment(s, index, segment):
    while not s[index:index+len(segment)] == segment:
        index += 1
    return index + len(segment)


def create_number(s, numbers, index):
    index += 1
    number = ""
    is_positive = True
    while s[index] == "-" or s[index].isnumeric():
        if s[index] == "-":
            is_positive = False
        else:
            number += s[index]
        index += 1
    numbers.append(int(number) * (1 if is_positive else -1))
    return index


def create_pair(s, result, index):
    name = ""
    numbers = []
    index = pass_string_segment(s, index, "<block>")
    index = pass_string_segment(s, index, "opt")
    index = pass_string_segment(s, index, "[")
    while s[index] != "]":
        if s[index] == "#":
            index = create_number(s, numbers, index)
        else:
            index += 1
    index = pass_string_segment(s, index, "=>")
    index = pass_string_segment(s, index, "q(")
    while s[index] != ")":
        name += s[index]
        index += 1
    index += 1
    result[name] = numbers
    index = pass_string_segment(s, index, "</block>.")
    return index


def main(s):
    result = dict()
    index = 0
    index = pass_string_segment(s, index, "do")
    while True:
        if not s[index].isspace():
            if s[index:index+3] == "end":
                return result
            index = create_pair(s, result, index)
        else:
            index += 1


main("""do <block> opt[ #4032 . #1985 ] =>q(leor_3) </block>. <block>
opt[#-3487 . #2590 .#-4114 ] =>q(eronra_350) </block>.<block> opt [
#8522 . #4465 .#4011] =>q(erri_62) </block>. <block>opt [ #-5249 .
#-8476 . #5414 . #8585] =>q(inqu_639) </block>. end""")
main("""do <block>opt [ #-8466 . #8061 ]=> q(zale_173) </block>.<block> opt
[#-7572 . #9246 . #-9412 . #9736 ] => q(edmaed) </block>. <block> opt
[#-1594 . #-9312 .#4993 .#-5984 ] => q(resoar_188) </block>.
<block>opt[ #-2735 .#4999 ] => q(ceteon) </block>. end""")

print(main("""do <block> opt[ #4032 . #1985 ] =>q(leor_3) </block>. <block>
opt[#-3487 . #2590 .#-4114 ] =>q(eronra_350) </block>.<block> opt [
#8522 . #4465 .#4011] =>q(erri_62) </block>. <block>opt [ #-5249 .
#-8476 . #5414 . #8585] =>q(inqu_639) </block>. end"""))
print()
print()
print()
print(main("""do <block>opt [ #-8466 . #8061 ]=> q(zale_173) </block>.<block> opt
[#-7572 . #9246 . #-9412 . #9736 ] => q(edmaed) </block>. <block> opt
[#-1594 . #-9312 .#4993 .#-5984 ] => q(resoar_188) </block>.
<block>opt[ #-2735 .#4999 ] => q(ceteon) </block>. end"""))
