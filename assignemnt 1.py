"""design a command-line contact book that allows user to to add, search and delete contacts using dictionaries and loops"""

#what to do: create a function that asks for user input
#assign a value to the user input(an integer in the form of a string)




 
full_name = input("whats your full name")
number = input("contact number")   
print(full_name)
print(number)

contact_information = {full_name:number}
for full_name, number in contact_information.items():
    print('\n', full_name,'\n', number)

print(contact_information[full_name])

contact_information.clear 
print(contact_information) 
 