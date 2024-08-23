# *****
# ****
# ***
# **
# * print this output
print("5 to 1 pattern:")
n=5;
for i in range(n,0,-1):
    print("*"*i);
print("1 to 5 pattern:")
n1=5
for i in range(1,n1+1):
    print("*"*i)

#for numbers

print("forword numbers")
a=5
for i in range(1,a+1):
    for j in range(1,i+1):
      print(j,end=" ")
    print()

#back word
print("backword numbers")
b=5
for i in range(b,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#alfabets

print("for word A to E")
c=5
for i in range(c):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()

print("back word E to A")
d=5
for i in range(d,0,-1):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()