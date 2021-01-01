# coding: utf-8

import cherrypy
import datetime
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
   def list_employees(self):
      return self.create_list_employees()

   @cherrypy.expose
   def list_trainings(self):
      return self.create_list_trainings()
   
   @cherrypy.expose
   def add_employee(self):
      return self.create_epmloyee_form()

   @cherrypy.expose
   def add_training(self):
      return self.create_training_form()

   @cherrypy.expose
   def edit_employee(self, id):
      return self.create_epmloyee_form(id)

   @cherrypy.expose
   def edit_training(self, id):
      return self.create_training_form(id)

   @cherrypy.expose
   def save_employee(self, id_param, name, vorname, akadGrade, taetigkeit):
      id = id_param
      data = [name, vorname, akadGrade, taetigkeit]
      if id != "None":
         data.append(self.database.employee_data[id][4])
         self.database.update_employee_entry(id, data)
      else:
         data.append({})
         self.database.new_employee_entry(data)
      raise cherrypy.HTTPRedirect('/list_employees')

   @cherrypy.expose
   def save_training(self, id_param, bezeichnung, von, bis, beschreibung, maxTeiln, minTeiln):
      if self.is_date_correct(von, bis):
         id = id_param
         data = [bezeichnung, von, bis, beschreibung, maxTeiln, minTeiln]
         if id != "None":
            data.append(self.database.training_data[id][6])
            data.append(self.database.training_data[id][7])
            self.database.update_training_entry(id, data)
         else:
            data.append({"Qualifikation": []})
            data.append({"Zertifikat": []})
            self.database.new_training_entry(data)
      raise cherrypy.HTTPRedirect('/list_trainings')

   @cherrypy.expose
   def delete_employee(self, id_param):
      id = id_param
      if id != None:
         deletion_successful = self.database.delete_employee_entry(id)
      if deletion_successful:
         raise cherrypy.HTTPRedirect('/list_employees')
      else:
         raise cherrypy.HTTPError(500, "Diesen Eintrag gibt es nicht (mehr).")

   @cherrypy.expose
   def delete_training(self, id_param):
      id = id_param
      if id != None:
         deletion_successful = self.database.delete_training_entry(id)
      if deletion_successful:
         raise cherrypy.HTTPRedirect('/list_trainings')
      else:
         raise cherrypy.HTTPError(500, "Diesen Eintrag gibt es nicht (mehr).")

   @cherrypy.expose
   def show_employee(self, id):
      if id in self.database.employee_data:
         self.create_show_employee(id)
      else:
         raise cherrypy.HTTPError(500, "Diesen Eintrag gibt es nicht (mehr).")

   @cherrypy.expose
   def show_training(self, id):
      if id in self.database.training_data:
         self.create_show_training(id)
      else:
         raise cherrypy.HTTPError(500, "Diesen Eintrag gibt es nicht (mehr).")

   @cherrypy.expose
   def default(self, *arguments, **kwargs):
      msg_s = "unbekannte Anforderung: " + str(arguments) + ' ' + str(kwargs)
      raise cherrypy.HTTPError(404, msg_s)
   default.exposed = True

   def create_index(self):
      num_of_employees = len(self.database.read_employee())
      trainings = self.database.read_training()
      num_of_trainings_in_planning = 0
      num_of_trainings_finished = 0
      num_of_trainings_currently_running = 0
      for v in trainings.values():
         start_date = datetime.datetime(int(v[1][:4]), int(v[1][5:7]), int(v[1][8:10]))
         end_date = datetime.datetime(int(v[2][:4]), int(v[2][5:7]), int(v[2][8:10]))
         today = datetime.datetime.now()
         if start_date > today:
            num_of_trainings_in_planning += 1
         elif end_date < today:
            num_of_trainings_finished += 1
         elif start_date < today and end_date > today:
            num_of_trainings_currently_running += 1
         else:
            print("Fehler. Das End-Datum liegt vor dem Startdatum...")
      data = [num_of_employees, num_of_trainings_in_planning, num_of_trainings_currently_running, num_of_trainings_finished]
      return self.view.create_index(data)

   @cherrypy.expose
   def create_list_employees(self):
      data = self.database.read_employee()
      return self.view.create_list_employees(data)

   @cherrypy.expose
   def create_list_trainings(self):
      data = self.database.read_training()
      return self.view.create_list_trainings(data)

   def create_epmloyee_form(self, id = None):
      if id != None:
         data = self.database.read_employee(id)
      else:
         data = self.database.get_employee_default()
      return self.view.create_employee_form(id, data)

   def create_training_form(self, id = None):
      if id != None:
         data = self.database.read_training(id)
      else:
         data = self.database.get_training_default()
      return self.view.create_training_form(id, data)

   def create_show_employee(self, id):
      return self.view.create_show_employee(id)

   def create_show_training(self, id):
      return self.view.create_show_training(id)

   def is_date_correct(self, von, bis):
      start_date = datetime.datetime(int(von[:4]), int(von[5:7]), int(von[8:10]))
      end_date = datetime.datetime(int(bis[:4]), int(bis[5:7]), int(bis[8:10]))
      return end_date > start_date