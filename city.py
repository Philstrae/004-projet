# -*- coding:utf8 -*-

def cities(country, *cities):
    print(country, cities)
    print("Type is ", type(cities))

cities("France")

cities("France", "Roubaix", "Lille", "Tourcoing", "Croix")
cities("Belgique", "Namur", "Bruxelles", "Gand", "Tournai")
cities("Angleterre", "Londres", "Manchester", "Cardiff")
cities("Lyon","Lille", "Rouen", "France")
