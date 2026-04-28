nums = list(range(1,21))
licha = []
suda = []

for num in nums:
    if num % 2 == 0:
        suda.append(num)
    else:
        licha.append(num)

print("licha:",licha)
print("suda:",suda)

