#!/usr/bin/env python3
# My solution to the following challenge: https://redd.it/39ws1x

# I'm probably going to have to redo this whole thing to use a dictornary.

from datetime import date

class ToDo():
	def __init__(self):
		self.items = []

	def addItem(self, item, category='default'):
		if not item:
			print("You cannot add a blank item.")
			return

		self.items.append([item, category])
	
	def removeItem(self, item):
		# This has got to be fixed to accomdate for categories.
		if item in self.items:
			self.items.remove(item)
	
	def list(self):
		for item in self.items:
			print(self.items)

if __name__ == '__main__':
	pass	
