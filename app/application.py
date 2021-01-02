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
   def save_training(self, id_param, bezeichnung, von, bis, beschreibung, maxTeiln, minTeiln, qualification0, zertifikat):
      if self.is_date_correct(von, bis):
         id = id_param
         data = [bezeichnung, von, bis, beschreibung, maxTeiln, minTeiln, [qualification0], [zertifikat]]
         if id != "None":
            data[6] = self.database.training_data[id][6] # Qualifikationen (1 bis n)
            data[6][0] = qualification0
            self.database.update_training_entry(id, data)
         else:
            self.database.new_training_entry(data)
      raise cherrypy.HTTPRedirect('/list_trainings')

   @cherrypy.expose
   def save_qualification(self, id_param, index, bezeichnung):
      id = id_param
      if id != "None" and id in self.database.training_data and len(self.database.training_data[id][6]) >= int(index):
         self.database.save_qualification(id, index, bezeichnung)
         raise cherrypy.HTTPRedirect('/edit_training/' + id_param)
      else:
         raise cherrypy.HTTPError(500, "Es wurde keine valide Weiterbildung ausgewählt.")

   @cherrypy.expose
   def add_qualification(self, id_param = None):
      id = id_param
      if id != "None" and id in self.database.training_data:
         training_data = self.database.training_data[id]
         new_index = len(training_data[6])
         return self.create_edit_qualification(id, new_index, training_data)
      else:
         raise cherrypy.HTTPError(500, "Es wurde keine valide Weiterbildung ausgewählt.")

   @cherrypy.expose
   def edit_qualification(self, id_param = None, index = None):
      id = id_param
      if id != "None" and index != "None" and id in self.database.training_data and len(self.database.training_data[id][6]) > int(index):
         training_data = self.database.training_data[id]
         return self.create_edit_qualification(id, index, training_data)
      else:
         raise cherrypy.HTTPError(500, "Diesen Eintrag gibt es nicht (mehr).")

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
         return self.create_show_employee(id)
      else:
         raise cherrypy.HTTPError(500, "Diesen Eintrag gibt es nicht (mehr).")

   @cherrypy.expose
   def show_training(self, id):
      if id in self.database.training_data:
         return self.create_show_training(id)
      else:
         raise cherrypy.HTTPError(500, "Diesen Eintrag gibt es nicht (mehr).")

   @cherrypy.expose
   def participation_employees(self):
      employee_data = self.database.employee_data
      return self.view.show_participation_employees(employee_data)

   @cherrypy.expose
   def participation_employee(self, id):
      if id in self.database.employee_data:
         employee_data = self.database.employee_data[id]
         data = self.calculate_participation_employee(id)
         return self.view.show_participation_employee(id, employee_data, data)
      else:
         raise cherrypy.HTTPError(500, "Diesen Eintrag gibt es nicht (mehr).")

   @cherrypy.expose
   def register_for_training(self, id_employee, id_training):
      self.database.register_for_training(id_employee, id_training)
      raise cherrypy.HTTPRedirect('/participation_employee/' + id_employee)

   @cherrypy.expose
   def cancel_registration(self, id_employee, id_training):
      self.database.cancel_registration(id_employee, id_training)
      raise cherrypy.HTTPRedirect('/participation_employee/' + id_employee)

   @cherrypy.expose
   def participation_trainings(self):
      data = self.calculate_participation_trainings()
      return self.view.show_participation_trainings(data)

   @cherrypy.expose
   def participation_training(self, id):
      if id in self.database.training_data:
         data = self.calculate_participation_training(id)
         training_data = self.database.training_data[id]
         start_date = self.get_date(training_data[1])
         end_date = self.get_date(training_data[2])
         today = datetime.datetime.now()
         if start_date < today and end_date > today:
            return self.view.show_participation_training_current(id, training_data, data)
         elif end_date < today:
            return self.view.show_participation_training_finished(id, training_data, data)

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
         start_date = self.get_date(v[1])
         end_date = self.get_date(v[2])
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
      employee_data = self.database.employee_data[id]
      training_data = self.database.training_data
      return self.view.create_show_employee(id, employee_data, training_data)

   def create_show_training(self, id):
      data = self.database.training_data[id]
      return self.view.create_show_training(id, data)

   def create_edit_qualification(self, id, index, training_data):
      return self.view.create_edit_qualification(id, index, training_data)

   def is_date_correct(self, von, bis):
      start_date = self.get_date(von)
      end_date = self.get_date(bis)
      return end_date > start_date

   def calculate_participation_employee(self, id_param):
      data = [] # [[Trainings, zu denen sich Mitarbeiter anmelden kann], [bereits gebuchte, zukünftige Trainings]], jeweils Aufbau: [id, bezeichnung, von, bis, beschreibung]
      data.append([])
      data.append([])
      employee_data = self.database.employee_data[id_param]
      training_data = self.database.training_data
      already_registered_trainings = []
      today = datetime.datetime.now()
      future_trainings = []
      for k, v in employee_data[4].items():
         if v == "angemeldet":
            already_registered_trainings.append(k)
      for k, v in training_data.items():
         start_date = self.get_date(v[1])
         if start_date > today:
            future_trainings.append(k)
      for id in future_trainings:
         if id not in already_registered_trainings:
            data[0].append([id, training_data[id][0], training_data[id][1], training_data[id][2], training_data[id][3]])
         else:
            data[1].append([id, training_data[id][0], training_data[id][1], training_data[id][2], training_data[id][3]])
      return data

   def calculate_participation_trainings(self):
      data = []
      data.append([]) # laufende Trainings
      data.append([]) # abgeschlossene Trainings
      today = datetime.datetime.now()
      training_data = self.database.training_data
      for k, v in training_data.items():
         start_date = self.get_date(v[1])
         end_date = self.get_date(v[2])
         if start_date < today and end_date > today:
            data[0].append([k, v[0], v[1], v[2], v[3], v[4], v[5]])
         elif end_date < today:
            data[1].append([k, v[0], v[1], v[2], v[3], v[4], v[5]])
      return data

   def calculate_participation_training(self, id):
      data = [] # Aufbau jeweils: [id_employee, name, vorname, akad. Grade, Tätigkeit, Teilnahmestatus]
      if id in self.database.training_data:
         for k, v in self.database.employee_data:
            if id in v[4] and v[4][id] == "angemeldet" or v[4][id] == "nimmt teil" or v[4][id] == "nicht erfolgreich beendet" or v[4][id] == "erfolgreich beendet":
               data.append([k, v[0], v[1], v[2], v[3], v[4][id]])
      return data

   def get_date(self, date):
      return datetime.datetime(int(date[:4]), int(date[5:7]), int(date[8:10]))