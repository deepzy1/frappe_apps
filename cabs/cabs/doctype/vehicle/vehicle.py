# Copyright (c) 2025, Deepak R and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Vehicle(WebsiteGenerator):
	def before_save(self):
		self.set_title()
		# self.title=f"{self.make} {self.model}  {self.year}"
	def set_title(self):
		self.title=f"{self.make}{self.model}{self.year}"
	pass
