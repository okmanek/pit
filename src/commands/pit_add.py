print '<code for pit_add>'

#if user invoked app as: 'pit add' with no fileName
def pit_add(argc, argv):
	if argc == 2:
		print( 'needed file as an argument' )
	else:
		print( 'fileNames to be added: ' )
		#print( *argv, sep='\n' ) # python 3
		fileNames = []
		for el in argv[2:]:
			print el
			fileNames.append( el )
