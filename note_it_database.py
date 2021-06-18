import sqlite3
import json
import collections
from termcolor import colored
from firebase import firebase

firebase = firebase.FirebaseApplication('https://note-95345.firebaseio.com/', None)  

class NoteItDb():
	"""Class that creates table and handles database queries"""
	def __init__(self): # Initializes the class 
		"""Creates note_it.db then connects to it """ 
		self.conn = sqlite3.connect('C:/Users/Ruth/clones/bc-9-note-it/bc-9-note-it/note_it.db')
		self.c = self.conn.cursor()

	def create_table(self):
		"""Creates the table that notes will be stored in """
		self.c.execute("CREATE TABLE if not exists note_it_data \
				(id_column INTEGER PRIMARY KEY AUTOINCREMENT, \
				title_column CHAR(50), \
				body_column TEXT)" \
				)
		self.conn.commit() # Commits the changes

	def save_note(self, title, note_content):
		"""Saves the note_content that has been entered to the database """
		with self.conn:
			self.c.execute("INSERT INTO note_it_data(title_column, body_column) \
				VALUES ('%s','%s')" % (title, note_content))
			# {} is a place holder for note_content

	def view(self, note_id):
		"""Allows you to view a note with a particular note_id """ 
		with self.conn:
			self.c.execute("SELECT * FROM note_it_data WHERE \
				id_column == ('%i')" % (note_id))
			for item in self.c.fetchall():
				return colored('{0} : {1} --> {2}'.format(item[0], item[1], item[2]), green)

	def search(self, query_string, limit):
		"""Retrieves a list of all the notes with a particuler query string, where
			the limit specifies the maximum number of notes that can be listed  
		"""  
		with self.conn:
			self.c.execute("SELECT * FROM note_it_data WHERE body_column LIKE \
				'%{}%' LIMIT '{}'".format(query_string, int(limit)))
			for item in self.c.fetchall():
				print colored('{0} : {1} --> {2}'.format(item[0], item[1], item[2], \
					ensure_ascii=False), 'green')

	def search_next(self, query_string, start, step):
		""""Invokes the next set of data in the running query """
		with self.conn:
			self.c.execute("SELECT * FROM note_it_data WHERE body_column LIKE '%{}%' \
				LIMIT '{}', '{}'".format(query_string, int(start), int(step))) 
			for item in self.c.fetchall():
				return item
				
	def list_(self, limit):
		"""Retrieves a list of all the notes taken, where the limit specifies the 
			maximum number of notes that can be listed
		""" 
		with self.conn:
			self.c.execute("SELECT * FROM note_it_data LIMIT'{}'".format (int(limit)))
			for item in self.c.fetchall():
				print colored('{0} : {1} --> {2}'.format(item[0], item[1], item[2], \
					ensure_ascii=False), 'green')

	def list_next(self, start_point, step_size):
	 	"""Invokes the next set of data in the running query"""
	 	with self.conn:
	 		self.c.execute("SELECT * FROM note_it_data LIMIT '{}' \
	 			'{}'".format(start_point, step_size))
	 		# step_size specifes by how the next item to be shown increases   

	def delete(self, note_id):
		"""Deletes a note with a particular note_id from database """ 
		with self.conn:
			self.c.execute("DELETE FROM note_it_data WHERE \
				id_column == '%i'" % (note_id))

	def exp(self, filename):
		"""Exports entire database content to a JSON file, and saves it using  
			a JSON format 
		"""
		rows = None
		with self.conn:
			self.c.execute("SELECT * from note_it_data")
			rows = self.c.fetchall()
			# rows now contains all the results of the query   
		json1 = json.dumps(rows, ensure_ascii=False)
		# Converts rows to JSON, eliminating the ascii's
		json_file = str(filename)
		# json_file is the file the JSON of the database will be exported to.
		b = open(json_file, 'wb') 
		# Creates file with specified name, then adds the JSON to it. 
		b.write(json1)
		b.close()
		self.c.close()

	def imp(self, filename):
		"""Imports JSON file such that, you can populate database through \
			the respective file
		"""
		json_file = str(filename)
		_load =  json.load(open(json_file, 'r+'))
		for item in _load:
			with self.conn:
				self.c.execute("INSERT INTO note_it_data (title_column, \
					body_column) VALUES (?,?)",(item[1], item[2]))

	def sync(self):
		"""Syncs notes in the local database with Firebase """
		with self.conn:
			self.c.execute("SELECT * FROM note_it_data")
			for items in self.c.fetchall():
				firebase.post('note_it_data', items) 
				print colored("sdf",'red')
				

			


