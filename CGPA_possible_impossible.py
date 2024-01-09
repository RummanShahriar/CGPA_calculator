credit = float(input("Enter your Completed credits here:"))
cpc = 3 # cpc = credit_per_course

now_cg = float(input("Enter your current CGPA:"))
now_number = now_cg * (credit/cpc)

store = credit/cpc
now_credit = credit/cpc

# to_get goal
target_cgpa = float(input("Enter your TARGET cgpa here:"))

while True :
    cg = now_number/now_credit
    if cg == target_cgpa or cg > target_cgpa or  now_credit > 45 :
        break
    else :
        now_number += 4
        now_credit += 1

if now_credit > 45 :
  print("Impossible")
else :
  print(f"To achieve the goal {now_credit-store} more courses needs to be completed with a cg-4.00")