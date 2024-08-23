new1={1,2,3,4,5,6}
print(len(new1))

new=0
while new<=10:  #this loop coutinue when new value < equlas to 10
    if new % 2==0: # this loop check the even values
        new+=1  #new=new+1
        continue #this cammand is use for if it is even than command is excuted and go for next one
    print(new)
    new +=1 #new=new+1

''''+=' is a opperater this  can be add the values
    '-=' also same this can be subtract the values
   '*= and /=' they are using to print multiplication and divison '''
s=10
s +=6
print(s)

#normal addition sub and mul and divison

x=10
y=5
print(x/y)

print("Hello.World!")


vowel=['a','e','i','o','u']
string="sandeep"
count=0
for i in string:
    if i in vowel:
        count+=1
    print(count)

