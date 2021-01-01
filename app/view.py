# coding: utf-8

import codecs
from pathlib import Path
import os.path
import json

from mako.template import Template
from mako.lookup import TemplateLookup

class View:

   def __init__(self):
      self.lookup = TemplateLookup('./templates')
      self.data_dir = os.path.join(Path(os.path.abspath(__file__)).parent.parent, 'data')

   def create_tpl(self, tpl_name = 'index', id = None, data_param = None, employee_data_param = None, training_data_param = None, index = None):
      tpl_file = tpl_name + '.tpl'
      template = self.lookup.get_template(tpl_file)
      markup = template.render(key = id, data = data_param, employee_data = employee_data_param, training_data = training_data_param, index = index)
      return markup

   def create_index(self, data_param):
      return self.create_tpl(data_param = data_param)

   def create_list_employees(self, employee_data_param):
      tpl_name = 'list_employees'
      return self.create_tpl(tpl_name = tpl_name, employee_data_param = employee_data_param)

   def create_list_trainings(self, training_data_param):
      tpl_name = 'list_trainings'
      return self.create_tpl(tpl_name = tpl_name, training_data_param = training_data_param)

   def create_employee_form(self, id, employee_data_param):
      tpl_name = 'form_employee'
      return self.create_tpl(tpl_name = tpl_name, id = id, employee_data_param = employee_data_param)

   def create_training_form(self, id, training_data_param):
      tpl_name = 'form_training'
      return self.create_tpl(tpl_name = tpl_name, id = id, training_data_param = training_data_param)

   def create_show_employee(self, id, employee_data_param, training_data_param):
      tpl_name = 'show_employee'
      return self.create_tpl(tpl_name = tpl_name, id = id, employee_data_param = employee_data_param, training_data_param = training_data_param)

   def create_show_training(self, id, training_data_param):
      tpl_name = 'show_training'
      return self.create_tpl(tpl_name = tpl_name, id = id, training_data_param = training_data_param)

   def create_edit_qualification(self, id, index):
      tpl_name = "form_qualification"
      return self.create_tpl(tpl_name, id = id, index = index)