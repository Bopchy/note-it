# def main():
"""This program is a Note taking application, known as 'Note It'.
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
"""

import sys
import cmd
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
	
	# def __init__(self):
	# 	self.prompt = "-->"
	prompt = "(NoteIt)"

	@docopt_cmd
	def do_create(self, title):
		"""Usage: create <title> <note_content> """ 
		title = arg["<title>"]
		note_content = arg["<note_content>"]
		NoteTaker().create_note(title, note_content)

	@docopt_cmd
	def do_view(self):
		"""Usage: view <note_id> """
		note_id = arg["<note_id>"]
		return NoteTaker().view_note(note_id)	
# 
	@docopt_cmd
	def do_delete(self):
		"""Usage: delete <note_id> """
		note_id = arg["<note_id>"]
		return NoteTaker().delete_note(note_id)

	@docopt_cmd
	def do_list(self):
		"""Usage: list (--limit) """
		limit = arg["(--limit)"]
		return NoteTaker().list_note(limit)

	@docopt_cmd
	def do_list_next(self):
		"""Usage: list_next <start_point> <step_size>"""
		start_point = arg["<start_point>"]
		step_size = arg["step_size"]
		return NoteTaker().l_next(start_point, step_size)

	@docopt_cmd
	def do_search(self, arg):
		"""Usage: search <query_string> (--limit) """
		query_string = arg["<query_string>"]
		limit = arg["(--limit)"]
		return NoteTaker().search_note(query_string, limit)

	@docopt_cmd
	def do_search_next(self):
		"""Usage: search_next <query_string> <start> <step> """
		query_string = arg["<query_string>"]
		start = arg["<start>"]
		step = arg["<step>"]
		return NoteTaker().s_next(query_string, start, step)

	@docopt_cmd
	def do_import(self):
		"""Usage: import <filename> """
		filename = arg["<filename>"]
		return NoteTaker().import_note(filename)

	@docopt_cmd
	def do_export(self):
		"""Usage: export <filename> """
		filename = arg["<filename>"]
		return NoteTaker().export_note(filename)

	# def do_EOF(self, line):
	# 	return True

	def do_quit(self):
		"""Usage: Quits interactive mode """
		print '****** You have left NoteIt ******'
		exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
	NoteIt().cmdloop()

print(opt)
		# def default(self, arg):
		# 	print("Exiting")

	# 
	# 	# print("Im Here!")
	# 	"""Creates note_it.db then connects to it """ 
		
	# 	try:
	# 		NoteIt().cmdloop()
	# 		# self.conn = sqlite3.connect('C:/Users/Ruth/clones/bc-9-note-it/bc-9-note-it/note_it.db')
	# 		# self.c = self.conn.cursor()
	# 	except KeyboardInterrupt:
	# 		print("Default Interrupt")
# if __name__ == '__main__':
# 	main()
	




 

