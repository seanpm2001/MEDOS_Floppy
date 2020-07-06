in1 = str
print ("Command testing")
print ("Opening command: HELP")
print ("Command type: Information display")
print ("Test the help command")
print ("Type 'help' to try out the command!")
in1 = str(input("FC://"))
if in1 == ("help"):
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
testconfirm = int(input("Did the command info look right? type 1 to confirm, type anything else and/or press enter to quit "))
if testconfirm == 1:
    print ("Done!")
else:
    print ("Done!")
    