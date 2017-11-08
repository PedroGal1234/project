#Pedro Gallino
#11/7/17
#My proggram for the Chapter 2 SOS in Biology Honors

from math import log

def Hplus_pH(x):
    pH = -1*log(x,10)
    return pH
def OHminus_pH(x):
    OH_pH = -1*log(x,10)
    return OH_pH
def OH(x):
    OH = 10**(-1*x)
    return OH
def H(x):
    H = 10**(-1*x)
    return H

print('1: If you know the concentration of H plus ions')
print('2: If you know the concentration of OH minus ions')
print('3: If you know the pH')

choice = int(input('Enter A number: '))


if choice == 1:
    print('You have to put a zero before the decimal if there is one')
    H = float(input('What is the molarity of H plus ions: '))
    OH_pH = (14 - Hplus_pH(H))
    OH = OH(OH_pH)
    print('The pH of your substance is:',Hplus_pH(H))
    print('The concentration of OH minus is:',OH)

if choice == 2:
    print('You have to put a zero before the decimal if there is one')
    OH = float(input('What is the molarity of OH minus ions: '))
    OH_pH = OHminus_pH(OH)
    pH = (14 - OH_pH)
    print('The pH of your substance is:',pH)
    print('The concentration of H plus is:',H(pH))

if choice == 3:
    pH = float(input('What is the pH: '))
    OH = OH(14-pH)
    print('The concentration of H plus is:',H(pH))
    print('The concentration of OH minus is:',OH)
else:
    print('Click go again')
    print('There are only three options')
    
