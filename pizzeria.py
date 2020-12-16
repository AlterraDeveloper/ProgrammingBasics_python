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
    

class Order(object):

    _pizzas = []
    pizzas = {}
    
    isApproved = False

    def addPizza(self, pizza):
        self._pizzas.append(pizza)
        pizzaName = type(pizza).__name__
        if pizzaName in self.pizzas.keys():
            self.pizzas[pizzaName] = self.pizzas[pizzaName] + 1
        else:
            self.pizzas[pizzaName] = 1

    def removePizza(self, pizza):
        if self.isApproved : return
        self._pizzas.remove(pizza)
        pizzaName = type(pizza).__name__
        if pizzaName in self.pizzas.keys():
             self.pizzas[pizzaName] = self.pizzas[pizzaName] - 1

    def getTotal(self):
        total = 0
        for pizza in self._pizzas: total += pizza.price
        return total  

    def approve(self): self.isApproved = True

class Terminal(object):
    
    menu = [Pepperoni('40 cm, round', 'tomato sauce', 450), Bbq('30 cm, square', 'BBQ sauce', 550)]

    def takeOrder(self):
        while True:
            action = input("""
Добро пожаловать!
Выберите действие:
1. Сделать заказ
2. Посмотреть меню
""")

            if action == '1': 
                self.currentOrder = Order()
                print('Ваш заказ успешно создан!')
                while not self.currentOrder.isApproved:
                    pizzaSelect = input("""
Какую пиццу будете заказывать?
1. Пепперони
2. Барбекю
Может быть вы хотите удалить свой выбор из заказа?
3. удалить Пепперони
4. удалить Барбекю
""")
                    # print("{}".format(int(pizzaSelect))
                    if pizzaSelect == "1" or pizzaSelect == "2": 
                            self.currentOrder.addPizza(self.menu[int(pizzaSelect)-1])
                    elif pizzaSelect == '3' or pizzaSelect == '4': self.currentOrder.removePizza(self.menu[int(pizzaSelect)-3])
                    else: 
                        print('Не понял вас, попробуйте еще раз...')
                        continue

                    approve = input('Вы подтверждаете свой заказ? [Да/Нет]')
                    if approve == 'Да':
                        self.currentOrder.isApproved = True
                        print('Повторю ваш заказ:')
                        print(self.currentOrder.pizzas)
                        print('Итого : {}'.format(self.currentOrder.getTotal()))
                        break
                    elif approve == 'Нет': continue
            if action == '2':
                for pizza in self.menu: print(pizza)
                    



########################################################################################################
pizza_Pepperoni = Pepperoni('40 cm, round', 'tomato sauce', 450)
pizza_BBQ = Bbq('30 cm, square', 'BBQ sauce', 550)

order = Order()
order.addPizza(pizza_Pepperoni)
order.addPizza(pizza_Pepperoni)
order.addPizza(pizza_BBQ)

print(order.pizzas)
print(order.getTotal())
order.removePizza(pizza_Pepperoni)
print(order.pizzas)
print(order.getTotal())

terminal1 = Terminal()

terminal1.takeOrder()


# print(pizza_Pepperoni, end='\n')
# print(pizza_BBQ, end='\n')
