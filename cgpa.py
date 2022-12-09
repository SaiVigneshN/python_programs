cgpa=float(input('enter cgpa:'))
if(cgpa>=9 and cgpa<=10):
    print('outstanding')
elif(cgpa>=8 and cgpa<9):
    print('Excellent')
elif(cgpa>=7 and cgpa<8):
    print('Good')
elif(cgpa>=6 and cgpa<7):
    print('Average')
elif(cgpa>=5 and cgpa<6):
    print('Should do better')
elif(cgpa<5 and cgpa>=0):
    print('Must improve')
else:
    print('Invalid input')
