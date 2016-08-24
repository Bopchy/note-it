from note_it_database import NoteItDb

s = NoteItDb()
# Instantiates 's' as an object of database class NoteItDb 

class NoteTaker(object):
	"""Class that allows you to create, view, list, search through, 
		delete and import, export as well well sync notes.
	"""
	
	def __init__(self):
		"""Creates a new table if one doesn't exist """
		s.create_table() 
		
	def create_note(self, title, note_content):
		"""Creates and saves a note """
		s.save_note(title, note_content)  
	
	def view_note(self, note_id):
		"""Retrieves and displays a note with a specific note_id"""
		return s.view(note_id)

	def list_note(self, limit):
		"""Lists the specified number of all the existing notes"""
		return s.list(limit)

	def l_next(self, start_point, step_size):
		"""Moves from one set of list results data, to the next """
		return s.list_next(start_point, step_size)

	def search_note(self, query_string, limit):
		"""Searches and lists notes that containing a particular query_string """
		return s.search(query_string, limit)

	def s_next(self, start, step):
		"""Moves from one set of search results data, to the next """
		return search_next(start, step)

	def delete_note(self, note_id):
		s.delete(note_id)

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
# a.create_note('Note 1', 'This is my first note.')

# b = NoteTaker()
# b.create_note('This is my second note.')

# e = NoteTaker()
# print e.view_note(5)

# h = NoteTaker()
# print h.create_note('Note 7', 'This is my seventh note.')

# print s.list(5)
# print s.delete(5)
print s.search ('This', 5)




