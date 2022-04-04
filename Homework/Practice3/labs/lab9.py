class GraphVertex:
    def __init__(self, has_dash, has_send,
                 value_dash, value_send, next_dash, next_send):
        self.has_dash = has_dash
        self.has_send = has_send
        self.value_dash = value_dash
        self.value_send = value_send
        self.next_dash = next_dash
        self.next_send = next_send


class Graph:
    def __init__(self, root):
        self.current_vertex = root

    def dash(self):
        if self.current_vertex.has_dash:
            value = self.current_vertex.value_dash
            self.current_vertex = self.current_vertex.next_dash
            return value
        else:
            raise KeyError

    def send(self):
        if self.current_vertex.has_send:
            value = self.current_vertex.value_send
            self.current_vertex = self.current_vertex.next_send
            return value
        else:
            raise KeyError


def main():
    vertex6 = GraphVertex(False, True, None, 9, None, None)
    vertex6.next_send = vertex6
    vertex5 = GraphVertex(True, False, 8, None, vertex6, None)
    vertex4 = GraphVertex(False, True, None, 7, None, vertex5)
    vertex3 = GraphVertex(True, False, 6, None, vertex4, None)
    vertex2 = GraphVertex(True, True, 4, 5, vertex3, vertex5)
    vertex1 = GraphVertex(True, True, 2, 3, vertex2, vertex5)
    vertex0 = GraphVertex(True, True, 0, 1, vertex1, vertex6)
    return Graph(vertex0)


o = main()
# o.dash()  # 0
# o.dash()  # 2
# o.dash()  # 4
# o.dash()  # 6
# o.send()  # 7
# o.dash()  # 8
# o.send()  # 9
# o.send()  # 9
o = main()
# o.dash()  # 0
# o.dash()  # 2
# o.dash()  # 4
# o.dash()  # 6
# o.dash()  # KeyError
# o.send()  # 7
# o.dash()  # 8
# o.send()  # 9
# o.send()  # 9
# o.send()  # 9
# o.send()  # 9
# o.send()  # 9
# o.send()  # 9
# o.send()  # 9
# o.send()  # 9

o = main()
print(o.dash())
print(o.dash())
print(o.dash())
print(o.dash())
print(o.send())
print(o.dash())
print(o.send())
print(o.send())
o = main()
print(o.dash())
print(o.dash())
print(o.dash())
print(o.dash())
print(o.dash())
print(o.send())
print(o.dash())
print(o.send())
print(o.send())
print(o.send())
print(o.send())
print(o.send())
print(o.send())
print(o.send())
print(o.send())
