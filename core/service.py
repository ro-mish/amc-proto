
from core import bo
from json import dumps
from json import loads
from json import JSONDecoder
from json import JSONEncoder


# the following global dicts are going to act as temporary datastores that
# will be used to store the data.
# I will move this to a DB once I'm sure of the schema.
user_dict = {'admin':'admin', 'manager':'pass123', 'employee':'employee'}
global_dict= {}
tasks_dict = {}

def check_login_credentials(username, password):
  '''
  Checks the user credentials for login
  :return: True or False
  '''
  global user_dict
  if username not in user_dict or user_dict[username] != password:
    return False
  else:
    return True



def create_task():
  '''
  Creates tasks
  '''

