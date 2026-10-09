#question-1 print all elements
lst=[10,20,30,40,50]
for i in lst:
    print(i)

#question-2 print each element with its index
lst=[10,20,30] 
for i in range(len(lst)):
    print(i,lst[i]) 

#question-3 find the sum
lst=[5,10,15,20]
sum=0
for i in lst:
    sum=sum+i
print(sum)

#question-4 find the largest element
lst=[12,45,23,67,34]
largest=lst[0]
for i in lst:
    if i>largest:
        largest=i
print(largest)    

#question-5 find the smallest element
lst=[12,45,3,67,34]
smallest=lst[0]
for i in lst:
    if i<smallest:
        smallest=i
print(smallest)        

#question-6 count even numbers
lst=[2,7,4,9,6,11]
count=0
for i in lst:
    if i%2==0:
        count=count+1
print(count)        

#question-7 count odd numbers
lst=[2,7,4,9,6,11]
count=0
for i in lst:
    if i%2!=0:
        count=count+1
print(count)

#question-8 print only even numbers
lst=[10,15,22,31,44,51]
for i in lst:
    if i%2==0:
        print(i)

#question-9 print only odd numbers
lst=[10,15,22,31,44,51]
for i in lst:
    if i%2!=0:
        print(i)

#question-10 calculate average
lst=[10,20,30,40]
sum=0
for i in lst:
    sum=sum+i
    average=sum/len(lst)
print(average)  

#question-11 count number greater than 10
lst=[5,12,8,20,15,3]
count=0
for i in lst:
    if i>10:
        count=count+1
print(count)       

#question-12 print numbers greater than 10
lst=[5,12,8,20,15,3]
for i in lst:
    if i>10:
        print(i)

#question-13 count positive numbers
lst=[-2,5,-7,8,0,10] 
count=0
for i in lst:
    if i>0:
        count=count+1
print(count)   

#question-14 count negative numbers
lst=[-2,5,-7,8,0,-10]
count=0
for i in lst:
    if i<0:
        count=count+1
print(count)  

#question-15 sum of even numbers
lst=[2,5,8,11,14]
sum=0
for i in lst:
    if i%2==0:
        sum=sum+i
print(sum) 

#question-16 sum of odd numbers
lst=[2,5,8,11,14]
sum=0
for i in lst:
    if i%2!=0:
        sum=sum+i
print(sum)

#question-17 print elements in reverse order
lst=[10,20,30,40,50]
for i in range(len(lst)-1,-1,-1): # 
    print(lst[i])

#question-18 count how many times a number appears
lst=[2,5,2,8,2,10]
num=2
count=0
for i in lst:
    if i==num:
        count=count+1
print(count)   

#question-19 check whether a number exists
lst=[10,20,30,40,50]
num=30
found=False
for i in lst:
    if i==num:
        found=True
if found:
    print("found")
else:
    print("not found") 

#question-20 print square of every element
lst=[2,3,4,5]
for i in lst:
    print(i**2)               