# list +-10
# 2 hodnoty pak prohodit

nums = []
for i in range(1,11):
    nums.append(i)
    print(nums)
while True:
    a = int(input("ktery prvek bude prvni, ktery chcete vymenit?"))
    b = int(input("ktery prvek bude druhy, ktery chcete vymenit"))

    if a!=b and a>=0 and b >=0 and a < len(nums) and b < len(nums):
        break 


