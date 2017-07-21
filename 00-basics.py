'''
Basic Python Commands
'''

## This is a list
x = [1, 2, 3, 4]
print(x)
x[0]
x[2]
x[0:3]
x[-1]


## Strings
x = "Hello"
x[1]
len(x)
x + ' World'


## This is a tuple
x = 1, 2, 3, 4
print(x)
x[3]
x[3] = 1  ## Wont work

x = (1,2,3,4),(5,6,7,8)
print(x)
x[0]
x[0][0]


## This is a dictionary
x = {'label1': 1, 'label2': 2}
print(x)
x['label1']


## This is a loop
fact = 1

## The second arguement is in range is the stopping point
for i in range(1, 3):
  fact = i
  print(fact)
