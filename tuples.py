tup = (1,2,3,4,"arslan")
print(type(tup))
# in tuple you can not modify the value once initialize 
# to make changes in tuple first we make it list then change
tep = list(tup)
tep.append(23)
tep[3]="mian"
tup=tuple(tep)
print(tup)
# we can also murge tupples