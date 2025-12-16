# Print Fibonacci series up to n terms

n_terms = 10

# First two terms
n1, n2 = 0, 1
count = 0

print(f"Fibonacci sequence upto {n_terms} terms:")

if n_terms <= 0:
   print("Please enter a positive integer")
elif n_terms == 1:
   print(f"Fibonacci sequence upto {n_terms}:")
   print(n1)
else:
   while count < n_terms:
       print(n1, end=" ")
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
print()
