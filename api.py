import flask_restful as restful
import json
from flask import Flask, request
from flask_cors import CORS
from EmailNotifyr import EmailNotifyr	# config imported here
from CronManager import CronManager
from get_config import *

################# API RESPONSE FORMAT #################
# {
# 	'success': True,
# 	'message': '',
# 	'error_code': 12,	# if success == False
# 	'data': []
# 	'count': 0
# }
################# API RESPONSE FORMAT #################

# service method classes
class SendEmail(restful.Resource):
	def post(self):
		data = request.get_json()

		obj = EmailNotifyr()
		obj.send_mail(data['subject'], data['body'], data.get('to', []), data.get('cc', []))
	    
		return {'success': True, 'message': 'Email sent Successfully'}

class GetAllCrons(restful.Resource):
	def post(self):
		# data = request.get_json()

		obj = CronManager()
		res = obj.get_all_crons()
	    
		return {'success': True, 'message': 'Request Successful', 'data': res}

class ActivateCron(restful.Resource):
	def post(self):
		data = request.get_json()

		obj = CronManager()
		res = obj.activate_cron(data['script'], data['rules'])
	    
		return {'success': res, 'message': 'Cron Activated Successfully', 'data': res}

class DeactivateCron(restful.Resource):
	def post(self):
		data = request.get_json()

		obj = CronManager()
		res = obj.deactivate_cron(data['script'])

		if res:
			return {'success': res, 'message': 'Cron Deactivated Successfully'}
		else:
			return {'success': res, 'message': 'Something went wrong'}

class UpdateCron(restful.Resource):
	def post(self):
		data = request.get_json()

		obj = CronManager()
		res = obj.deactivate_cron(data['script'])
		res = obj.activate_cron(data['script'], data['rules'])
	    
		return {'success': res, 'message': 'Cron Updated Successfully', 'data': res}

##########################################################################################
# APIs
app = Flask(__name__)
api = restful.Api(app)

CORS(app, max_age=1000)

api.add_resource(SendEmail, '/send_email')
api.add_resource(GetAllCrons, '/get_all_crons')
api.add_resource(ActivateCron, '/activate_cron')
api.add_resource(DeactivateCron, '/deactivate_cron')
api.add_resource(UpdateCron, '/update_cron')
