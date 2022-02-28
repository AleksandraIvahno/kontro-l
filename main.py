a = int(input("Līdz kuram skaitlim: "))
s = 0
for i in range(1, a+1, 2):
  s = i + s
print("Summa ir", s)