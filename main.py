class House:
    def __init__(self, name, number_of_flors):
        self.name = name
        self.number_of_flors = number_of_flors

    def go_to(self, new_floor):
        if new_floor > self.number_of_flors or new_floor < 1:
            print ('такого этажа не существует')
        else:
            #print(f'надо приехать на {new_floor} этаж') #как вариант прописать куда ехать вместо перечисления каждого этажа
            for floor in range (1, new_floor + 1):
                print (floor)
    def __len__(self):
        return self.number_of_flors
    def __str__(self):
        return (f"название:{self.name}, количество этажей:{self.number_of_flors}")


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

#стр
print(h1)
print(h2)

#len
print(len(h1))
print(len(h2))


