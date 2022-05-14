import random
import matplotlib.pyplot as plt
import time


class SchellingModel:
    def __init__(self,
                 population_number,
                 field_width,
                 field_height,
                 groups_ratio,
                 max_tolerance,
                 steps_number):
        self.population_number = population_number
        self.field_width = field_width
        self.field_height = field_height
        self.groups_ratio = groups_ratio
        self.max_tolerance = max_tolerance
        self.steps_number = steps_number
        self.field = []
        self.people = []
        self.happiness = []

    def createModel(self):
        for i in range(self.field_height):
            self.field.append([])
            for j in range(self.field_width):
                self.field[i].append(0)
        first_group_number = self.population_number * self.groups_ratio
        for i in range(self.population_number):
            current_cell_number = random.randint(0, self.field_width * self.field_height - len(self.people) - 1)
            x, y = self.giveCoordinationsOfNthCell(current_cell_number)
            group = (1 if i < first_group_number else 2)
            person = Person(x, y, group, self.max_tolerance)
            person.move(self.field, x, y)
            self.people.append(person)

    def giveCoordinationsOfNthCell(self, number):
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if self.field[i][j] == 0:
                    if number == 0:
                        print(j, i)
                        return j, i
                    else:
                        number -= 1

    def startSimulation(self):
        for i in range(self.steps_number):
            current_happiness = 0
            for person in self.people:
                current_happiness += (1 if person.isHappy(self.field) else 0)
                if not person.isHappy(self.field):
                    cells_left = self.field_width * self.field_height - self.population_number
                    new_x, new_y = self.giveCoordinationsOfNthCell(random.randint(0, cells_left - 1))
                    person.move(self.field, new_x, new_y)
            self.happiness.append(current_happiness)


class Person:
    def __init__(self, x, y, group, max_tolerance):
        self.x = x
        self.y = y
        self.group = group
        self.max_tolerance = max_tolerance

    def move(self, field, new_x, new_y):
        field[self.y][self.x] = 0
        self.x = new_x
        self.y = new_y
        field[self.y][self.x] = self.group

    def isHappy(self, field):
        number_of_others = 0
        if self.y != 0:
            number_of_others += (0 if field[self.y - 1][self.x] == self.group else 1)
        if self.y != len(field) - 1:
            number_of_others += (0 if field[self.y + 1][self.x] == self.group else 1)
        if self.x != 0:
            number_of_others += (0 if field[self.y][self.x - 1] == self.group else 1)
        if self.x != len(field[0]) - 1:
            number_of_others += (0 if field[self.y][self.x + 1] == self.group else 1)
        return self.max_tolerance >= number_of_others

    def getDistance(self, new_x, new_y):
        return abs(new_x - self.x) + abs(new_y - self.y)


model = SchellingModel(70, 10, 10, 0.5, 2, 20)
model.createModel()
plt.imshow(model.field)
plt.show()
model.startSimulation()
plt.imshow(model.field)
plt.show()
plt.plot(model.happiness, range(model.steps_number))
plt.show()
