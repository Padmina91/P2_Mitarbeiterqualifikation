# coding: utf-8

from pathlib import Path
import os.path
import codecs
import json

from . import dataid

class Database:

   def __init__(self):
      self.data = None
      self.max_id = dataid.DataId()
      self.read_data()

   def new_entry(self, data):
      id = self.max_id.create_new_id()
      self.data[str(id)] = data
      self.save_data()
      return str(id)

   def read(self, id = None):
      data = None
      if id is None:
         data = self.data
      else:
         if id in self.data:
               data = self.data[id]
      return data

   def update_entry(self, id, data):
      status = False
      if id in self.data:
         self.data[id] = data
         self.save_data()
         status = True
      return status

   def delete_entry(self, id):
      status = False
      if self.data.pop(id, None) != None:
         self.save_data()
         status = True
      return status

   def get_default(self):
      return ['', '', '', '', '', '', '', '']

   def read_data(self):
      try:
         current_file = Path(os.path.abspath(__file__))
         webteams_dir = current_file.parent.parent
         data_dir = os.path.join(webteams_dir, 'data')
         fp = codecs.open(os.path.join(data_dir, 'webteams.json'), 'r', 'utf-8')
      except:
         self.data = {}
         self.save_data()
      else:
         with fp:
            self.data = json.load(fp)
      return

   def save_data(self):
      current_file = Path(os.path.abspath(__file__))
      webteams_dir = current_file.parent.parent
      data_dir = os.path.join(webteams_dir, 'data')
      with codecs.open(os.path.join(data_dir, 'webteams.json'), 'w', 'utf-8') as fp:
         json.dump(self.data, fp, indent=3)