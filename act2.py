a={1,2,3}
b={"a","b","c"}
c=list(zip(a,b))
print(c)


e=[10,20,30,40]
f=[100,200,300,400]
for x,y in zip(e,f[::-1]):
    print(x , y)


stock=["relience","infosys","tcs"]
price=[123,2123,3134]
new_dict={stock: price for stock,price in zip(stock,price)}
print(new_dict)
