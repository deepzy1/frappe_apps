import frappe

cars=[]
@frappe.whitelist(allow_guest=True)
def get_car():
    cars=["Bugati","Lambo","Ferrari"]
    return cars


def throw_emoji(doc,event):
    frappe.throw("🔱")

def demo_cron():
    pass

def query_conditions(user):
    frappe.throw(user)
    return "name=1"
    