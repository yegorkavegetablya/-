class MyDictionary:
    def __init__(self):
        self.values = []
        self.keys = []
        self.iterator_counter = 0

    def __getitem__(self, key):
        return self.values[self.keys.index(key)]

    def __setitem__(self, key, value):
        if self.keys.count(key):
            self.values[self.keys.index(key)] = value
        else:
            self.keys.append(key)
            self.values.append(value)

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterator_counter >= len(self.keys):
            raise StopIteration
        else:
            result = (self.keys[self.iterator_counter], self.values[self.iterator_counter])
            self.iterator_counter += 1
            return result


d = MyDictionary()
d["1"] = 2
d[2] = set()
d[3.5] = "12345"
print(d[2], d[3.5], d["1"])
for el in d:
    print(el)
assert dict() == MyDictionary(), "Нет, это разные классы"
d2 = dict()
d2["1"] = 2
d2[2] = set()
d2[3.5] = "12345"
assert d["1"] == d2["1"], "странно"
assert d[2] == d2[2], "странно"
assert d[3.5] == d2[3.5], "странно"


