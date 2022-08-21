import random
''' 
random.seed(10)
print(random.random())
#the generator creates a random number based on the seed value, so if the seed value is 10, you will always get 0.5714025946899135 as the first random number.

x = random.getstate()
print(x)

# returns random no. between 0 & 1
print(random.random())

#returns a random item
myList = ['hydrogen' , 'helium' , 'lithium','berilium']
print(random.choice(myList))

#returns a random no. from specified parameters *(start ,stop ,step)
print(random.randrange(0,9 ,1 ))

#returns a random interger froms given parameters* (start , stop)
print(random.randint(1,9))

#shuffls the items
random.shuffle(myList)
print(myList)

#returns a random float number between given parameters
print(random.uniform(4,5))
'''

'''practice!'''
'''
WAP to make a dice for a ludo by different  methods
'''

def Randint(x,y):
    dice = random.randint(x,y)
    print(dice)


def Choice():
    list = [1,2,3,4,5,6]
    print(random.choice(list))


def Randrange(x,y,z):
    Dice= random.randrange(x,y,z)
    print(Dice)

Randint(1,6)
Choice()
Randrange(1,6,1)