x= int(input())
y= int(input())
highest=0
if x > y:
    print("first")
    highest=x
elif y>x:
    print('second')
    highest=y
else:
    print('same')
    highest=x=y
print('square=',highest*highest)
