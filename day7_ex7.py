def calculate_price(pizza, topping_price ):
    total_sum = 0
    for topping in pizza:
        total_sum  += pizza[topping] * topping_price[topping]
    return  total_sum 

def Calculate_Sales_Price(pizza, topping_price ):
    return (calculate_price(pizza, topping_price) * 1.5)

def print_one_day_price_list(pizza_list, topping_price, counter):
    count = 1
    for pizza in pizza_list:
        if count == counter:
            print( count,'Sale:', pizza.ljust(20, " "),"%6.2f" %  calculate_price(pizza_list[pizza], topping_price ),'€')
        else:
            print( count, pizza.ljust(26, " "), "%6.2f" % Calculate_Sales_Price(pizza_list[pizza], topping_price ),'€') 
        count += 1

def print_extra_toppings(toppings):
    extra_toppings = ''
    for my_topping in toppings: 
        if len(extra_toppings) == 0:
            extra_toppings += my_topping
        else:
            extra_toppings +=  ', ' + my_topping
    print('Extra Toping:',extra_toppings)

def print_all_prices(day_list, pizza_list, topping_price):
    counter = 1
    for day in day_list:
        print('Our Pizza List Of',day+':')
        print()
        print_one_day_price_list(pizza_list, topping_price,counter)
        counter += 1
        print()

day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']    
toppings = ['mozzarella','tomato','eggplant','tuna','olives','anchovies','capers','goat cheese','ham','truffle','pecorino','portobello mashrooms','truffle pesto','yello tomato','basil','nduja','res onion','shrimps','garlic','parsley']
topping_price = {'mozzarella':2,'tomato':2,'eggplant':3,'tuna':4,'olive':2,'anchovies':3,'capers':2,'goat cheese':3,'ham':5,'truffle':6,'pecorino':5,'portobello mashrooms':3,'truffle pesto':3,'yello tomato':4,'basil':2,'nduja':3,'red onion':2,'shrimps':4,'garlic':2,'parsley':2}

margarita ={'tomato':2 ,'mozzarella':1}
sicilia = {'tomato':2,'mozzarella':1,'eggplant':1,'goat cheese':1}
tartufina = {'ham':4,'truffle':1,'pecorino':3,'portobello mashrooms':3,'truffle pesto':1}
sorrentina = {'tomato':1,'mozzarella':2,'olive':5,'capers':5,'anchovies':4,'yello tomato':3,'basil':5}
calabrina ={'tomato':3,'mozzarella':2,'nduja':6,'portobello mashrooms':4,'red onion':4,'pecorino':3}
mazzarani ={'tomato':3,'mozzarella':4,'yello tomato':4,'shrimps':7,'garlic':1,'parsley':5}
marinella = {'tomato':2,'mozzarella':3,'yello tomato':2,'tuna':2,'olive':6,'parsley':4}

pizza_list = {'Margarita': margarita, 'Sicilia': sicilia, 'Tartufina': tartufina, 'Sorrentins': sorrentina, 'Calabria': calabrina, 'Mazzarani':mazzarani, 'Marinella': marinella}
print()
print_all_prices(day_list, pizza_list, topping_price)
print_extra_toppings(toppings)





# 7) Create an algorithm that prints out a price list with a title and all
#  the pizzas in our restaurant.
#  Additionally it prints all available topping below the price list.
#  Example: