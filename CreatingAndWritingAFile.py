# Create and Write In A File
#use "a" for append
#use "x" for creating new empty file
#use "w" for overwriting a file

file = open("demo.txt", "w")
try:
    file.write("FA21-BCS-130 Muhammad Usman")
    print("File Created Successfully.")
    file.close()
except Exception as error:
    print(error)