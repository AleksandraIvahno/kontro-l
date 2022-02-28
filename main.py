a = float(input("Ievadiet jūsu svaru(N): "))
b = float(input("Ievadiet jūsu svaru(N): "))
c = float(input("Ievadiet jūsu svaru(N): "))
x = a* 0.10197
y = b* 0.10197
z = c* 0.10197
print("Jūsu masa ir", round(x,2))
print("Jūsu masa ir", round(y,2))
print("Jūsu masa ir", round(z,2))
d = [x,y,z]
print("Jūsu kopēja masa ir", round(sum(d),2))
print("Jūsu kopēja masa ir", round(sum(d)/len(d),2))
if sum(d)<300:
  print("Jūs varat braukt ar liftu")
else:
  print("Jūs nevarat braukt ar liftu")