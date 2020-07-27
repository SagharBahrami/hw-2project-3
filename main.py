# Exercise No.2
# Programmer:    Saghar Bahrami
# Date:          June 21, 2020
#
def main():
  sum = 0
  print("This program computes the avrage of two exam scores!")
  numOfExam = eval(input("Enter the number of exam scores to be averaged:"))
  for i in range (0,numOfExam):
   print("Enter score", (i+1),":", end = ' ')
   score = eval(input(" "))
   print()
   sum = sum + score
  print()
  print()
  average = sum / numOfExam
  print("The average of the scores is:", average)
main()