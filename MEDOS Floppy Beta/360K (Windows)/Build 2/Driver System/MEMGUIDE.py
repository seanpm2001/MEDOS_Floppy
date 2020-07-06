byte = int
bit1 = int
bit2 = int
bit3 = int
bit4 = int
bit5 = int
bit6 = int
bit7 = int
bit8 = int
bit1 = 0
bit2 = 0
bit3 = 0
bit4 = 0
bit5 = 0
bit6 = 1
bit7 = 0
bit8 = 0
byte = (bit1 + bit2 + bit3 + bit4 + bit5 + bit6 + bit7 + bit8)
kilobyte = int
kilobyte = (byte * 1000)
sysmem = int
sysmem = (kilobyte * 360)
'''
print (byte)
print (kilobyte)
print (sysmem)
'''
thousnd = int
thousnd = 1000
hundred = int
hundred = 100
tennum = int
tennum = 10
tenthous = int
tenthous = 10000
hundrths = int
hundrths = 100000
'''
definitions
'sysmem = system memory for the whole system
'thousnd' stands for 'thousand'
'hundred' stands for 'hundred' (obvious)
'tennum' stands for 'ten'
'tenthous' stands for 'ten thousand'
'hundrths' stands for 'hundred thousand'
the system doesn't go up to a million, so that isn't required
'''
print ("===")
print ("Inside Preview:")
print ("_______________________________________")
print ("System Binary Definitions")
print ("Contains: Binary and definitions")
print ("Language: Python 3.6.4")
print (" ") 
testconfirm = int(input("This is a system file that is not meant to be launched through the MEDOS terminal. This program holds the strings and values to ensure that the system is able to read and work with memory correctly. The file can be modified through the shell, but not MEDOS. This program cannot run, and is not designed to run. Press ENTER to quit"))
if testconfirm == 1:
    print ("Leaving")
    print ("Closing out of driver window")
else:
    print ("Exiting")   