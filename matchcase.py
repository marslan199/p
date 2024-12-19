a=int(input("ENTER NUMBER "))
match a:
    case 0:
        print("NUM IS 0")
    case 5:
        print("NUM IS 5")
    # to print default value use _ 
    case _ if a!=10:
        print(a)
        
    case _ if a>10 and a<20:
        print("BETWEEN 10 AND 20")

