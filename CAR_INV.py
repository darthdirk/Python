class coolAutomobileInventory:
    automobile_list = []
    def __init__(self, make, model, color, year, mileage):
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = year
        self.__mileage = mileage
        coolAutomobileInventory.automobile_list.append(self)
    def add_automobile(automobile):
        coolAutomobileInventory.automobile_list.append(automobile)
    def del_veh(automobile_name):
        for automobile in coolAutomobileInventory.automobile_list:
            if automobile.get_make()==automobile_name:
                coolAutomobileInventory.automobile_list.remove(automobile)
    def del_automobile(self):
        if self in coolAutomobileInventory.automobile_list:
            coolAutomobileInventory.automobile_list.remove(self)
            self = None
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_color(self):
        return self.__color
    def get_year(self):
        return self.__year
    def get_mileage(self):
        return self.__mileage
    def set_make(self, value):
        self.__make = value
    def set_model(self, value):
        self.__model = value
    def set_color(self, value):
        self.__color = value
    def set_year(self, value):
        self.__year = value
    def set_mileage(self, value):
        self.__mileage = value
    def __str__(self):
        return "automobile make: " + self.get_make() + " model: " + str(
            self.get_model()) + " color: " + self.get_color() + " year: " + str(self.get_year()) + " mileage: " + str(
            self.get_mileage())
def menu():
    print("Enter choice")
    print("1. Add automobile")
    print("2. Delete automobile")
    print("3. exit")
    choice=input()
    return choice
def main():
    while True:
        choice=int(menu())
        if choice==1:
            print("Enter automobile name")
            name=input()
            make=input("Enter automobile make")
            color=input("Enter automobile color")
            year=input("Enter automobile year")
            mileage=input("Enter automobile mileage")
            model=input("Enter automobile model")
            automobile = coolAutomobileInventory(name, model, color, year, mileage)
        elif choice==2:
            name=input("Enter automobile name")
            coolAutomobileInventory.del_veh(name)
        elif choice==3:
            break
main()
file = open("inventory.txt", "w")
for v in coolAutomobileInventory.automobile_list:
    file.write(str(v) + "\n")
