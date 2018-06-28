#!/usr/bin/env python
from sys import argv
#print('in main.py')

argc = len( argv )

commands_all = { 'add'		: 'pit_add',
                 'init'     : 'pit_init',
                 'log'		: 'pit_log',
                 'status'	: 'pit_status',
				 'stash'    : 'pit_stash',
				 'rm'       : 'pit_rm',
				 'pull'     : 'pit_pull',
				 'push'     : 'pit_push'
                 }

def execute_cmd(cmdToExecute):
	"""
	if pit is invoked as:	'pit push'

	then vars are:
	cmdToExecute:	commands_all[argv[1]], therefore 'push'
	fileToImport:	'src.commands.pit_push'

	what is executed:
	exec:			'import src.commands.pit_push
	eval:			'src.commands.pit_push.pit_push()'
	"""
	fileToImport = 'src.commands.' + cmdToExecute
	print( 'in execute_cmd();   fileToImport: ' + fileToImport)
	exec( 'import ' + fileToImport )
	eval( fileToImport + '.' + cmdToExecute + '()' )

# if invoked with app name only, do nothing (maybe status then???)
if argc == 1:
	pass
# if executed with 1 arg... (e.g.: 'pit add')
elif argc >= 2:
	#and this arg is known in commands list...
	if( argv[1] in commands_all ):
		#print related text
		execute_cmd( commands_all[argv[1]] )
	else:
		print( 'no such command' )