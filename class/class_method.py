class Worker():
    def __init__(self, fullname, area, salary = 700):
        self.fullname = fullname
        self.area = area
        self.salary = salary 
    
    def show_info(self):
        print(f"Hello I'm {self.fullname}, I work in {self.area}, and I earn {self.salary}")

juan = Worker("Juan Perez", "sales", salary = 1400)
david = Worker("David Perez", "IT", salary = 2000)

juan.show_info()
david.show_info()

