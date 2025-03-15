nums=range(1,21)
evens=[x for x in nums if x%2==0]
odds=[x for x in nums if x%2!=0]
even_dict={x:x**2 for x in nums if x%2==0}
odd_dict={x:x**3 for x in nums if x%2!=0}
print("Evens:",evens)
print("Odds:",odds)
print("Even Dict:",even_dict)
print("Odd Dict:",odd_dict)
