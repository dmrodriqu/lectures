'''

Decision Structures


If
    if
        if
            if
                if
                    if





Assignments:

    Hw 4 - Monday
    
    LP 2
    Lab 2
    HW 5 - Mon 2/17



'''


'''

Main idea:

     
    Step 1
    
    Step 2

    Step 3

    |
    |
    |
    V
    end


    branch:

        step 1

        step 2

     ->  condition
    |
    |       |
    |       |
    |      / \
    |     /   \
    L step3a  step3b
                |
               end 



we need to develop a gate for our code.
1 if we can let the condition pass
0 if the condition will not pass.
'''

def ifGate(gate):
    if gate == 1:
        print("pass")

def willItpass():
    ifGate(0)
    ifGate(1)

#willItpass()

'''
conditions: 

        start 
          |
   let it pass at 1?
       /    \
    yes     no
   print    dont print

'''

# lets replace it with a special data type: the Boolean
#print (True == 1)
#ifGate(True)


'''
now lets simplify
'''

def ifGate(gate):
    if gate:
        print("pass")
#ifGate(True)



'''

Converting any type to a bool will convert: 

    Empty and null values = False.
    Else = True
Conditions are formed through boolean expressions.

Each expression is a proposition that may be either True or False.

'''

#print(bool(234))
#a = [1]
#print ('' == 1)
#print (a == a)
#print (bool([]) == False)
#print ([] == False)

'''
Ifs and else ifs and elifs



'''


def fizzbuzz(n):
    for i in range(1, n):
        if (i % 3 == 0) and (i % 5 ==0):
            print('fizzbuzz' ,i)
        elif i % 3 == 0:
            print('fizz', i)
        elif i % 5 == 0:
            print('buzz', i)
# fizzbuzz(20)
