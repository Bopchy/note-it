import sqlite3
 

class NoteItDb():
	'''Class that creates table and handles database queries'''
	
	def __init__(self): # Initializes the class 
		# Creates note_it.db then connects to it 
		self.conn = sqlite3.connect('C:/Users/Ruth/clones/bc-9-note-it/bc-9-note-it/note_it.db')
		self.c = self.conn.cursor()

	def create_table(self):
		# Creates the table that notes will be stored in
		self.c.execute("CREATE TABLE if not exists note_it_data \
				(id_column INTEGER PRIMARY KEY AUTOINCREMENT, \
				title_column CHAR(50), \
				body_column TEXT)" \
				)
		self.conn.commit() # Commits the changes
	
	def save_note(self, title, note_content):
		# Saves the note_content that has been entered to the database
		with self.conn:
			self.c.execute("INSERT INTO note_it_data(title_column, body_column) \
				VALUES ('{}', '{}')".format(title, note_content))
			# {} is a place holder for note_content

	def view(self, note_id):
		# Allows you to view a note with a particular note_id 
		with self.conn:
			for item in self.c.execute("SELECT * FROM note_it_data WHERE \
				id_column == '{}'".format(note_id)):
				return item

	def search():
		# Retrieves a list of all the notes with a particuler query string  
		pass

	def list(self):
		# Retrieves a list of all the notes taken 
		return self.c.execute("SELECT * FROM note_it_data")

	def delete():
		# Deletes a note with a particular note_id from database 
		pass

	def sync():
		# Syncs notes with Firebase
		pass

# self.conn.close() # Closes connection to database file 
