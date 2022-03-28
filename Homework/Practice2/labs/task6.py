def main_old_0(x):
    if x[3] == "VCL":
        if x[0] == "KRL":
            if x[1] == "ALLOY":
                return 0
            else:
                return 1
        elif x[0] == "TEA":
            return 2
        else:
            return 3
    elif x[3] == "OPA":
        if x[1] == "ALLOY":
            if x[0] == "KRL":
                return 4
            elif x[0] == "TEA":
                return 5
            else:
                return 6
        else:
            return 7
    else:
        if x[1] == "ALLOY":
            if x[2] == "EJS":
                return 8
            else:
                return 9
        else:
            return 10


def main_old_1(x):
    if x[3] == "VCL" and x[0] == "KRL" and x[1] == "ALLOY":
        return 0
    elif x[3] == "VCL" and x[0] == "KRL" and x[1] == "YANG":
        return 1
    elif x[3] == "VCL" and x[0] == "TEA":
        return 2
    elif x[3] == "VCL" and x[0] == "PAWN":
        return 3
    elif x[3] == "OPA" and x[1] == "ALLOY" and x[0] == "KRL":
        return 4
    elif x[3] == "OPA" and x[1] == "ALLOY" and x[0] == "TEA":
        return 5
    elif x[3] == "OPA" and x[1] == "ALLOY" and x[0] == "PAWN":
        return 6
    elif x[3] == "OPA" and x[1] == "YANG":
        return 7
    elif x[3] == "NCL" and x[1] == "ALLOY" and x[2] == "EJS":
        return 8
    elif x[3] == "NCL" and x[1] == "ALLOY" and x[2] == "TOML":
        return 9
    else:
        return 10


class VertexPair:
    def __init__(self, key_to_next, vertex_value, vertex_index):
        self.key_to_next = key_to_next
        self.next_vertex = Vertex(vertex_value, vertex_index)

    def __str__(self):
        return f"VertexPair: key_to_next={self.key_to_next}"


class Vertex:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.vertex_pair_list = []

    def add_pair(self, key_to_next, vertex_index, vertex_value=-1):
        self.vertex_pair_list.append(VertexPair(key_to_next, vertex_value, vertex_index))

    def __str__(self):
        return f"Vertex: value={self.value}, index={self.index}, vertex_pair_list length={len(self.vertex_pair_list)}"


def special_dfs(current_array, current_vertex):
    if current_vertex.value != -1:
        return current_vertex.value
    for vertex_pair in current_vertex.vertex_pair_list:
        if current_array[current_vertex.index] == vertex_pair.key_to_next:
            return special_dfs(current_array, vertex_pair.next_vertex)


def main_old_2(x):
    task_tree = Vertex(-1, 3)
    task_tree.add_pair("VCL", 0)
    task_tree.add_pair("OPA", 1)
    task_tree.add_pair("NCL", 1)
    task_tree.vertex_pair_list[0].next_vertex.add_pair("KRL", 1)
    task_tree.vertex_pair_list[0].next_vertex.add_pair("TEA", -1, 2)
    task_tree.vertex_pair_list[0].next_vertex.add_pair("PAWN", -1, 3)
    task_tree.vertex_pair_list[1].next_vertex.add_pair("ALLOY", 0)
    task_tree.vertex_pair_list[1].next_vertex.add_pair("YANG", -1, 7)
    task_tree.vertex_pair_list[2].next_vertex.add_pair("ALLOY", 2)
    task_tree.vertex_pair_list[2].next_vertex.add_pair("YANG", -1, 10)
    task_tree.vertex_pair_list[0].next_vertex.vertex_pair_list[0].next_vertex.add_pair("ALLOY", -1, 0)
    task_tree.vertex_pair_list[0].next_vertex.vertex_pair_list[0].next_vertex.add_pair("YANG", -1, 1)
    task_tree.vertex_pair_list[1].next_vertex.vertex_pair_list[0].next_vertex.add_pair("KRL", -1, 4)
    task_tree.vertex_pair_list[1].next_vertex.vertex_pair_list[0].next_vertex.add_pair("TEA", -1, 5)
    task_tree.vertex_pair_list[1].next_vertex.vertex_pair_list[0].next_vertex.add_pair("PAWN", -1, 6)
    task_tree.vertex_pair_list[2].next_vertex.vertex_pair_list[0].next_vertex.add_pair("EJS", -1, 8)
    task_tree.vertex_pair_list[2].next_vertex.vertex_pair_list[0].next_vertex.add_pair("TOML", -1, 9)
    return special_dfs(x, task_tree)


def solve_zero(x, left_result, middle_result, right_result):
    if x[0] == "KRL":
        return left_result
    if x[0] == "TEA":
        return middle_result
    if x[0] == "PAWN":
        return right_result


def solve_first(x, left_result, right_result):
    if x[1] == "ALLOY":
        return left_result
    if x[1] == "YANG":
        return right_result


def solve_second(x, left_result, right_result):
    if x[2] == "EJS":
        return left_result
    if x[2] == "TOML":
        return right_result


def solve_third(x, left_result, middle_result, right_result):
    if x[3] == "VCL":
        return left_result
    if x[3] == "OPA":
        return middle_result
    if x[3] == "NCL":
        return right_result


def main(x):
    return solve_third(x,
                       solve_zero(x, solve_first(x, 0, 1), 2, 3),
                       solve_first(x, solve_zero(x, 4, 5, 6), 7),
                       solve_first(x, solve_second(x, 8, 9), 10))


main(['KRL', 'ALLOY', 'TOML', 'VCL'])
main(['PAWN', 'ALLOY', 'TOML', 'OPA'])

print(main(['KRL', 'ALLOY', 'TOML', 'VCL']))
print(main(['PAWN', 'ALLOY', 'TOML', 'OPA']))
