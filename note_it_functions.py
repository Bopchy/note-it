from note_it_database import NoteItDb



s = NoteItDb()
# Instantiates 's' as an object of database class NoteItDb 
# obj.create_table()

class NoteTaker(object):
	"""Class that allows you to create, view, list, search through, 
		delete and import, export as well well sync notes.
	"""
	_id = 0
	note = []

	def __init__(self):
		s.create_table() # Creates a new table if one doesn't exist 
		
	def create_note(self, note_content):
		# NoteTaker.note.append(note_content)
		# # Adds note to list 
		
		s.save_note(note_content)
		

def view_note(note_id):
	pass

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

d = NoteTaker()
d.create_note('This is my fourth note.')