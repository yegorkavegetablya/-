import os


class Vertex:
    def __init__(self, name, path, type):
        self.children = []
        self.name = name
        self.path = path
        self.type = type

    def dfs_print(self, length=0):
        if self.type == "file":
            print(("\t" * length) + "File with name: " + self.name)
        else:
            print(("\t" * length) + "Direction with name: " + self.name + ", internal files and directories:")
            for el in self.children:
                el.dfs_print(length + 1)

    def dfs_print_fancy(self, length=0, is_first=False):
        if self.type == "dir":
            if is_first:
                print(("\t" * length) + "digraph " + self.name + " {")
            else:
                print(("\t" * length) + "subgraph " + self.name + " {")
            files = []
            for el in self.children:
                if el.type == "file":
                    files.append(el)
                else:
                    el.dfs_print_fancy(length + 1)
            for i in range(len(files)):
                if i == 0:
                    print("\t" * (length + 1), end="")

                print("\"" + files[i].name + "\"", end="")

                if i != len(files) - 1:
                    print(" -> ", end="")
                else:
                    print(";")
            print("\t" * length + "}")


def scan_dir(dir, vertex):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            vertex.children.append(Vertex(name, path, "file"))
        else:
            vertex.children.append(Vertex(name, path, "dir"))
            scan_dir(path, vertex.children[-1])


root = Vertex("Practice2", "../../Practice2", "dir")
scan_dir("../../Practice2", root)
root.dfs_print()
root.dfs_print_fancy(0, True)