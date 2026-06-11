# create and write data to a file
with open("employee.txt","w") as file:
    file.write("Name: Mousam\n")
    file.write("Age: 19\n")
    file.write("Department: technical team\n")
#read the file
with open("employee.txt","r") as file:
          print("employee details:")
          print(file.read())
#append new data
with open("employee.txt","a") as file:
 file.write("\ncity: Greater Noida")

print("Data added successfully!")
          
