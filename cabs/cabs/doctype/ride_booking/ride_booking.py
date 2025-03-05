# Copyright (c) 2025, deepak and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document


class RideBooking(Document):
	# def validate(self):
	# 	total_distance=0
	# 	ride=frappe.get_doc("Ride Booking",self)
	# 	for item in ride.items:
	# 		total_distance+=item.distance
	# 	ride.amount=total_distance*ride.rate
	# 	ride.save()
	# 	frappe.db.commit()
	
	def validate(self):
		if not self.rate:
			self.rate=frappe.db.get_single_value("Rental Settings","standard_rate")

			# frappe.throw("Please provide a rate")

		total_distance=0
		for item in self.items:
			total_distance+=item.distance
		self.amount=total_distance*self.rate
