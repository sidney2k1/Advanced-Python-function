num=int(input("you want odd and even numbers under what value?"))
oddlist=[i for i in range(num) if num%2!=0]
print("The list of odd numbers:",oddlist)
evenlist=[i for i in range(num) if num%2==0]
print("the list of even numbers:",evenlist)
list1=["apple","banana","papaya","mango","melon"]
fruits=[x[0].upper()+ x[1:] for x in list1]
print("Fruits as proper nouns:",fruits)