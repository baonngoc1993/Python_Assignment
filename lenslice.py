#!/bin/python3

#Task 1
toppings = [ "pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms" ]

#Task 2
prices = [ 2,6,1,3,2,7,2 ]

#Task 3
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices) 

#Task 4
num_pizzas = len(toppings)
print(num_pizzas)

print("We sell " + str( num_pizzas ) + " different kinds of pizza!")

#Task 5
pizza_and_prices = [[2,"pepperoni"],[6,"pipeapple"],[1,"chesse"],[3,"sausage"],[2,"olives"],[7,"anchovies"],[2,"mushrooms"]]
print(pizza_and_prices)

sort_pizza_and_prices = pizza_and_prices.sort()
print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0][1]
print(cheapest_pizza)

priciest_pizza = pizza_and_prices[6][-1]
print(priciest_pizza)

pizza_and_prices.pop(6)
print(pizza_and_prices)

pizza_and_prices.append([2.5,"peppers"])
pizza_and_prices.sort()
print(pizza_and_prices)

three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)
