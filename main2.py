arr = []
n = int(input("Enter array size:"))
while(n):
  num = int(input("Enter number:"))
  arr.append(num)
  n = n-1

res = 0
for i in arr:
  res = res ^ i
print("OddOccuring number is" , res)