'''
Strings lists slicing

All your ix belong to us.

CS177
1/30/2020

Dylan Rodriquez
'''


'''
Strings:
    enclosed in quotes " "
'''

thisIsAString = "string"
thisIsAlsoAString = 'thisIsAStringToo'

print(thisIsAString)


'''
Sequences:

    An enumerated, ordered grouping of elements that can be 
    accessed using indices.

'''

print()
sequence1 = [1,2,3,4,5]
print()
print(sequence1)

charlist  = ['a', 'b', 'c', 'd']

print()
print(charlist)
print()
wordList = ['marry', 'had', 'a', 'little', 'lamb']
#             0        1     2     3         4 

print(wordList[0])
print()
triList = [sequence1, charlist, wordList]

word = "abcd"

alsoAWord = 'abcd'

# the following does not work, why?

#listList = [sequence1, charlist, wordList, listList]


'''

slicing sequences


IMPORTANT!!!

SYNTAX:
    sequenceName [from:to,step]  -> sequence
    where from is inclusive, to is exclusive:
    
                [from, to)

    *hint*
    step can be used forward or backward

'''

#indexing lists and strings is the same
myString = 'BoilerUpHammerDown'
#           012345


myString = [1,2,3,4,5,6,7,8,9]
boiler = myString[0:6]
evens = myString[0::2]
weirdWord = boiler + evens
print()
print(weirdWord)
print()
print('abc' + 'def')



'''

Iteration over sequences


'''


# we might get an error here if the string length
# is shorter than our range


# what if we append results?
#           0 1 2 3 4 5 6 7 8
myString = [1,2,3,4,5,6,7,8,9]
strlen = len(myString)
# range(5)
# [0,1,2,3,4]

for i in range(strlen):
    print(myString[i])



a = 0
for element in myString:
    a += element


 

# what else can we do here with the results?


# lets try counting characters


'''

String methods!

Here are some common methods for strings

'''

stringTesting = 'look at what this method does'

#capitalizations

print()
stringTesting = stringTesting.upper()
print(stringTesting)
stringTesting = stringTesting.lower()
print(stringTesting)
stringTesting = stringTesting.capitalize()
print(stringTesting)
stringTesting.swapcase()

print(stringTesting)

# capitalize what
# split everything
listofwords = stringTesting.split()
# where is what
indexofwhat = listofwords.index('what')
print(indexofwhat)
capitalizedWhat =  listofwords[2].title()
listofwords[2] = capitalizedWhat
print(' '.join(listofwords))

'''

string.split -> list of words

' '.join(list of words) -> string


''' 


# alpha numeric checking

'a1'.isalpha() # -> bool (true or false)
'32'.isdigit() # -> bool (true or false)


# string replacement
print('abcd'.replace('a','!'))

# finding substrings

#returns the number of times substring occurs


# prefix and suffix testing
# string similarity testing 


'''

List Methods


'''

testlist = [0,6,3,6,2,4,7,4,8]

testlist = testlist.append(1)
testlist.sort()
testlist.reverse()
testlist testlist.index(6)
testlist.insert(0,42)
testlist.count(4)
testlist.remove(6)


'''

Reverses a string and inverts capitalization ('Forward' -> 'DRAWROf')
Capitalizes alternating letters in a String

Counts the number of words in a String

Converts the numeric characters 0 – 9 in a String to the characters 
displayed above them on the keys of the keyboard. (1 to !, 2 to @, 3 to # …)

'''


'''
Accepts a series of Strings from the user, stores them CAPITALIZED 
in a list and then prints each String on a separate line

Accepts a String from the user then creates a List containing the following 
statistics about the String:  word count, average word length, 
the individual words, the number of vowels, the number of non-vowels 
and the number of spaces

Accepts 20 Float values from the user storing them in a List, then prints the 
following statistics about them: average, max, min, standard deviation and range.

'''
