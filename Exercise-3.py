Questions=["What is name of Pakistans's PM : ", "What is Pakistans Age:  ","How many province Pakistan have"]
Answers=["IK", "75","5"]
i=0
win=0
while(i<3):
  print(Questions[i])
  ans=input("enter your answer :  ")
  if(ans==Answers[i]):
      win+=2000
      print("Correct Answer")
  else:
      print("Wrong Answer")


  i=i+1
print("your winning is :  ",win)
