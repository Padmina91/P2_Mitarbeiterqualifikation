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
      self.read_view_file()

   def create_list(self, data_param):
      self.read_view_file()
      tpl_file = self.view_style + '.tpl'
      template = self.lookup.get_template(tpl_file)
      markup = template.render(data = data_param)
      return markup

   def create_form(self, id, data_param):
      template = self.lookup.get_template('form.tpl')
      markup = template.render(data = data_param, key = id)
      return markup

   def read_view_file(self):
      try:
         fp = codecs.open(os.path.join(self.data_dir, "view_file.json"), 'r', 'utf-8')
      except:
         self.view_style = "list"
         self.safe_view_file()
      else:
         with fp:
            self.view_style = json.load(fp)
      return

   def toggle_view(self):
      if self.view_style == "list":
         self.view_style = "list2"
      else:
         self.view_style = "list"
      self.safe_view_file()

   def safe_view_file(self):
      with codecs.open(os.path.join(self.data_dir, "view_file.json"), "w", "utf-8") as fp:
         json.dump(self.view_style, fp)