import pandas as pd

#One Dimentional Array
a=pd.Series([1,2,3,4,5])
s=pd.Series([1,3,5,7,9])
print(a)
print(s)
x=pd.Series([1,3,5,7],index=['a','b','c','d'])
print(x)

#Two Dimentinal array
data={
    'Name':['sandeep','Naruto','Luffy'],
    'Age':[24,19,20],
    'City':['Khammam','Konaha','FlowerCity']}
datas=pd.DataFrame(data)
print(datas)
#reaing excel by using pandas
data2=pd.read_excel('Book1.xlsx')
print(data2.head())

