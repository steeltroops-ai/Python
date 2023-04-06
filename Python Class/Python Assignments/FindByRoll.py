import pickle
#creating the file and writing the data
f=open(r"C:\Omniverse\Python Class\Class\Python Projects\Python r files\students.dat", "wb")
#list index 0 = roll number
#list index 1 = name
#list index 2 = marks
pickle.dump([1, "Wakil", 90], f)
pickle.dump([2, "Tanish", 80], f)
pickle.dump([3, "Priyashi", 90], f)
pickle.dump([4, "Kanupriya", 80], f)
pickle.dump([5, "Ashutosh", 85], f)
f.close()

#opeining the file to read contents
f=open(r"C:\Omniverse\Python Class\Class\Python Projects\Python r files\students.dat", "rb")
roll=int(input("Enter the Roll Number: "))
marks=float(input("Enter the updated marks: "))
List = [ ] #empty list
flag = False #turns to True if record is found
while True:
    try:
        record=pickle.load(f)
        List.append(record)
    except EOFError:
        break
f.close()

#reopening the file to update the marks
f=open(r"C:\Omniverse\Python Class\Class\Python Projects\Python r files\students.dat", "wb")
for rec in List:
    if rec[0]==roll:
        rec[2] = marks
        pickle.dump(rec, f)
        print("Record updated successfully")
        flag = True
    else:
        pickle.dump(rec,f)
f.close()
if flag==False:
    print("This roll number does not exist")
    