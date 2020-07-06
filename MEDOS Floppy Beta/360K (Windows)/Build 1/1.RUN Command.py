compat2 = str
print ("Command testing")
print ("Test the Windows 1.x compatibility command")
print ("Type '1.RUN' to try out the command!")
print ("Warning! Commands are CaSe SeNsItIvE")
compat2 = str(input("FC:\\"))
if compat2 == ("1.RUN"):
	print ("Windows 1 compatibility center")	
	print ("A = Windows 1.0")
	print ("B = Windows 1.01")
	print ("C = Windows 1.02")
	print ("D = Windows 1.03")
	print ("E = Windows 1.04")
	print ("Choose a letter A-E then click enter to continue compatibility testing")
	print ("Type XE to quit")
testconfirm = int(input("Did the command info look right? type 1 to confirm, type anything else and/or press enter to quit "))
if testconfirm == 1:
    print ("Done!")
else:
    print ("Done!")
   