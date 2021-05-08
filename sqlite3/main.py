import sqlite3

#establishing a connection to the database
conn = sqlite3.connect("contacts.db")

#creating a cursor
c = conn.cursor()

#user inputs te contacts to the database
#name = input("Enter the name of the contact: ")
#number_of_contact = input("Enter the number of the contact: ")

c.execute("SELECT * FROM contact")


#making a list of dictionary to enter the data into the database
#list = [
#			(name),(number_of_contact),
#			
#
#	   ]
#executing a command to the database
print(c.fetchall())
#commiting the command to the database
conn.commit()

#closing the connection to the database
conn.close()


print("Command ran successfully...")