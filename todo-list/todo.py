#!/usr/bin/env python3
# My solution to the following challenge: https://redd.it/39ws1x

from datetime import date

class ToDo():
	def __init__(self, date=date.today()):
		self.items = []
		self.date = date

	def addItem(self, item):
		if not item:
			print("You cannot add a blank item.")
			return

		self.items.append(item)
	
	def removeItem(self, item):
		if item in self.items:
			self.items.remove(item)
	
	def list(self):
		print("To Do List for {0}".format(self.date))
		print(self.items)

if __name__ == '__main__':
	today = ToDo()
	today.addItem('Take a shower.')
	today.addItem('Go to work.')
	# Try to add a blank item. This should fail.
	today.addItem('')
	today.list()
	today.removeItem('Go to work.')
	today.list()
