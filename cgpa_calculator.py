# -*- coding: utf-8 -*-
"""CGPA calculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G18CmPx3MXo88MHQr93L5Vx68nkVGw2W
"""

credit = float(input("Enter your Completed credits here:"))
cpc = 3 # cpc = credit_per_course
now_cg = float(input("Enter your current CGPA:"))
course_taken = int(input("Enter the number of course taken this semster:"))
# Calculation #
sum = 0
for i in range(course_taken) :
  x = float(input(f"Enter the grade that you think you will get in course {i+1}:"))
  sum += x
course = credit/cpc
a = course*now_cg
sum += a
div = sum / (course + course_taken)
print()
print("Your cgpa will be:",div)