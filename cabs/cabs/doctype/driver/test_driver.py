# Copyright (c) 2025, Deepak R and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestDriver(FrappeTestCase):

	def test_full_name(self):
		test_driver = frappe.new_doc("Driver")
		test_driver.first_name="Bin"
		test_driver.last_name="Sharma"
		test_driver.save()
		self.assertEqual(test_driver.full_name,"Bin Sharma")

	def test_name_without_last_name(self):
		test_driver = frappe.new_doc("Driver")
		test_driver.first_name="Ravi"
		# test_driver.last_name="Sharma"
		test_driver.save()
		self.assertEqual(test_driver.full_name,"Ravii")

			


		
	
