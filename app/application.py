# coding: utf-8

import cherrypy
import datetime

from .database import Database
from .view import View
from .validator import Validator

class Application:

   def __init__(self):
      self.database = Database()
      self.view = View()
      self.validator = Validator()

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
      self.database.save_employee(id_param, name, vorname, akadGrade, taetigkeit)
      raise cherrypy.HTTPRedirect('/list_employees')

   @cherrypy.expose
   def save_training(self, id_param, bezeichnung, von, bis, beschreibung, maxTeiln, minTeiln, qualification0, zertifikat):
      date_correct = self.validator.is_date_correct(von, bis)
      num_participants_correct = self.validator.is_num_participants_correct(minTeiln, maxTeiln)
      if date_correct and num_participants_correct:
         self.database.save_training(id_param, bezeichnung, von, bis, beschreibung, maxTeiln, minTeiln, qualification0, zertifikat)
         raise cherrypy.HTTPRedirect('/list_trainings')
      elif not date_correct:
         raise cherrypy.HTTPError(500, "Das Datum \"Bis\" darf nicht vor dem Datum \"Von\" liegen.")
      else:
         raise cherrypy.HTTPError(500, "Die maximale Teilnehmeranzahl darf nicht geringer als die minimale Teilnehmeranzahl sein. Außerdem dürfen beide Werte nicht 0 oder kleiner sein.")

   @cherrypy.expose
   def save_qualification(self, id_param, index, bezeichnung):
      if self.database.save_qualification(id_param, index, bezeichnung):
         raise cherrypy.HTTPRedirect('/edit_training/' + id_param)
      else:
         raise cherrypy.HTTPError(500, "Es wurde keine valide Weiterbildung ausgewählt.")

   @cherrypy.expose
   def add_qualification(self, id_param = None):
      id = id_param
      if id != "None" and id in self.database.training_data:
         training_data = self.database.training_data[id]
         new_index = len(training_data[6])
         return self.view.create_edit_qualification(id, new_index, training_data)
      else:
         raise cherrypy.HTTPError(500, "Es wurde keine valide Weiterbildung ausgewählt.")

   @cherrypy.expose
   def edit_qualification(self, id_param = None, index = None):
      id = id_param
      if id != "None" and index != "None" and id in self.database.training_data and len(self.database.training_data[id][6]) > int(index):
         training_data = self.database.training_data[id]
         return self.view.create_edit_qualification(id, index, training_data)
      else:
         raise cherrypy.HTTPError(500, "Diesen Eintrag gibt es nicht (mehr).")

   @cherrypy.expose
   def delete_employee(self, id_param):
      if self.database.delete_employee_entry(id_param):
         raise cherrypy.HTTPRedirect('/list_employees')
      else:
         raise cherrypy.HTTPError(500, "Diesen Eintrag gibt es nicht (mehr).")

   @cherrypy.expose
   def delete_training(self, id_param):
      if self.database.delete_training_entry(id_param):
         raise cherrypy.HTTPRedirect('/list_trainings')
      else:
         raise cherrypy.HTTPError(500, "Diesen Eintrag gibt es nicht (mehr).")

   @cherrypy.expose
   def show_employee(self, id):
      if id in self.database.employee_data:
         employee_data = self.database.employee_data[id]
         training_data = self.database.training_data
         return self.view.create_show_employee(id, employee_data, training_data)
      else:
         raise cherrypy.HTTPError(500, "Diesen Eintrag gibt es nicht (mehr).")

   @cherrypy.expose
   def show_training(self, id):
      if id in self.database.training_data:
         data = self.database.calculate_training_data(id)
         return self.view.create_show_training(id, data)
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
         data = self.database.calculate_participation_employee(id)
         return self.view.show_participation_employee(id, employee_data, data)
      else:
         raise cherrypy.HTTPError(500, "Diesen Eintrag gibt es nicht (mehr).")

   @cherrypy.expose
   def register_for_training(self, id_employee, id_training):
      if self.database.register_for_training(id_employee, id_training):
         raise cherrypy.HTTPRedirect('/participation_employee/' + id_employee)
      else:
         raise cherrypy.HTTPError(500, "Die Anmeldung hat nicht geklappt.")

   @cherrypy.expose
   def cancel_registration(self, id_employee, id_training):
      if self.database.cancel_registration(id_employee, id_training):
         raise cherrypy.HTTPRedirect('/participation_employee/' + id_employee)
      else:
         raise cherrypy.HTTPError(500, "Die Stornierung hat nicht geklappt.")

   @cherrypy.expose
   def participation_trainings(self):
      data = self.database.calculate_participation_trainings()
      return self.view.show_participation_trainings(data)

   @cherrypy.expose
   def participation_training(self, id_training):
      if id_training in self.database.training_data:
         data = self.database.calculate_participation_training(id_training)
         training_data = self.database.training_data[id_training]
         date_from = training_data[1]
         date_until = training_data[2]
         if self.validator.is_training_currently_running(date_from, date_until):
            return self.view.show_participation_training_current(id_training, training_data, data)
         elif self.validator.is_training_finished(date_until):
            return self.view.show_participation_training_finished(id_training, training_data, data)

   @cherrypy.expose
   def cancel_participation(self, id_training, id_employee):
      if self.database.cancel_participation(id_training, id_employee):
         raise cherrypy.HTTPRedirect('/participation_training/' + id_training)
      else:
         raise cherrypy.HTTPError(500, "Die Weiterbildung konnte nicht abgebrochen werden.")

   @cherrypy.expose
   def participation_success(self, id_training, id_employee):
      if self.database.update_participation_status(id_training, id_employee, "erfolgreich beendet"):
         raise cherrypy.HTTPRedirect('/participation_training/' + id_training)
      else:
         raise cherrypy.HTTPError(500, "Der Status konnte nicht aktualisiert werden.")

   @cherrypy.expose
   def participation_failure(self, id_training, id_employee):
      if self.database.update_participation_status(id_training, id_employee, "nicht erfolgreich beendet"):
         raise cherrypy.HTTPRedirect('/participation_training/' + id_training)
      else:
         raise cherrypy.HTTPError(500, "Der Status konnte nicht aktualisiert werden.")

   @cherrypy.expose
   def evaluation_employees(self):
      data = self.database.calculate_evaluation_employees()
      return self.view.show_evaluation_employees(data)

   @cherrypy.expose
   def evaluation_trainings(self):
      data = self.database.calculate_evaluation_trainings()
      return self.view.show_evaluation_trainings(data)

   @cherrypy.expose
   def evaluation_certificates(self):
      data = self.database.calculate_evaluation_certificates()
      return self.view.show_evaluation_certificates(data)

   @cherrypy.expose
   def default(self, *arguments, **kwargs):
      msg_s = "unbekannte Anforderung: " + str(arguments) + ' ' + str(kwargs)
      raise cherrypy.HTTPError(404, msg_s)
   default.exposed = True

   def create_index(self):
      data = self.database.calculate_index_data()
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