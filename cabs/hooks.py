app_name = "cabs"
app_title = "cabs"
app_publisher = "deepak"
app_description = ".."
app_email = "h@j"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "cabs",
# 		"logo": "/assets/cabs/logo.png",
# 		"title": "cabs",
# 		"route": "/cabs",
# 		"has_permission": "cabs.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/cabs/css/cabs.css"
# app_include_js = "/assets/cabs/js/cabs.js"

# include js, css files in header of web template
# web_include_css = "/assets/cabs/css/cabs.css"
# web_include_js = "/assets/cabs/js/cabs.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "cabs/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "cabs/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "cabs.utils.jinja_methods",
# 	"filters": "cabs.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "cabs.install.before_install"
# after_install = "cabs.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "cabs.uninstall.before_uninstall"
# after_uninstall = "cabs.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "cabs.utils.before_app_install"
# after_app_install = "cabs.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "cabs.utils.before_app_uninstall"
# after_app_uninstall = "cabs.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "cabs.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }

# permission_query_conditions = {
# 	"Vehicle": "cabs.api.query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# fixtures = [["dt": "Vehicle Type", "filters": "is_standard": 1}]

fixtures=["Vehicle Type",'Rental Settings']

# fixtures =[{'dt':"Vehicle Type",'filters':{"available":1}}]

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# apps/cabs/cabs/api.py

doc_events = {
	"ToDo": {
		"before_insert":"cabs.api.throw_emoji"
	}
}

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"cabs.tasks.all"
# 	],
# 	"daily": [
# 		"cabs.tasks.daily"
# 	],
# 	"hourly": [
# 		"cabs.tasks.hourly"
# 	],
# 	"weekly": [
# 		"cabs.tasks.weekly"
# 	],
# 	"monthly": [
# 		"cabs.tasks.monthly"
# 	],
# }

scheduler_events = {
    "Cron":{
        "33 15 * * 3": [
		"cabs.api.demo_cron"
	]
    }
	
}
	


# Testing
# -------

# before_tests = "cabs.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "cabs.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "cabs.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["cabs.utils.before_request"]
# after_request = ["cabs.utils.after_request"]

# Job Events
# ----------
# before_job = ["cabs.utils.before_job"]
# after_job = ["cabs.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"cabs.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

