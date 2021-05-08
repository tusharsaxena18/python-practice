import time
import datetime

def delay3 ():
    time.sleep(2)

def delay2 ():
    time.sleep(1)

def delay ():
    time.sleep(0.5)

name=input("Enter your name: ")
a=input("Choose a noun: ")
b=input("Choose a plural noun: ")
c=input("Choose another noun: ")
d=input("Name a place: ")
e=input("Choose an adjective: ")
f=input("Choose another noun: ")

print("-------------------------------")
delay2()
print(name + " This is a MAD LIBS GENERATOR BY RealSpartanTS")
delay()
print("Be kind to your "+ a ,"- footed "+ b)
delay3()
print("For a duck may be somebody's " + c)
delay3()
print("Be kind to your "+b,"in "+ d)
delay3()
print("Where the weather is always "+ e)
print("")
delay2()
print("You may think that is this the "+f)
print("Well it is.")
delay2()
print("-------------------------------")

print("Press any key to exit: ")
end=input("")
if end in ['Y']:
    exit()
else:
    exit()