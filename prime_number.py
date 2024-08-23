num=eval(input("Enter a number:"))
sum1=0
if num==1:
    print(num,"is not a prime number")
elif num>1:
    for i in range(2,num):
        if(num%i)==0:
            sum1=1
            break
        if sum1:
            print(num,"is not a prime number")
        else:
            print(num,"is a prime Number")
