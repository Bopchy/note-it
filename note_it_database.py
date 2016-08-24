import sqlite3

class NoteItDb():
	def __init__(self): # Initializes the class 
		# Creates note_it.db then connects to it 
		self.conn = sqlite3.connect('C:/Users/Ruth/clones/bc-9-note-it/bc-9-note-it/note_it.db')
		self.c = self.conn.cursor()
		
	def create_table(self):
		# Creates the table that notes will be stored in
		self.c.execute("CREATE TABLE if not exists note_it_data \
				(id_column INTEGER PRIMARY KEY AUTOINCREMENT, \
				title_column TEXT, \
				body_column TEXT)" \
				)
		self.conn.commit() # Commits the changes
		self.conn.close() # Closes connection to database file 
	
	def save_note(self, ):
		# Saves the note_content that has been entered to the database
		with self.conn:
			self.c.execute("INSERT INTO note_it_data\
					")