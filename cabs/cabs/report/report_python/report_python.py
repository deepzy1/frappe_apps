# Copyright (c) 2025, deepak and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):

	frappe.errprint(filters)

	
	columns= [{
		"fieldname":"make",
		'label':"make",
		"fieldtype":"Data"
	},{
		"fieldname":"total_revenue",
		'label':"Revenue",
		"fieldtype":"Currency",
		"options":"AED"
	},]

	data = frappe.get_all(
		"Ride Booking",
		fields=["SUM(amount) AS total_revenue",'vehicle.make'],
		filters={"docstatus":1},group_by= "make")
	
	chart= {
		"data":{
			   "labels":[x.make for x in data],
				"datasets":[{
				"values": [x.total_revenue for x in data]
				},
				],
			},
		"type":"pie",
	}

	


					   



	return columns, data , "Custom chart by deepak" , chart
