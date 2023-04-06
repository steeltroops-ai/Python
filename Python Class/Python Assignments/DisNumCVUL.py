#read()
f=open(r"D:\Omniverse\Python Class\Python Projects\Python r files\DisNumCVUL.txt",'r')
File = f.read()
vowels=consonants=uppercase=lowercase=0
vowels_list=['a','e','i','o','u']
for i in File:
    if i in vowels_list:
        vowels += 1
    if i not in vowels_list:
        consonants +=1
    if i.isupper():
        uppercase += 1
    if i.islower():
        lowercase += 1
f.close()

print("Number of Vowels = ",vowels)
print("NUmber of consonants = ",consonants)
print("Number of uppercase characters = ",uppercase)
print("Number of Lowercase characters = ",lowercase)