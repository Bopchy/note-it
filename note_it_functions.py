from note_it_database import NoteItDb

s = NoteItDb()
# Instantiates 's' as an object of database class NoteItDb 

class NoteTaker(object):
	"""Class that allows you to create, view, list, search through, 
		delete and import, export as well well sync notes.
	"""
	
	def __init__(self):
		""" Creates a new table if one doesn't exist """
		s.create_table() 
		
	def create_note(self, title, note_content):
		"""Creates and saves a note """
		s.save_note(title, note_content)  
	
	def view_note(self, note_id):
		"""Retrieves and displays a note with a specific note_id"""
		note = int(note_id)
		return s.view(note_id)

	def list_note():
		pass

def search_note(query_string):
	pass

def delete_note():
	pass

def sync_note():
	pass

def import_note():
	# Imports notes from database as a JSON 
	pass

def export_note():
	# Exports notes as a JSON 
	pass

# if __name__ == '__main__':
# 	note

# a = NoteTaker()
# a.create_note('This is my first note.')

# b = NoteTaker()
# b.create_note('This is my second note.')

e = NoteTaker()
print e.view_note(5)

f = NoteTaker()
print f.view_note(7)