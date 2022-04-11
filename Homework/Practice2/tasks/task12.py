def edit_md_file(file_name_read, file_name_write):
    is_open_bracket_now = 0
    result_text = ""
    fr = open(file_name_read, "r+")
    while True:
        line = fr.readline()
        if not line:
            break

        if line[0:4] == "    ":
            result_text += line
        else:
            for c in line:
                if c == "\"":
                    result_text += ("<<" if is_open_bracket_now % 2 == 0 else ">>")
                    is_open_bracket_now = (is_open_bracket_now + 1) % 2
                else:
                    result_text += c
    fw = open(file_name_write, "w+")
    fw.write(result_text)


edit_md_file("info.md", "new_info.md")

