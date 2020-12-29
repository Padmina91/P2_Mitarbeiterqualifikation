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

   def create_index(self, data_param):
      tpl_file = 'index.tpl'
      template = self.lookup.get_template(tpl_file)
      markup = template.render(data = data_param)
      return markup

   def create_list_employees(self):
      template = self.lookup.get_template('list_employees.tpl')
      markup = template.render()
      return markup

   def create_list_trainings(self):
      template = self.lookup.get_template('list_trainings.tpl')
      markup = template.render()
      return markup

   def create_employee_form(self, id, data_param):
      template = self.lookup.get_template('employee_form.tpl')
      markup = template.render(data = data_param, key = id)
      return markup

   def create_training_form(self, id, data_param):
      template = self.lookup.get_template('training_form.tpl')
      markup = template.render(data = data_param, key = id)
      return markup