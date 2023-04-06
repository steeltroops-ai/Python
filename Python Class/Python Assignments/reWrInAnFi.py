File1=open(r"C:\Omniverse\Python Class\Class\Python Projects\Python r files\DisNumCVUL.txt","r")
File2=open(r"C:\Omniverse\Python Class\Class\Python Projects\Python r files\WriteItHere.txt",'w')
Line=File1.readlines()
for i in Line:
    if 'a' in i:
        i=i.replace('a','')
        File2.write(i)
File2.close()
File1.close()