pan=input('Enter the pan:\t')
if len(pan)!=10:
    invalid=True
else:
    for i in range(0,5):
        if pan[i].isalpha():
            invalid=False
            break
    for j in range(5,9):
        if pan[i].isdigit():
            invalid=False
            break
    if pan[9].isalpha:
        invalid=False
if invalid==True:
    print("Invalid")
else:
    print("Ok")
