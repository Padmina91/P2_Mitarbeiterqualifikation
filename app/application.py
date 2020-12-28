# coding: utf-8

import cherrypy
from .database import Database
from .view import View

class Application:

   def __init__(self):
      self.database = Database()
      self.view = View()

   @cherrypy.expose
   def index(self):
      return self.create_index()

   @cherrypy.expose
   def add(self):
      return self.create_form()

   @cherrypy.expose
   def edit(self, id):
      return self.create_form(id)

   @cherrypy.expose
   def save(self, id_param, name1, vorname1, matrnr1, semesteranzahl1, name2, vorname2, matrnr2, semesteranzahl2):
      id = id_param
      data = [name1, vorname1, matrnr1, semesteranzahl1, name2, vorname2, matrnr2, semesteranzahl2]
      if id != "None":
         self.database.update_entry(id, data)
      else:
         self.database.new_entry(data)
      raise cherrypy.HTTPRedirect('/')

   @cherrypy.expose
   def delete(self, id_param):
      id = id_param
      if id != None:
         deletion_successful = self.database.delete_entry(id)
      if deletion_successful:
         raise cherrypy.HTTPRedirect('/')
      else:
         raise cherrypy.HTTPError(500, "Diesen Eintrag gibt es nicht (mehr).")

   @cherrypy.expose
   def default(self, *arguments, **kwargs):
      msg_s = "unbekannte Anforderung: " + \
      str(arguments) + \
      ' ' + \
      str(kwargs)
      raise cherrypy.HTTPError(404, msg_s)
   default.exposed = True

   def create_index(self):
      #data = self.database.read()
      return self.view.create_list(None)

   def create_form(self, id = None):
      if id != None:
         data = self.database.read(id)
      else:
         data = self.database.get_default()
      return self.view.create_form(id, data)

   @cherrypy.expose
   def toggle_view(self):
      self.view.toggle_view()
      raise cherrypy.HTTPRedirect('/')