class DemoClass:
    num = 101

    # parameterized constructor
    def __init__(self, data):
        self.num = data

    # a method
    def read_number(self):
        print(self.num)


obj = DemoClass(55)

# calling the instance method using the object obj
obj.read_number()

# creating another object of the class
obj2 = DemoClass(66)

# calling the instance method using the object obj
obj2.read_number()


if x = 5:
    pass
elif (random.randint(0,100) < 2):
            propertySelection = random.randint(0,2)
            if (propertySelection == 0):
                mutation = random.randint(0, baseEnergy)
                self.baseEnergy = baseEnergy - mutation
                propertySelection = random.randint(0,1)
                if (propertySelection == 0):
                    self.viewDistance = viewDistance + mutation
                else:
                    self.movementEfficiency = movementEfficiency + mutation
            elif (propertySelection == 1):
                mutation = random.randint(0, viewDistance)
                self.viewDistance = viewDistance - mutation
                propertySelection = random.randint(0,1)
                if (propertySelection == 0):
                    self.baseEnergy = baseEnergy + mutation
                else:
                    self.movementEfficiency = movementEfficiency + mutation
            else:
                mutation = random.randint(0, movementEfficiency)
                self.movementEfficiency = movementEfficiency - mutation
                propertySelection = random.randint(0,1)
                if (propertySelection == 0):
                    self.baseEnergy = baseEnergy + mutation
                else:
                    self.viewDistance = viewDistance + mutation
            self.energy = baseEnergy