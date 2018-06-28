#!/usr/bin/env python
import sys

#print('in main.py')

commands_all = { 'add' : 'pit_add',
                 'log' : 'pit_log',
                 'status' : 'pit_status' }



def pit_add():
	print '<code for pit add>'

def pit_log():
	print '<code for pit log>'

def pit_status():
	print '<code for pit status>'

def execute_cmd(cmdToExecute):
	#print( 'in execute!')
	print( 'In execute_cmd();   command to execute: ' + cmdToExecute )
	cmdToExecute += '()'
	eval( cmdToExecute )

# if invoked with app name only, do nothing
if len( sys.argv ) == 1:
	pass
# if executed with 1 arg... (e.g.: 'pit add')
elif len( sys.argv ) == 2:
	#and this arg is known in commands list...
	if( sys.argv[1] in commands_all ):
		#print related text
		execute_cmd( commands_all[sys.argv[1]] )
	else:
		print( 'no such command' )