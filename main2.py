s1={2,3,1}
s2={"a","b","c"}
s3=list(zip(s1,s2))
print("\n",s3)
list1=[10,20,30,40]
list2=[100,200,300,400]
for x,y in zip(list1,list2[::-1]):
    print(x,y)
stocks={"reliance","infosys","tcs"}
stockprice={2250,2500,3125}
newdict={stocks:stockprice for stocks,stockprice in zip(stocks,stockprice)}
print("\n{}".format(newdict))