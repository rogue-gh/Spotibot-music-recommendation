# Peyton Ritze1rt 4:30-5:45
# COP1500 - Intro to Computer Science
# Album Recommendations by Genre

# sepTest = 14
# print("Sep= Parameter Test", sepTest, "Testing",sep='Hello World!')
# Sep didn't fit within the project, it puts "Hello World!" in place of
# every comma in this instance.

# My program didn't rely on any numeric operators. Here's what they all do:
# a = 20
# b = 5
# + adds values together
# a + b = 25
# - subtracts values
# a - b = 15
# * multiplies values
# a * b = 100
# / divides the right by the left
# a / b = 4
# % returns the remainder after dividing the left by the right
# a % b = 0
# ** is the same as exponents
# a**b = 3200000
# // this is floor division, where the numbers after the decimal are removed.
# 7//2 = 3

# + when used with strings combines two variable together into one string
# b = " five"
# print("My favorite number is"+b)
# This returns: My favorite number is five
# * as a string operator is used to multiply the variable by the number given
# print("My favorite number is"*2)
# This returns: My favorite number isMy favorite number is

# Program starts here:
import time
sleepTimer = 2


def endOption():
    print("\nThe format of is Album Title - Artist Name.")
#Early testing of functions, pretty redundant.


def printMenu():
    time.sleep(sleepTimer)
    print(" ")
    print("Hello! I'm Spotibot, here to give you recommen", end='')
    print("dations based on your selected genre!")
    for key in range(menuOptions.keys()):
        print (key,'.', menuOptions[key] )


menuOptions = {
    1: 'Pop',
    2: 'Rock',
    3: 'Jazz',
    4: 'Hip-Hop',
    5: 'Alternative',
    6: 'Settings',
    7: 'Exit',
}
if __name__=='__main__':
    while True:
        printMenu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number.')
        if option == 1:
            print("\n1 . 21 - Adele")
            print("2 . ÷ (Divide) - Ed Sheeran")
            print("3 . MONTERO - Lil Nas X")
            endOption()
        elif option == 2:
            print("\n1 . Rumours - Fleetwood Mac\n2 . The Dark ", end='')
            print("Side of the Moon - Pink Floyd\n3 . Back in Black - AC/DC")
            endOption()
        elif option == 3:
            print("\n1 . My Favorite Things - John Coltrane")
            print("2 . The Essential Duke Ellington - Duke Ellington")
            print("3 . Head Hunters - Herbie Hancock")
            endOption()
        elif option == 4:
            print("\n1 . My Beautiful Dark Twisted Fantasy - Kanye West")
            print("2 . Illmatic - Nas")
            print("3 . IGOR - Tyler, The Creator")
            endOption()
        elif option == 5:
            print("\n1 . OK Computer - Radiohead")
            print("2 . MTV Unplugged In New York - Nirvana")
            print("3 . AM - Arctic Monkeys")
            endOption()
        elif option == 6:
            while True:
                try:
                    sleepTimer = int(input('\nSet reset timer (in seconds).'))
                    print("Please wait...")
                    if sleepTimer < 1 or sleepTimer > 10:
                        raise ValueError
                    break
                except ValueError:
                    print("\nThe number cannot be below 1 or above 10.")
        elif option == 7:
            print("\nThank you for using the program.")
            exit()
        else:
            print('Integer must be within 1 and 7.')

#The operator != means does NOT equal to.
#elif option != 7:
#   exit()
#This would make it so that if the option chosen was anything other than 7,
#the program would exit.

#The and boolean operator is used to require two terms together.
#if option = 1 and option = 5:
#   print("You're using the boolean operator: and")

#The or boolean operator is used to require either term, not both like before.
#if option = 2 or option = 3:
#   print("You're using the boolean operator: or")

#Parameter passing functions weren't crucial to my program.
#Parameter passing functions make each function argument become a variable
#to which the passed value is assigned.
#def say(text):
#    text = int(input(text))
#   print(int(text))
#say("Super")
#The output would be:Super