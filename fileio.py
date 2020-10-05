'''


file i/o

read in -> write out


CS 177



================================
understanding what a file is


Files, in essence are collections of information

variables -> RAM : 
    program termination in python means everything from
    RAM is cleaned. 
    
    x = 3
    
    restart terminal

    print(x)
    
    error

files -> persistent

    but use the same type of encoding as variables.
    
    RAM
         
    |---| ...  | --- |

      X           3        


    File (simplified):

    |start  | | | |. . . .|end  |
    

a file is no more than a large (mostly and ideally) contiguous set of
values


so if we see:

    Hello
    world

the file fileobject looks a little like this:

0x68 0x65 0x6c 0x6c 0x6f 0x20 0xa 0x20 0x77 0x6f 0x72 0x6c 0x64


    "hello\nworld\n"




opening a file puts us at the start of the file

closing puts us back at the beginning

    .open()
    .read()
     =====================

     ----                  -> string
     ----
     ----
     ---
 
     =====================
    .read()

                           nothing
    

'''


# open
                   # file name
fileobject = open("pigeon-racing",'r')
listoflines = []


# methods of reading uncomment to see how they work
'''
.read()
    file object -> string
.readlines()
    file object -> list
iteratively
initial string = none, while true -> string -> while false, final string = Type 

#method 1 .read
# read file
filestring = fileobject.read()
#print(filestring)
# split into lines 
filelist = filestring.split('\n')
print(filelist)
# split by commas
columnNames = filelist[0].split(',')
#print(columnNames)
# iterate through list and replace each line with its
# split counterpart
for i in range(len(filelist)):
    # index
    print(i)
    # before
    print(filelist[i])
    filelist[i] = filelist[i].split(',')
    # after
    print(filelist[i])
#print(filelist)
newlist = []
for i in  range(len(filelist)):
    newlist.append(filelist[i].split(','))

#print (filestring.split('\n'))

#method 2 .readlines
filelist = fileobject.readlines()
columnNames = filelist[0].split(',')

'''

#method3 iterative
# read the file
filelist = []
for line in fileobject:
    filelist.append(line)

########### file is now closed
fileobject.close()
###########

# get the column names
columnNames = filelist[0].split(',')
print(columnNames)

# instead of using indices, lets use column names
columns = {}
ix = 0
for i in columnNames:
    columns[i] = ix
    ix+=1
print(columns)
for i in range(len(filelist)):
    filelist[i] = filelist[i].split(',')

# now we can use the column names as indices

namedl = []
unnamedl = []
utime = 0
named = 0
ntime = 0
unnamed = 0
for i in range(1, len(filelist)):
    # '' - > false -> (bool(''))
    # blank -> nothing
    # not == ('') -> true -> bool('...') 
    # nonblank -> give name
    name = filelist[i][columns['Name']]
    place = filelist[i][columns['Pos']]
    time = filelist[i][columns['Speed']]
    
    # if a pigeon is named append to the named list
    if bool(name):
        namedl.append([name,place,time])
        ntime += float(time)
        named += 1 
    # if it is not named append to the unnamed list
    else:
        unnamedl.append([name,place,time])
        utime += float(time)
        unnamed +=1

avtime = ntime/named
uavtime = utime/unnamed
total= 0


for i in namedl:
    total+= (float(i[2])- avtime)**2
    print("{:<20} {:>4} {:>10}".format(i[0], i[1],i[2]))
average=total/named
stdv = average**(1/2)
print()
print("{:^20} {:^10} {:>10}".format("average","variance", "stddev"))
print("{:<20.3f} {:>4.3f} {:>10.3f}".format(avtime, average,stdv))

averageunnamed=0 
ix = 0
nprint = 0

# iterate for every element in list
# save to a string
# write to output

output = ''
for i in unnamedl:
    averageunnamed+= (float(i[2])- uavtime)**2
    
    # print first 5 and last 5
    if ix<5 or ix > len(unnamedl)-6:
        output += "{:<20} {:>4} {:>10}\n".format(i[0], i[1],i[2])
        print("{:<20} {:>4} {:>10}".format(i[0], i[1],i[2]))
    elif ix > 5 and nprint < 5:
        output +=  "{:^34}\n".format(".")
        print("{:^34}".format("."))
        nprint += 1
    ix += 1
# get std dev and variance
averageunnamed= averageunnamed/unnamed
stdv2 = averageunnamed**(1/2)

print()
print("{:<20} {:<10} {:<10}".format("average","variance", "stddev"))
print("{:<20.3f} {:<10.3f} {:<10.3f}".format(uavtime, averageunnamed,stdv2))


z = (avtime - uavtime)/(((average/named) +(averageunnamed/unnamed))**(1/2))


print("z-score: ", z)

outfile = open("output.txt",'w')
for i in output:
    outfile.write(i)
outfile.write("z-score: " + str(z))
outfile.close()
    

# TODO
# practice


# abstract the above to functions and make the final datatype
# a list

# file -> fileObj -> str/list (preprocessing) -> list


# abstract the above to a function that prints a table:
# and constructs a string to write
# list -> str
# def listPrinter(listToPrint):
# # for loop 

# abstract the above to a function to write a file
# str -> None
# def stringWriter(str)

