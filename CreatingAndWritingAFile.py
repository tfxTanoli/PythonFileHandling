# Create and Write In A File
file = open("demo.txt", "w") #use "a" for append
try:
    file.write("FA21-BCS-130 Muhammad Usman")
    print("File Created Successfully.")
    file.close()
except Exception as error:
    print(error)