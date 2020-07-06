# File compatibility for file formats
# Currently only keeps them as values, and applies an outputted name value to them
# They don't apply to the system all the way yet
TXT = str
TXT == ("TXT File (plain text document)")
BAT = str
BAT == ("BAT File (Batch file)")
MID = str
MID == ("MID File (MIDI Audio file)")
SYS = str
SYS == ("SYS File (System fole)")
print ("===")
print ("Inside Preview:")
print ("_______________________________________")
print ("File definitions for 4 file types")
print ("Contains: Definitions, Comments, File Info")
print ("Language: Python 3.6.4")
print (" ") 
testconfirm = int(input("This is a system file that is not meant to be launched through the MEDOS terminal. This program holds the strings and values to ensure that files are compatible with the system. The file can be modified through the shell, but not MEDOS. This program cannot run, and is not designed to run. Press ENTER to quit"))
if testconfirm == 1:
    print ("Leaving")
    print ("Closing out of driver window")
else:
    print ("Exiting")   