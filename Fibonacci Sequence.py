# adapted and altered from python mainframe website

def fib(n):

   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))

terms = int(input("How many terms? "))

if terms <= 0: # error checking methods
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(terms):
       print(fib(i)) # input the integer of terms in fib(i) which recurses "terms" number of times

       

       
