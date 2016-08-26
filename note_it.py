# def main():
"""This program is a Note taking application, known as 'Note It'.
The available commands are specified under Usage below.

Usage:  
	note_it create [note]
	note_it view [note_id]
	note_it delete [note_id]
	note_it list [(--limit)]
	note_it list_next [<start_point>] [<step_size>]
	note_it search [query_string] [(--limit)]
	note_it search_next <query_string> <start> <step>
	note_it import [filename]
	note_it export [filename]
	note_it sync []
	note_it -h | --help
	note_it --version
	note_it --interactive | -i
	
Options:
	-h, --help  shows this help message and exits
	--limit		sets the number of items to display in resulting list
	-i, --interactive  interactive mode  		  
"""

import sys
import cmd
# from colorama import init
# from termcolor import cprint 
# from pyfiglet 
from docopt import docopt, DocoptExit
from note_it_functions import NoteTaker 

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

class NoteIt(cmd.Cmd): 
	"""This is a Note Taking console application dubbed Note It """
	
	def intro():
		pass

	intro = intro()
	prompt = "(NoteIt)"

	@docopt_cmd
	def do_create(self, arg):
		"""Usage: create [note] """ 
		NoteTaker().create_note(arg)

	@docopt_cmd
	def do_view(self, arg):
		"""Usage: view [note_id] """
		return NoteTaker().view_note(arg)	
 
	@docopt_cmd
	def do_delete(self, arg):
		"""Usage: delete [note_id] """
		return NoteTaker().delete_note(arg)

	@docopt_cmd
	def do_list(self, arg):
		"""Usage: list [(--limit)] """
		return NoteTaker().list_note(arg)

	@docopt_cmd
	def do_list_next(self, arg):
		"""Usage: list_next <start_point> <step_size>"""
		# start_point = arg["<start_point>"]
		# step_size = arg["step_size"]
		return NoteTaker().l_next(start_point, step_size)

	@docopt_cmd
	def do_search(self, args):
		"""Usage: search [query_string] [(--limit)] """
		return NoteTaker().search_note(args)

	@docopt_cmd
	def do_search_next(self, arg):
		"""Usage: search_next <query_string> <start> <step> """
		# query_string = arg["<query_string>"]
		# start = arg["<start>"]
		# step = arg["<step>"]
		return NoteTaker().s_next(query_string, start, step)

	@docopt_cmd
	def do_import(self, arg):
		"""Usage: import [filename] """
		NoteTaker().import_note(arg)
		print 'The file contents have been imported into the database.'

	@docopt_cmd
	def do_export(self, arg):
		"""Usage: export [filename] """
		NoteTaker().export_note(arg)
		print 'The data has been exported to a JSON file.'

	@docopt_cmd
	def do_sync(self, args):
		"""Usage: sync [] """
		NoteTaker().sync_note(args)
		print 'Firebase has been synced with your local database.'

	def do_quit(self, arg):
		"""Usage: Quits interactive mode """
		print '****** You have left NoteIt ******'
		exit()
	
# opt = docopt(__doc__, sys.argv[1:])

# if opt['--interactive']:
# 	NoteIt().cmdloop()

# print(opt)
		# def default(self, arg):
		# 	print("Exiting")

if __name__ == '__main__':
	NoteIt().cmdloop()
	




 

