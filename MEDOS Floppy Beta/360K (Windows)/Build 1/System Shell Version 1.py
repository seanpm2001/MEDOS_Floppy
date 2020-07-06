'''
floppy version edit time: August 15th 9:13 am to August 15th 11:18 am 
reason for quitting, stable state, need to edit to finalize this command correctly, minor rewrite required
'''
SESNUM = int
SESNUM = 0
print ("MEDOS Beta 1")
print ("For virtual 360 Kilobyte Floppy diskettes")
print ("Free memory: 348480 bytes")
print ("Used memory: 11520 bytes")
print ("Starting system")
print ("Reading from drivers:")
print ("MEMTYPE.PY")
print ("FFDEF.PY")
print ("SHELDEF.PY")
print ("System ready for use!")
print ("Type a command, use the 'help' command for help. Type '1' to end the session")
while (SESNUM == 0):
	INP = str(input("FC:\\"))
if (INP == "help"):
	print ("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
	print ("Help list")
	print ("Floppy 360K has a simplified command list. Versions with more memory operate differently")
	print ("For Windows Compatibility")
	print ("DOSCOMP = Test compatibility for MS-DOS operating systems from 1.0 to 3.1")
	print ("1.RUN = Test compatibility for versions of the Windows 1x product line from 1.0 to 1.04")
	print ("2.RUN = Test compatibility for versions of the Windows 2x product line from 2.0 to 2.11")
	print ("3.RUN = Test compatibility for versions of the Windows 3x product line from 3.0 to 3.2")
	print ("For user help")
	print ("Help = See help (current command listed)")
	print ("Memory testing")
	print ("4INT = Test your system via 4 bit integer counting")
	print ("8INT = Test your system via 4 bit integer counting")
	print ("=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|")
else:
	if (INP == "DOSCOMP"):
		print ("MS-DOS compatibility center")	
		print ("J MS-DOS 1.0")
		print ("K MS-DOS 1.10")
		print ("L MS-DOS 1.11")
		print ("M MS-DOS 1.14")
		print ("0 MS-DOS 1.24")
		print ("P MS-DOS 1.25")
		print ("Q MS-DOS 2.0")
		print ("R MS-DOS 2.1")
		print ("S MS-DOS 2.11")
		print ("T MS-DOS 3.0")
		print ("U MS-DOS 3.1")
		print ("Choose a letter J-U then click enter to continue compatibility testing")
		print ("Type XE to quit")
	else:
		if (INP == "INT4"):
			print ("Opening debug tool: 4 bit count")
			print ("This command tests your system to see if it can reach a 4 bit integer")
			print ("Are you ready?")
			print ("Type 'OPEN' to try out command")
			int4 = str(input("FC://"))
		if int4 == ("OPEN"):
			count = 0
			count = int
			count =+ 1
			print (count)
		while (count > 15):
			count += 1
			print (count)
		else:
			if (count == 16):
				print ("You have successfully counted to a 4 bit integer")
			else:
				if (INP == "0"):
					testconfirm = str(input("You have activated the shutdown function! Press any key to shut down"))
					if testconfirm == (testconfirm):
						print ("Shutting down")
						print ("Saving your settings")
						print ("It is now safe to turn off your virtual machine :)")
					else:
						print ("Shutting down")
						print ("Saving your settings")
						print ("It is now safe to turn off your virtual machine :)")