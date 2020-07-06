compat3 = str
print ("Command testing")
print ("Test the Windows 2.x compatibility command")
print ("Type '2.RUN' to try out the command!")
print ("Warning! Commands are CaSe SeNsItIvE")
compat3 = str(input("FC:\\"))
if compat3 == ("2.RUN"):
	print ("Windows 2 compatibility center")
	print ("1 Windows 2.0")
	print ("2 Windows 2.01")
	print ("3 Windows 2.02")
	print ("4 Windows 2.03")
	print ("5 Windows 2.04")
	print ("6 Windows 2.10")
	print ("7 Windows 2.11")
	print ("Choose a number 0-7 then click enter to continue compatibility testing")
	print ("Type XE to quit")
testconfirm = int(input("Did the command info look right? type 1 to confirm, type anything else and/or press enter to quit "))
if testconfirm == 1:
    print ("Done!")
else:
    print ("Done!")
   