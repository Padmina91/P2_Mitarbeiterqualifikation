# coding: utf-8

from pathlib import Path
import os.path
import codecs
import json
import operator

from .dataid import DataId
from .validator import Validator

class Database:

   def __init__(self):
      self.validator = Validator()
      self.employee_data = None
      self.training_data = None
      self.max_id = DataId()
      self.read_employee_data()
      self.read_training_data()

# ---------------------------------------------------------------------------------------------------------------------------------

   def new_employee_entry(self, employee_data):
      id = self.max_id.create_new_id()
      self.employee_data[str(id)] = employee_data
      self.save_employee_data()
      return str(id)

   def new_training_entry(self, training_data):
      id = self.max_id.create_new_id()
      self.training_data[str(id)] = training_data
      self.save_training_data()
      return str(id)

   def read_employee(self, id = None):
      data = None
      if id is None:
         data = self.employee_data
      elif id in self.employee_data:
         data = self.employee_data[id]
      return data

   def read_training(self, id = None):
      data = None
      if id is None:
         data = self.training_data
      elif id in self.training_data:
         data = self.training_data[id]
      return data

   def update_employee_entry(self, id, employee_data):
      status = False
      if id in self.employee_data:
         self.employee_data[id] = employee_data
         self.save_employee_data()
         status = True
      return status

   def update_training_entry(self, id, training_data):
      status = False
      if id in self.training_data:
         self.training_data[id] = training_data
         self.save_training_data()
         status = True
      return status

   def save_qualification(self, id, index, bezeichnung):
      status = False
      if id != "None" and id in self.training_data and len(self.training_data[id][6]) >= int(index):
         if int(index) == len(self.training_data[id][6]):
            self.training_data[id][6].append(bezeichnung) # neue Qualifikation hinzufügen
         else:
            self.training_data[id][6][int(index)] = bezeichnung # bereits vorhandene Qualifikation updaten
         self.save_training_data()
         status = True
      return status

   def register_for_training(self, id_employee, id_training):
      status = False
      if id_employee in self.employee_data and id_training in self.training_data:
         self.employee_data[id_employee][4][id_training] = "angemeldet"
         self.save_employee_data()
         status = True
      return status

   def cancel_registration(self, id_employee, id_training):
      status = False
      if id_employee in self.employee_data and id_training in self.training_data:
         training_status = self.employee_data[id_employee][4].get(id_training, 0)
         if training_status == "angemeldet":
            self.employee_data[id_employee][4][id_training] = "storniert"
            self.save_employee_data()
         status = True
      return status

   def cancel_participation(self, id_training, id_employee):
      status = False
      if id_employee in self.employee_data and id_training in self.training_data:
         training_status = self.employee_data[id_employee][4].get(id_training, 0)
         if training_status == "angemeldet" or training_status == "nimmt teil":
            self.employee_data[id_employee][4][id_training] = "abgebrochen"
            self.save_employee_data()
      return status

   def update_participation_status(self, id_training, id_employee, new_participation_status):
      status = False
      if id_training in self.training_data and id_employee in self.employee_data:
         training_status = self.employee_data[id_employee][4].get(id_training, 0)
         if training_status != "storniert" and training_status != "abgebrochen" and training_status != new_participation_status and training_status != 0:
            self.employee_data[id_employee][4][id_training] = new_participation_status
            self.save_employee_data()
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

   def save_employee(self, id_param, name, vorname, akadGrade, taetigkeit):
      id = id_param
      data = [name, vorname, akadGrade, taetigkeit]
      if id != "None":
         data.append(self.employee_data[id][4])
         self.update_employee_entry(id, data)
      else:
         data.append({})
         self.new_employee_entry(data)

   def save_training(self, id_param, bezeichnung, von, bis, beschreibung, maxTeiln, minTeiln, qualification0, zertifikat):
      id = id_param
      data = [bezeichnung, von, bis, beschreibung, maxTeiln, minTeiln, [qualification0], [zertifikat]]
      if data[7][0] == "":
         data[7] = list()
      if id != "None":
         data[6] = self.training_data[id][6] # Qualifikationen (1 bis n)
         data[6][0] = qualification0
         self.update_training_entry(id, data)
      else:
         self.new_training_entry(data)

   def calculate_participation_training(self, id):
      data = [] # Aufbau jeweils: [id_employee, name, vorname, akad. Grade, Tätigkeit, Teilnahmestatus]
      if id in self.training_data:
         for k, v in self.employee_data.items():
            status = v[4].get(id, 0)
            if status == "angemeldet" or status == "nimmt teil" or status == "nicht erfolgreich beendet" or status == "erfolgreich beendet":
               data.append([k, v[0], v[1], v[2], v[3], status])
      return data

   def calculate_participation_employee(self, id_param):
      data = list() # [[Trainings, zu denen sich Mitarbeiter anmelden kann], [bereits gebuchte, zukünftige Trainings]], jeweils Aufbau: [id, bezeichnung, von, bis, beschreibung]
      data.append(list())
      data.append(list())
      employee_data = self.employee_data[id_param]
      training_data = self.training_data
      already_registered_trainings = list()
      today = self.validator.today
      future_trainings = list()
      for k, v in employee_data[4].items():
         if v == "angemeldet":
            already_registered_trainings.append(k)
      for k, v in training_data.items():
         start_date = self.validator.get_date(v[1])
         if start_date > today:
            future_trainings.append(k)
      for id in future_trainings:
         if id not in already_registered_trainings:
            data[0].append([id, training_data[id][0], training_data[id][1], training_data[id][2], training_data[id][3]])
         else:
            data[1].append([id, training_data[id][0], training_data[id][1], training_data[id][2], training_data[id][3]])
      return data

   def calculate_participation_trainings(self):
      data = list()
      data.append(list()) # laufende Trainings
      data.append(list()) # abgeschlossene Trainings
      today = self.validator.today
      training_data = self.training_data
      for k, v in training_data.items():
         start_date = self.validator.get_date(v[1])
         end_date = self.validator.get_date(v[2])
         if start_date < today and end_date > today:
            data[0].append([k, v[0], v[1], v[2], v[3], v[4], v[5]])
         elif end_date < today:
            data[1].append([k, v[0], v[1], v[2], v[3], v[4], v[5]])
      return data

   def calculate_evaluation_employees(self):
      data = list()
      employees_alphabetical = list()
      trainings_chronological = list()
      for v in self.employee_data.values():
         employees_alphabetical.append(v)
      employees_alphabetical.sort(key=operator.itemgetter(0))
      for k, v in self.training_data.items():
         trainings_chronological.append([k, v[0], v[1], v[2]])
      trainings_chronological.sort(key=operator.itemgetter(2))
      for employee in employees_alphabetical:
         data.append([employee[0], employee[1], employee[2], employee[3], list()])
      for i in range(len(employees_alphabetical)):
         for training in trainings_chronological:
            if training[0] in employees_alphabetical[i][4]:
               data[i][4].append([training[1], training[2], training[3], employees_alphabetical[i][4][training[0]]])
      return data

   def calculate_evaluation_trainings(self):
      trainings_alphabetical = list()
      for k, v in self.training_data.items():
         trainings_alphabetical.append([k, v[0], v[1], v[2], v[3], v[4], v[5], list()])
      trainings_alphabetical.sort(key=operator.itemgetter(1))
      for training in trainings_alphabetical:
         for employee in self.employee_data.values():
            if training[0] in employee[4] and employee[4][training[0]] == "erfolgreich beendet":
               training[7].append([employee[0], employee[1], employee[2], employee[3]])
         training[7].sort(key=operator.itemgetter(0))
      return trainings_alphabetical

   def calculate_evaluation_certificates(self):
      certificates_alphabetical = list()
      for k, v in self.training_data.items():
         if len(v[7]) == 1:
            certificates_alphabetical.append([k, v[7][0], list()])
      certificates_alphabetical.sort(key=operator.itemgetter(1))
      for i in range(len(certificates_alphabetical)):
         for employee in self.employee_data.values():
            if certificates_alphabetical[i][0] in employee[4] and employee[4][certificates_alphabetical[i][0]] == "erfolgreich beendet":
               certificates_alphabetical[i][2].append([employee[0], employee[1], employee[2], employee[3]])
         certificates_alphabetical[i][2].sort(key=operator.itemgetter(0))
      return certificates_alphabetical

   def calculate_index_data(self):
      num_of_employees = len(self.employee_data)
      trainings = self.read_training()
      num_of_trainings_in_planning = 0
      num_of_trainings_finished = 0
      num_of_trainings_currently_running = 0
      for v in trainings.values():
         start_date = self.validator.get_date(v[1])
         end_date = self.validator.get_date(v[2])
         today = self.validator.today
         if start_date > today:
            num_of_trainings_in_planning += 1
         elif end_date < today:
            num_of_trainings_finished += 1
         elif start_date < today and end_date > today:
            num_of_trainings_currently_running += 1
      data = [num_of_employees, num_of_trainings_in_planning, num_of_trainings_currently_running, num_of_trainings_finished]
      return data

   def calculate_training_data(self, id):
      training_data = self.training_data[id]
      data = [training_data[0], training_data[1], training_data[2], training_data[7], training_data[6], list()]
      for employee in self.employee_data.values():
         if id in employee[4]:
            data[5].append([employee[0], employee[1], employee[2], employee[3], employee[4][id]])
      return data

# ---------------------------------------------------------------------------------------------------------------------------------

   def get_employee_default(self):
      return ['', '', '', '']

   def get_training_default(self):
      return ['', '', '', '', '', '', [], []]

# ---------------------------------------------------------------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------------------------------------------------------------

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