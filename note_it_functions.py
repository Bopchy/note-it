from note_it_database import NoteItDb

s = NoteItDb()
# Instantiates 's' as an object of database class NoteItDb 

class NoteTaker(object):
	"""Class that allows you to create, view, list, search through, 
		delete and import, export as well as sync notes.
	"""
	
	def __init__(self):
		"""Creates a new table if one doesn't exist """
		s.create_table() 
	
	def create_note(self, args):
		"""Creates and saves a note """
		title = raw_input('RE:')
		note_content = raw_input(':-')
		s.save_note(title, note_content)
		print 'Your note has been saved.'  

	def view_note(self, note_id):
		"""Retrieves and displays a note with a specific note_id"""
		note_id = int(raw_input('Enter note ID:'))
		print s.view(note_id)

	def list_note(self, limit):
		"""Lists the specified number of all the existing notes"""
		return s.list_(limit)

	def l_next(self, start_point, step_size):
		"""Moves from one set of list results data, to the next """
		return s.list_next(start_point, step_size)

	def search_note(self, args):
		"""Searches and lists notes that containing a particular query_string """
		query_string = raw_input('For which words?')
		limit = raw_input('Show how many at once?')
		return s.search(query_string, limit)

	def s_next(self, query_string, start, step):
		"""Moves from one set of search results data, to the next """
		return s.search_next(query_string, start, step)

	def delete_note(self, note_id):
		"""Deletes note with a particular note_id """
		note_id = int(raw_input('Enter note ID:'))
		s.delete(note_id)
		print 'The note has been deleted'

	def import_note(self, filename):
		"""Imports notes from database as a JSON file """ 
		return s.imp(filename)

	def export_note(self, filename):
		"""Exports notes as a JSON """ 
		return s.exp(filename)







