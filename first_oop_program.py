class master:
    def __init__(self, name):
        self.name = name
    def teach(self,socc):
        print(socc)
    def sing(self):
        print(f"{self.name} is a famous singer")
m = master('D\'costa')
m.teach("bassbaba")
m.sing()