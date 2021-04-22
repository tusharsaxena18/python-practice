import sqlite3

#establishing a connection
conn=sqlite3.connect("contact.db")

#creating a cursor
c=conn.cursor()

#creating a list
listi=[
		('Mummy','74522'),
		('Mausi','36362534'),
		('Nana','12831849283')
	]

#executing a query
#DATATYPE : TEXT;INTEGER;BLOB;NULL;REAL
c.execute("SELECT * FROM contacts WHERE name = 'Mummy'")

#fetching the data
#print(c.fetchone())
#print(c.fetchmany())
items = c.fetchall()

#using a loop to make the data readable
for item in items:
	print(item[0], item[1], sep=' | ')

#commiting the command
conn.commit()

#closing a connection
conn.close()

#testing the program
print("Command executed succesfully.....")