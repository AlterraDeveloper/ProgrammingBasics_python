class Ingredient(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Pizza(object):
    dough = ''
    sauce = ''
    Ingredients = []

    def __init__(self, dough, sauce, price):
        self.dough = dough
        self.sauce = sauce
        self.price = price

    def __str__(self):
        pizza_internals = ''
        pizza_internals += "dough = '{}'\n".format(self.dough)
        pizza_internals += "sauce = '{}'\n".format(self.sauce)
        for ingr in self.Ingredients : pizza_internals += "{}...............{}\n".format(ingr.name, ingr.weight)
        pizza_internals += '-----------------------------\n'
        pizza_internals += "Price\t\t\t{}\n".format(self.price)
        return  pizza_internals


class Pepperoni(Pizza):
    Ingredients = [
        Ingredient('pepperoni', 300),
        Ingredient('tomato', 150),
        Ingredient('cheese', 200)
    ]

    def __init__(self, dough, sauce, price):
        super().__init__(dough, sauce, price)
    
    def __str__(self):
        return "-----------------------------\n\tPepperoni Pizza\n{}".format(super().__str__())

class Bbq(Pizza):
    Ingredients = [
        Ingredient('pepperoni', 300),
        Ingredient('tomato', 150),
        Ingredient('cheese', 200)
    ]

    def __init__(self, dough, sauce, price):
        super().__init__(dough, sauce, price)

    def __str__(self):
        return "-----------------------------\n\tBBQ Pizza\n{}".format(super().__str__())
    

class Terminal(object):
    


########################################################################################################
pizza_Pepperoni = Pepperoni('40 cm, round', 'tomato sauce', 450)
pizza_BBQ = Pepperoni('30 cm, square', 'BBQ sauce', 550)

print(pizza_Pepperoni, end='\n')
print(pizza_BBQ, end='\n')



