"""design a command-line contact book that allows user to to add, search and delete contacts using dictionaries and loops"""






#user inputing names and contact number
full_name = input("whats your full name")
number = input("contact number")   
print(full_name)
print(number)


#retrieving cintact information
contact_information = {full_name:number}
for full_name, number in contact_information.items():
    print('\n', full_name,'\n', number)

#searching for a contact number using full name
print(contact_information[full_name])


#deleting the entire contact information.
contact_information.clear 
print(contact_information) 
 
