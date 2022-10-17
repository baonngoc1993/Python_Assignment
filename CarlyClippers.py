#!/bin/python3

# provided with three lists:

hairstyles = ["bouffant","pixie","dreadlocks","crew","bowl","bob","mohawk","flattop"]

prices = [30,25,40,20,20,35,50,35]

last_week =[2,3,5,8,4,4,6,2]

# sum up all the prices of haircuts

total_price = 0

for price in prices:
	total_price = total_price + price
	print(total_price)
# average price

average_price = total_price /len(prices)
print("Average Haircut Price: " + str(average_price))

#comprehension list

new_prices = [price-5 for price in prices]
print(new_prices)

#Revenue
total_revenue = 0
for i in range(len(hairstyles)):
	total_revenue = prices[i] + last_week[i]
	print("Total Revenue: " + str(total_revenue))

#average daily revenue 

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# create a list cuts under 30

cut_under_30 = [new_prices[i] for i in range(len(new_prices)-1)if new_prices[i] < 30]
print(cut_under_30)
