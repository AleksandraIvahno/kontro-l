i = int (input("Ievadi cik ir "))
sum_ = 0
len_ = 0
while i>0:
  al = int(input("Ievadi vienu atzīmi "))
  i = i-1
  sum_+=i-1
  len_+=1
print(sum_/len_)