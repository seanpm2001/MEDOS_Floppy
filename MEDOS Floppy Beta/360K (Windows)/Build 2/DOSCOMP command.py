compat1 = str
print ("Command testing")
print ("Test the MS-DOS compatibility command")
print ("Type 'DOSCOMP' to try out the command!")
print ("Warning! Commands are CaSe SeNsItIvE")
compat1 = str(input("FC:\\"))
if compat1 == ("DOSCOMP"):
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
testconfirm = int(input("Did the command info look right? type 1 to confirm, type anything else and/or press enter to quit "))
if testconfirm == 1:
    print ("Done!")
else:
    print ("Done!")
   