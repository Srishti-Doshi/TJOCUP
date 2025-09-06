# Input → space-separated decimal numbers
# Process → apply floor (greatest integer ≤ number)
# Output → comma-separated integers
import math

weights_List = input("Enter weights as space-separated decimal numbers")
weights_List = weights_List.split(" ")
weights_List = list(weights_List)
integerlist = []
for item in weights_List:
   item = math.floor(float(item))
   integerlist.append(str(item))

print(integerlist)
print(",".join(integerlist))