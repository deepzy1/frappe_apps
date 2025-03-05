import frappe

def execute():
    Vehicles=frappe.db.get_all("Vehicle",pluck="name")
    for v in Vehicles:
        print("vehicle::",v,"type::",type(v))
        Vehicle=frappe.get_doc("Vehicle",v)
        Vehicle.set_title()
        Vehicle.save()
    frappe.db.commit()

    