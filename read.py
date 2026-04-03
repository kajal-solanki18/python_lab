f=open("one.txt","r")
data=f.read()
print("file content:",data)
f.close()

f=open("one.txt","r")
data=f.read(5)
print("file part:",data)
f.close()

f=open("one.txt","r")
line1=f.readline()
line2=f.readline()
line3=f.readline()
print("Line1:",line1)
print("Line2:",line2)
print("Line3:",line3)
f.close()

f=open("one.txt","r")
lines=f.readlines()
print("List of line:",len(lines))
f.close()


f=open("one.txt","r")
lines=f.readlines()
print(lines[1].strip())
f.close()
