# coding: utf-8

from pathlib import Path
import os.path
import codecs
import json

from .dataid import DataId

class Database:

   def __init__(self):
      self.employee_data = None
      self.training_data = None
      self.max_id = DataId()
      self.read_employee_data()
      self.read_training_data()

   def new_employee_entry(self, data):
      id = self.max_id.create_new_id()
      self.employee_data[str(id)] = data
      self.save_employee_data()
      return str(id)

   def new_training_entry(self, data):
      id = self.max_id.create_new_id()
      self.training_data[str(id)] = data
      self.save_training_data()
      return str(id)

   def read_employee(self, id = None):
      data = None
      if id is None:
         data = self.employee_data
      else:
         if id in self.employee_data:
               data = self.employee_data[id]
      return data

   def read_training(self, id = None):
      data = None
      if id is None:
         data = self.training_data
      else:
         if id in self.training_data:
               data = self.training_data[id]
      return data

   def update_employee_entry(self, id, data):
      status = False
      if id in self.employee_data:
         self.employee_data[id] = data
         self.save_employee_data()
         status = True
      return status

   def update_training_entry(self, id, data):
      status = False
      if id in self.training_data:
         self.training_data[id] = data
         self.save_training_data()
         status = True
      return status

   def delete_employee_entry(self, id):
      status = False
      if self.employee_data.pop(id, None) != None:
         self.save_employee_data()
         status = True
      return status

   def delete_training_entry(self, id):
      status = False
      if self.training_data.pop(id, None) != None:
         self.save_training_data()
         status = True
      return status

   def get_employee_default(self):
      return ['', '', '', '']

   def get_training_default(self):
      return ['', '', '', '', '', '']

   def read_employee_data(self):
      try:
         current_file = Path(os.path.abspath(__file__))
         mq_dir = current_file.parent.parent
         data_dir = os.path.join(mq_dir, 'data')
         fp = codecs.open(os.path.join(data_dir, 'employee.json'), 'r', 'utf-8')
      except:
         self.employee_data = {}
         self.save_employee_data()
      else:
         with fp:
            self.employee_data = json.load(fp)
      return

   def read_training_data(self):
      try:
         current_file = Path(os.path.abspath(__file__))
         mq_dir = current_file.parent.parent
         data_dir = os.path.join(mq_dir, 'data')
         fp = codecs.open(os.path.join(data_dir, 'training.json'), 'r', 'utf-8')
      except:
         self.training_data = {}
         self.save_training_data()
      else:
         with fp:
            self.training_data = json.load(fp)
      return

   def save_employee_data(self):
      current_file = Path(os.path.abspath(__file__))
      mq_dir = current_file.parent.parent
      data_dir = os.path.join(mq_dir, 'data')
      with codecs.open(os.path.join(data_dir, 'employee.json'), 'w', 'utf-8') as fp:
         json.dump(self.employee_data, fp, indent=3)

   def save_training_data(self):
      current_file = Path(os.path.abspath(__file__))
      mq_dir = current_file.parent.parent
      data_dir = os.path.join(mq_dir, 'data')
      with codecs.open(os.path.join(data_dir, 'training.json'), 'w', 'utf-8') as fp:
         json.dump(self.training_data, fp, indent=3)