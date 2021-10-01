class Automobile:
    def __init__(self, name, color, model, mileage, cost):
        self.name=name
        self.color=color
        self.model=model
        self.mileage=mileage
        self.cost=cost
    def get_name(self):
        return self.name
    def get_color(self):
        return self.color
    def get_model(self):
        return self.model
    def get_mileage(self):
        return self.mileage
    def get_cost(self):
        return self.color
    def set_name(self, value):
        self.name=value
    def set_color(self, value):
        self.color=value
    def set_model(self, value):
        self.model=value
    def set_mileage(self, value):
        self.mileage=value
    def set_cost(self, value):
        self.cost=value
