count = int
int4 = str
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
while not (count > 15):
    count += 1
    print (count)
else:
        print ("You have successfully counted to a 4 bit integer")
testconfirm = int(input("Did the setup look right? type 1 to confirm, type anything else and/or press enter to quit "))
if testconfirm == 1:
    print ("System setup successful!")
    print ("Shutting down, please wait")
else:
    print ("Shutting down")
    