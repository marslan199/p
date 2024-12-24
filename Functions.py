
# parametrized function 
def calculate(a,b):
    gmean=(a*b)+(a**2)
    print(gmean)
# unparametrized function
def isgreater():
    a=2
    b=2345
    if(a>b):
        print(a," is gretaer ")
    else:
        print(b," is greater")

def islesser(a,b):
    # if you want that you initializa body of function later use keyword 
 pass
# function with default values 
def default(a=2,b=13):
   print(a,b)
def nums(*number): # *numbers provide a kind of list 
   sum=0
   for i in number:
      sum=sum+i
   return sum
a=10
b=20
calculate(a,b)
isgreater()
default( b=10) #here it take default a value
default( ) # here both are default
default( 12) # here b has default value '
z = nums(4,5,9,2)
print("is ans sjjnd",z)

