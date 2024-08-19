class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        for i in range(new_floor):
            j = i + 1
            if new_floor < self.number_of_floors:
                print(j)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: "{self.name}", количество этажей:  {self.number_of_floors}'


h1 = House('ЖК Авангард', 15)
h2 = House('ЖК Лилия', 25)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
