'''
#variables 

day = 3
month = 'Sept'
temp = -68
day_name = 'Tuesday'

print(f'Today is {day_name}, {month} {day}th and it is {temp} degrees outside.')

#boolean

day = 3
weight = 200.5
month = ' December'

lightIsOn = True
lightIsOff = False

if lightIsOn:
    print('The ligh is on !!')
    print('Hi there')

Door_Open = True

if Door_Open:
    print("GTHO")

#compare & else
    
lightIsOn = False
lightIsOff = False

if lightIsOn:
    print('NEPA don brong light!!')
else:
    print('We de for darkness')

weight = 200.5 

if weight < 205:
    print('Omo you slim o')

Age = 18
if Age >= 18:
    print("You are adult :) ")
else:
    print('You are a child :(')

#odd or even number
    
oddNumber = False
evenNumber = True

number = 27
remainder = number % 2

if remainder == 1:
    print(oddNumber)

else:
    print(evenNumber)


#random numbers

import random

print(random.randint(1, 20))

print(random.random())

choices = ('yes', 'no', 'maybe')

randomChoice = random.choice(choices)

print (randomChoice)


#fortune cookie

import random

luckyNumber = random.randint(1, 105)

fortuneNumber = random.randint(1,3)

fortuneText = ''

if fortuneNumber == 1:
    fortuneText = 'You will have a great day'

if fortuneNumber == 2:
    fortuneText = 'omo e go be'    

if fortuneNumber == 3:
    fortuneText = 'howfar relax o'  

print(f'{fortuneText} , Your Lucky nuumber is: {luckyNumber} ')

 #List
Fav_movies = ['Marvel', 'DC','Lego', 'Dune']

print(Fav_movies[3])

fav_num = ['9', '5' , '4']

print(fav_num[0])

Fav_movies = ['Marvel', 'DC','Lego', 'Dune']

len(Fav_movies)

print(len(Fav_movies))

Fav_movies.append('Tony Stark')

print(len(Fav_movies))

print(Fav_movies)

Fav_movies.insert(1, ' Aquaman')

print(Fav_movies)

del(Fav_movies[0])

#for loop

for number in range(100001):
    print(number)


Fav_movies = ['Marvel', 'DC','Lego', 'Dune']

for movie in Fav_movies:
    print(movie)


for x in range (41):

    print ((x + 1)*2)


#dictonary - with list we use [] , with dictonary we use {}

cats = {'pank': 6, 'tom': 15, 'pat': 8}

cats['willy'] = 1

del(cats['tom'])
len(cats)

print(len(cats))

test = {'1:yes', '2:no', '3:maybe'}

print(test)


#even number addition
    
numbers = [62, 66, 94, 97, 25, 11, 68, 54, 48, 67]
print(numbers[0] + numbers[1]+ numbers[2]+ numbers[6]+ numbers[7]+ numbers[8])


#even number addition - Real SOLUTION

numbers = [62, 66, 94, 97, 25, 11, 68, 54, 48, 67]

totalEvenSum = 0

for number in numbers:
    if number % 2 == 0:
        totalEvenSum = totalEvenSum + number

print (totalEvenSum)


#word analyzer

text ='Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal."'

print(len(text.split()))

#word counter analysis

text = 'Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.'

print(text.split())

wordCount = {}

for word in text.lower().split():
    if word in wordCount:
        wordCount[word] += 1
    else: 
        wordCount[word] = 1

print(wordCount)

#functions

def bark():
    print('Dog eat dog, woof woof!')
    print('black sheep')

for x in range(100):
    bark()

def greetings():
    print('Hello Nick')

greetings()

#parameters

def greetings(name):
    print(f'Hello {name}!')

greetings('henry')

def add_numbers(num1, num2):
    print(num1 + num2)

add_numbers(4,8)
add_numbers(100,9)

#parameters for dog name

def dog_info(name, age):
    print(f'Hi {name}, I am happy to see you, this is the first time seeing a {age} years old doggie.' )

dog_info('Sako', 85)


#return
def double(number):
    return number*2

newNumber = double(5)

print(newNumber)


#return texts to upper case
def caps(strings):
    return strings.upper()

newString = caps('ikechdgbsgbukWu')

print(newString)

#OR do this without the new string line
print(caps("marg"))

names = ['jerry', 'ana', 'ugo', 'ken']

for name in names:
    print(caps(name))


wallet = 40

wallet -= 8 # same as this line << wallet = wallet - 8


#input

userText = input('Enter some texts: ')

print(userText.upper())

userNumber = input('what do you wanna double?: ')

print(int(userNumber) * 2)


#In this project, if the user enters 1, the text will be converted to uppercase. For any other input (including 2), the text will be converted to lowercase.

userText = input('Enter some texts: ')

choice = int(input('Enter 1 for UPPERCASE or 2 for lowercase: '))

if choice == 1:
    print(userText.upper())

if choice == 2:
    print(userText.lower())


#number gussing game , game loop

guess = int(input('What is your guess bro?: '))
correctNumber = 9
guessCount = 1

while guess != correctNumber: #guess isnt = to correct number
    guessCount += 1 #guess count increase by 1
    guess = int(input('What is your guess bro?: '))

print(f'OMO you get am, The right answer was {correctNumber}, it took {guessCount} guesses to find it. ')


#number gussing game , game loop BUT adding HIGHER,LOWER OR POLISH GUESS

import random
import time

print('How far, you don land the guessing game , I go pick number between 1 & 100.')
time.sleep(5)
print('E de load, i de pick am...')
time.sleep(3)

guess = int(input('What is your guess bro?: '))
correctNumber = random.randint(1,101)
guessCount = 1

while guess != correctNumber: #guess isnt = to correct number
    time.sleep(2)
    guessCount += 1 #guess count increase by 1
    if guess < correctNumber:
        guess = int(input('You BANG AM, You need to guess HIGHER, What is your guess bro?: '))
    else:
        guess = int(input('You BANG AM, You need to guess LOWER, What is your guess bro?: '))

print(f'OMO you get am, The right answer was {correctNumber}, it took {guessCount} guesses to find it. ')

'''

#another version of finding odd or evwn number.
#The idea is that if you keep subtracting 2 from an even number, you will eventually reach 0, and if you keep subtracting 2 from an odd number, you will eventually reach 1.

def even(number):
    if number == 0: 
        return True

    elif number == 1:
        return False
    
    else:
        return even(number - 2)

num = int(input('Enter a number: '))

if even(num):
    print(f'The num {num} is Even')
else:
    print(f'The num {num} is Odd')