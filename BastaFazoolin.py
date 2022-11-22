#!/bin/python3

class menu:
	def __init__(self, name, items, start_time, end_time):
		self.name = name 
		self.items = items
		self.start_time = start_time
		self.end_time = end_time 

	def __repr__(self):
		return self.name + ' menu available from ' + str(self.start_time) + ' - ' + str(self.end_time)


	def calculate_bill(self,purchased_items):
		self.purchased_items = purchased_items
		bill = []
		for purchased_item in purchased_items:
			if purchased_item in self.items:
				bill += self.items[purchase_item]
		return sum(bill)
class Business:
	def __init__(self,name, fanchises):
		self.name = name 
		self.fanchises = fanchises

class Franchise:
	def __init__(self,address,menus):
		self.address = address
		self.menus = menus
	def __repr__(self):
		return " store is located at {location}.".format(location = self.address)

	def available_menu(self,time):
		available_menu=[]
		for menu in slef.menus:
			if time >= menu.start_time and time <= menu.end_time:
				available_menus.append(menu)
			return available_menu
#menu 

brunch = {
	 'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
	}

brunch_menu = menu('brunch', brunch,11,4)
print(brunch_menu)
print( brunch.purchased_items(['pancakes','home fries','coffee']))

early_bird = {
	'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,

}

early_bird = menu('early_bird',early_bird,3,6)
print(early_bird)

dinner = {

  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,

}
dinner_menu = menu('dinner',dinner,5,11)
print(dinner_menu)

kid = {

  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00

}



flagship_store = franchise('1232 West End Road', menus)

installemt = franchise('12 Easr Mulberry Street' menus)
# new business
arepas_menu ={

  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50

}
arepas_menu =('arepas_menu',arepas_menu,10,8)

arepas_place = franchise('198 Fitzgerald Avenue',[arepas_menu])

arepas = business("Take a 'Arepa",[arepas_place])

