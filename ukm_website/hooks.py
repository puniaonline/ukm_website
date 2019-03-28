# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "ukm_website"
app_title = "Ukm Website"
app_publisher = "INC"
app_description = "Theme For Punia UKM"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "dev@punia.online"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ukm_website/css/ukm_website.css"
# app_include_js = "/assets/ukm_website/js/ukm_website.js"

# include js, css files in header of web template
# web_include_css = "/assets/ukm_website/css/ukm_website.css"
# web_include_js = "/assets/ukm_website/js/ukm_website.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
 #home_page = "index"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "ukm_website.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ukm_website.install.before_install"
# after_install = "ukm_website.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ukm_website.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ukm_website.tasks.all"
# 	],
# 	"daily": [
# 		"ukm_website.tasks.daily"
# 	],
# 	"hourly": [
# 		"ukm_website.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ukm_website.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ukm_website.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ukm_website.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ukm_website.event.get_events"
# }

#custom hook

