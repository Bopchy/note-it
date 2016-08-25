'''This program is a Note taking application, known as 'Note It'.
	The available commands are specified under Usage below.

	Usage:  
		note_it create <title> <note_content> 
		note_it view <note_id>
		note_it delete <note_id>
		note_it list (--limit)
		note_it list_next <start_point> <step_size>
		note_it search <query_string> (--limit)
		note_it search_next <query_string> <start> <step>
		note_it import <filename>
		note_it export <filename>
		note_it sync
		note_it -h | --help
		note_it --version
		note_it --interactive | -i
		
	Options:
		-h, --help  shows this help message and exits
		--limit		sets the number of items to display in resulting list
		-i, --interactive  interactive mode  		  
'''

import cmd 
import sys
from docopt import docopt, DocoptExit
from functions import NoteTaker


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

class NoteIt(cmd.Cmd): # Imports Cmd from cmd
	"""This is a Note Taking console application dubbed Note It """
	
	def intro():
			pass

	@docopt_cmd
	def do_create(self, title, note_content):
		"""Usage: create <title> <note_content> """ 
		return  NoteIt().create_note(title, note_content)

	@docopt_cmd
	def do_view(self, note_id):
		"""Usage: view <note_id> """
		return NoteIt().view_note(note_id)	

	@docopt_cmd
	def do_delete(self, note_id):
		"""Usage: delete <note_id> """
		return NoteIt().delete_note(note_id)

	@docopt_cmd
	def do_list(self, limit):
		"""Usage: list (--limit) """
		return NoteIt().list_note(limit)

	@docopt_cmd
	def do_list_next(self, start_point, step_size):
		"""Usage: list_next <start_point> <step_size>"""
		return NoteIt().l_next(start_point, step_size)

	@docopt_cmd
	def do_search(self, query_string, limit):
		"""Usage: search <query_string> (--limit) """
		return NoteIt().search_note(query_string, limit)

	@docopt_cmd
	def do_search_next(self, query_string, start, step):
		"""Usage: search_next <query_string> <start> <step> """
		return NoteIt().s_next(query_string, start, step)

	@docopt_cmd
	def do_import(self, filename):
		"""Usage: import <filename> """
		return NoteIt().import_note(filename)

	@docopt_cmd
	def do_export(self, filename):
		"""Usage: export <filename> """
		return NoteIt().export_note(filename)

	def do_quit(self):
		"""Quits interactive mode """
		print('You have left NoteIt')

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
	NoteIt().cmdloop

print(opt)




 

