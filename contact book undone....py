class contact:
    def __init__(self,name,number):
        self.name = name
        self.number = number

print("Do you want to view a contact or store a contact (1/2)")
value = int(input(""))

if value in [1]:
    print("Enter the name of your contact.")
    name_of_contact=input("")
    print("Enter the umber of your contact.")
    number_of_contact=input("")


elif value in [2]:
    print("Enter the name of your contact.")
    name_of_contact2=input("")
    

else:
    print("Invaild Option")