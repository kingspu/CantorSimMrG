import math
import random
import winsound


primesand99 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 99]


constants = {
    "                 tau":2*math.pi,
    "                  pi":math.pi,
    "                 phi":(1+5**(1/2))/2,
    "                   e":math.e
}

noncirrationals = []
cantorlen = 10


def prompt(demand: str,optionname: list[str],func: list[callable]):
    print(demand)
    for i in range(0,len(optionname)):
        print(f"{i+1}: {optionname[i]}")
    choice = input("Choose an option:")
    try:
        choice = int(choice)
        if choice in range(1,len(optionname)+1):
            func[choice - 1]()
        else:
            print("Pick an allowed choice")
            prompt(demand,optionname,func)

    except ValueError:
        print("Pick an allowed choice")
        prompt(demand,optionname,func)

def promptInt(demand: str,range: list[int]):
    try:
        number = int(input(demand))
        if number < range[0] or number > range[1]:
            print("Please chose an integer between 1 and 16")
            promptInt(demand, range)
        else:
            return number
    except ValueError:
        print("Please chose an integer between 1 and 16")
        promptInt(demand,range)

def makenumber():
    global primesand99
    global constants
    global cantorlen
    numbers = primesand99 + list(constants.keys())
    chosen = []
    cantorsnumber = []
    print("CANTOR'S DIAGONAL PROOF SIMULATION")
    print("First Number : *0*")
    for i in range(1,cantorlen+1):
        current = numbers[random.randint(0, len(numbers) - 1)]
        numbers.remove(current)
        if current in constants.keys():
            current_number = constants[current]
        else:
            current_number = current

        spacing = ""
        betterspacing = ""
        if current_number < 10:
            spacing = " "
        if i < 10:
            betterspacing = " "


        if current in primesand99:
            stupidstring = f"{i}.{betterspacing}(Square root of {spacing}{current})/10 : {(current**(1/2))/10:.{cantorlen}f}"
            stupidstring = str(stupidstring)
            stupidstring = f"{stupidstring[:i + 29]}*{stupidstring[i + 29]}*{stupidstring[i + 30:]}"
            print(stupidstring)
            current = str((current**(1/2)) / 10)
        else:
            stupidstring = f"{i}.{current}/10 : {current_number/10:.{cantorlen}f}"
            stupidstring = str(stupidstring)
            stupidstring = f"{stupidstring[:i + 29]}*{stupidstring[i + 29]}*{stupidstring[i + 30:]}"
            print(stupidstring)
            current = str(current_number/10)

        cantorsnumber.append(current[i+1])
    final = ""
    for i in cantorsnumber:
        final = final + str(i)
    print(f"New number generated from diagonal: \n 0.{final}")
    print("THE NEW NUMBER GENERATED FROM THE DIAGONAL OF THE LIST OF IRRATIONAL NUMBERS ABOVE, DOES NOT MATCH ANY OF THE NUMBERS IN SUCH LIST.")
    if int(final) in numbers:
        print("PROOF RESULT: All infinities are the same size")
    else:
        print("PROOF RESULT: There are different sized infinities")
    prompt("What do you want do now?",["Give me a new number","Go to menu"],[makenumber,start])

def settings():
    prompt("Choose Options",["Change length of number","Play a random beep","Back to Menu"],[changenumlen,playnoise,start])

beepmeter = 0
def playnoise():
    global beepmeter
    if beepmeter < 10:
        x = random.randint(1000,5000)
        winsound.Beep(x,20)
        beepmeter = beepmeter + 1
        print("beware of the omega beep")
        settings()
    else :
        winsound.Beep(300,10000)
        beepmeter = 0
        settings()

def changenumlen():
    global cantorlen
    cantorlen = promptInt("Change Cantor's Number Length(Anywhere from 1 to 16, default is 10):", [1,16])
    print("Changed")
    settings()


def quitNumber():
    print("Thank you for using the Cantor's Diagonal Proof Simulator. See you again soon!")
    quit(0)


def start():
    prompt("Cantor's Diagonal Proof Program Main Menu",["Generate My Number", "Settings" ,"Quit"],[makenumber,settings,quitNumber])
'''
IGNORE
def findvecsum(Vecs : list[{str : list[int,int]}]):
    xco = 0
    yco = 0
    Resultant = 0
    Theta = 0
    for i in range(0,len(Vecs)):
        xco = xco + (list(Vecs[i].values())[0][0] * round(math.cos((math.pi/180)*list(Vecs[i].values())[0][1]),5))
        yco = yco + (list(Vecs[i].values())[0][0] * round(math.sin((math.pi/180)*list(Vecs[i].values())[0][1]),5))

    if xco > 0:
        Theta = round(math.degrees(math.atan(yco/xco)),2)
    else:
        Theta = round(math.degrees(math.atan(yco / xco)) + 180,2)

    Resultant = round((xco**2+yco**2)**(1/2),5)
    print(Resultant,Theta)
'''

start()
