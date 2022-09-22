'''
print('jack')
print('o-----')
print('  ||||')
print('jack '* 10)
print('@ '* 5)
print('\.?./ '*2)

#variables
Name='jack'                      #String
price=10                        #integer
price=20
rating=4.9                      #Float
is_published= True              #TRUE OR FALSE (Boolean condition)
print(price)

#Example
Full_name='john_smith'
age=45
is_new_patient=True

#getting inputs
name=input('what is your name? ')
Fav_color=input('what is your Fav color? ')
print(name + " likes " + Fav_color)

#type conversion
birth_year=input('birth year: ')
age=2022-int(birth_year)
print(age) 

#strings
course="python's course for beginner "           #use single, double or triple couts with their usage
course='python course for "beginner" '           #use single, double or triple couts with their usage
Message=' hi
how are you 
how is your work going on?                   #use single, double or triple couts with their usage
print(Message)

name='frost'
print(name[1:-1])

#formatting string
first_name='Jack'
last_name='frost'
#we want the msg as jack [frost] is a coder
msg=f'{first_name} [{last_name}] is a coder'            #f is formating keyword using infront of the str
print(msg)

#string methods
course='Python for Beginner'
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('y'))
print(course.replace('Beginner','jack'))     #After the dot that function called as methods
print('Python' in course)                       #like a boolean function but its a in function or methods

#Arithmetic operators
x=10+6          #Add
x=10-6          #Sub
x=10*6          #muliplication
x=10/6          #display float value
x=10//6         #display integer value
x=10%6          #remainder
x=10**6         #exponential power
print(x)

#If Statement
#ex_1
price=1000000
has_good_credit=False
if has_good_credit:
    down_payment = 0.1*price
else :
    down_payment = 0.2 * price
print(f'down payment : ${down_payment}')
print('happy day')

#Ex_2
is_hot=False
is_cold=False

if is_hot:
    print("It's is a Hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It is cold day")
    print("wear warm clothes")
else :
    print("It is a lovely day")
print("enjoy your day")

#while loop
i=10
while i<=100:
    print('*'* i)
    i=i+10
print("done")

#while guessing game
secret_number=8
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input("guess: "))
    guess_count +=1
    if guess == secret_number:
     print('you,won!')
    else :
     print("Wrong Guess!")

#tuples
z=('car','bike','bus','scooter')
y=list(z)
y[3]='flight'
x=tuple(y)
print(x)

#Dictionaries
dictt={
    'name':'jack',                   #example_'name'=key , 'jack'=value our requirement the key & values are changeable
    'age':30,
    'vehicle':'Audi',
    'location':'USA'
}
dictt['vehicle']='tesla'            #this is a update method by change one values
dictt.update({'name':'frost'})      #this is a format to update the multiple key values
dictt['province']='D.C'             #Add the extra key & values
print(dictt)
'''




