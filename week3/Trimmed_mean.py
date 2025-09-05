#Wisdom of Crowd Computing
Estimate = []
i = 0
total = 0
while i <= 40 : 
   n = input(str(i)+". Enter your value:" )
   n = int(n)
   Estimate.append(n)
   i += 1

Estimate.sort()
print(Estimate)
TrimmedEstimate = Estimate[10:31]
print(TrimmedEstimate)

for i in TrimmedEstimate:
    total = total + i

print("Trimmed mean = "+ str(total/20))

