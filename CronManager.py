from crontab import CronTab
import itertools
from os import listdir
from os.path import isfile, join
from get_config import *

class CronManager:

	def __init__(self):

		self.type_list = ['minute', 'hour', 'dom', 'month', 'dow']

		self.venv_path = config_json['config']['cron']['venv_path']
		self.scripts_dir = config_json['config']['cron']['scripts_dir']
		self.user_name = config_json['config']['cron']['cron_user']

		self.cron_list = CronTab(user=self.user_name)
		# print(self.cron_list)
		# job = self.cron_user.new(command='echo hello_world')
		# job.minute.every(1)
		# self.cron_user.write()


	def get_all_crons(self):
		scripts_list = [{'script': f} for f in listdir(self.scripts_dir) if isfile(join(self.scripts_dir, f))]
		types = self.type_list

		for script in scripts_list:
			script['rules'] = None
			for item in self.cron_list:
				if item.comment == script['script']:
					rule = {}
					for key in types:
						k = str(item.__getattribute__(key))
						_type, _val = self.get_type_val(k)
						rule[key] = {'type': _type, 'value': _val}
					script['rules'] = rule
					break

		return scripts_list


	def activate_cron(self, script, rules):
		command = self.venv_path+' '+self.scripts_dir+script
		job  = self.cron_list.new(command=command, comment=script)

		types = self.type_list

		for key in types:
			if rules[key]['type'] != None:
				if rules[key]['type'] == 'every':
					job.__getattribute__(key).every(rules[key]['value'])
				elif rules[key]['type'] == 'on':
					job.__getattribute__(key).on(rules[key]['value'])
			else:
				job.every(1).__getattribute__(key)

		self.cron_list.write()

		return True


	def deactivate_cron(self, script):

		self.cron_list.remove_all(comment=script)
		self.cron_list.write()
		return True


	def get_type_val(self, k):
		if "*/" in k:
			_type = 'every'
			_val = k[2:]
		elif "*" in k:
			_type = None
			_val = '1'
		else:
			_type = 'on'
			_val = k

		return _type,_val

	def clear_all(self):
		self.cron_list.remove_all()
		self.cron_list.write()


if __name__ == "__main__":
    # obj = CronManager()

    # obj.activate_cron('test1.py',{
    # 	"minute": {"type": None, "value": "54"}, 
    # 	"hour": {"type": None, "value": "2"}, 
    # 	"dom": {"type": None, "value": "3"}, 
    # 	"month": {"type": None, "value": "4"}, 
    # 	"dow": {"type": None, "value": "5"}
    # 	})

    # obj.deactivate_cron("test1.py")

    # print(obj.get_all_crons())
    
    # obj.clear_all()

    pass