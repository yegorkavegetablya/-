from itertools import groupby


def rle_encode(data):
    return [(k, len(list(g))) for k, g in groupby(data)]


def straight_transformation(text):
    result_number = -1
    result_string = ""

    t = [text]
    for i in range(len(text) - 1):
        t.append(t[i][1:] + t[i][0])

    t.sort()

    for el in t:
        result_string += el[-1]

    for i in range(len(t)):
        if t[i] == text:
            result_number = i + 1

    return result_string, result_number


def reverse_transformation(text, number):
    t = ["" for i in range(len(text))]
    for k in range(len(text)):
        for i in range(len(text)):
            t[i] = text[i] + t[i]
        t.sort()
    return t[number - 1]


string_test_1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sed pellentesque tellus, rutrum semper lectus. Proin in dui vitae neque feugiat congue non in ex. Phasellus sed velit et lectus ornare pellentesque. Donec aliquet suscipit nulla, at vulputate risus mattis vitae. Nam sit amet nunc eget mauris vulputate dapibus. Proin feugiat justo semper, sodales nunc quis, dapibus arcu. Morbi dignissim sapien ac est semper consectetur. Nulla facilisi. Fusce non euismod orci. Nunc bibendum diam in risus sodales molestie. Mauris tincidunt eleifend turpis et sollicitudin. Donec sed lorem a eros convallis imperdiet. Nunc interdum quis risus at porttitor."
string_test_2 = "Donec quis neque ac dui eleifend sodales. Aliquam luctus varius augue. Vestibulum bibendum, dolor sit amet blandit tempor, dolor elit dignissim ipsum, quis pretium ipsum mauris et magna. Donec ullamcorper scelerisque justo, vitae convallis quam posuere in. Vestibulum quis mollis lectus. Sed sed commodo nisi, quis pulvinar ex. Cras consectetur porttitor nulla, non tincidunt libero malesuada nec. In ornare rutrum lacus, sed mattis lacus vestibulum nec. Donec ex ante, imperdiet id diam vel, auctor auctor nisl. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla in vehicula purus, in lobortis quam. Pellentesque arcu risus, mollis eget eros vel, egestas sollicitudin felis. Pellentesque ultricies quam magna, nec molestie leo congue at. Cras a nibh et nulla ullamcorper molestie in quis felis."
string_test_3 = "Sed mattis lobortis eros, id porta purus luctus non. Nunc ultricies euismod nulla, et venenatis lacus eleifend sit amet. Morbi laoreet sem eu lectus tempus, eget posuere eros venenatis. Maecenas sollicitudin finibus nulla, et mattis purus cursus a. Donec iaculis lacinia purus, a blandit odio varius ac. Etiam tincidunt, ipsum varius bibendum dignissim, arcu metus faucibus arcu, sed vulputate orci erat sed erat. Fusce facilisis tellus tellus, eu accumsan lorem pulvinar eu. Donec pulvinar arcu in elementum commodo. Quisque et consectetur diam. Nulla iaculis tempor dapibus. Mauris in tempus velit. Vivamus varius nisi quis malesuada fermentum. Proin mollis risus et diam laoreet consectetur."
result_1 = straight_transformation(string_test_1)
result_2 = straight_transformation(string_test_2)
result_3 = straight_transformation(string_test_3)
rle1_1 = rle_encode(string_test_1)
rle1_2 = rle_encode(string_test_2)
rle1_3 = rle_encode(string_test_3)
rle2_1 = rle_encode(result_1[0])
rle2_2 = rle_encode(result_2[0])
rle2_3 = rle_encode(result_3[0])
print(len(rle1_1))
print(len(rle2_1))
print(rle1_1)
print(rle2_1)
print(len(rle1_2))
print(len(rle2_2))
print(rle1_2)
print(rle2_2)
print(len(rle1_3))
print(len(rle2_3))
print(rle1_3)
print(rle2_3)

