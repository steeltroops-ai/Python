file = open(r"C:\Omniverse\Python Class\Class\Python Projects\Python r files\DisNumCVUL.txt", "r") 
data = file.readlines() 
 
for i in data: 
    print(i.replace(" ", "#")) 