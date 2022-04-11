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

    def dfs_print_fancy(self, length=0):
        print(("\t" * (length + 1)) + "subgraph " + self.name + " {")
        print(("\t" * (length + 2)) + "node [style=filled,color=grey" + "];")
        for el in self.children:
            print(("\t" * (length + 2)) + self.name + " -> \"" + el.name + "\"")
            if el.type == "dir":
                el.dfs_print_fancy(length + 1)
        print(("\t" * (length + 1)) + "}")


def scan_dir(dir, vertex):
    for name in os.listdir(dir):
        if name != "__init__.py":
            path = os.path.join(dir, name)
            if os.path.isfile(path):
                vertex.children.append(Vertex(name, path, "file"))
            else:
                vertex.children.append(Vertex(name, path, "dir"))
                scan_dir(path, vertex.children[-1])


def print_graph_fancy(root):
    print("digraph G {")
    root.dfs_print_fancy()
    print("\tstart -> \"" + root.name + "\"")
    print("\tstart [shape=Mdiamond];")
    print("}")


root = Vertex("Practice2", "../../Practice2", "dir")
scan_dir("../../Practice2", root)
print_graph_fancy(root)