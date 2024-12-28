Questions= [ """
What is the Name Of PM of Pakistan : 
 1) Imran Khan                 2) Asim Munir
 3)Nawaz Sharif                4)None
"""
            ,
"""
How many provinces Pakistan have :
 1) 5                2) 3
 3) 6              4) 4


""","""

When Pakistan got Liberation
1)1946                  2)1948
3)1947                  4)1944


"""
    
]
Answers=["1","1", "3"]
i=0
win=0
while(i<len(Questions)):
    print(Questions[i])
    ans=input("Enter The Option ")
    if(ans==Answers[i]):
        print("correct answer ")
        win=win+2000
    else:
        print("Wrong answer ")
    i=i+1
print("Your Total Win is ",win)
