import re
pan=input("Enter pan:\t")
if len(pan)>10 or len(pan)<10:
    print("Pan length must be equal to 10")
    exit
elif re.match("[^a-zA-Z0-9]",pan):
    print("Any characters other than numbers or alphabets are not accepted")
elif re.match("[0-9]",pan[0:5]):
    print("First five characters should be alphabets")
elif re.match("[a-zA-Z]",pan[5:9]):
    print("Characters 6 to 9 should be numbers")
elif re.match("[^a-zA-Z]",pan[9]):
    print("Last character should be an alphabet")
else:
    print("Valid")
