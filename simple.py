
# function for addition
def adder(z):
    x = 1 + 2 /3
    #print(x)
    y = x + z
    return y

# use of adder
x = adder(1)
#print(x)

# increment result by one
z = x + 1

#print result
# print(z)
a = 1
b = 2
#print("a, b")
#print(a , b)
'''
does not work!
a = b
b = a
'''

# this does!
# simultaneous assignment!
a, b = b, a
#0, 1 = 0, 1
#print(a, b)

# all valid !
# var = arithmetic expression
# var = numeric literal
# var = strings
# var = output of functions
# var = input from user
# var = var
# var = var + (-) (op) val
# var = function names

total = 0
for i in range(100):
    # [0, 1, 2, ... 99]
    x = adder(i)
    total = total + x
print(total)


# ...

