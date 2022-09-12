
"""
費式25項和
"""

def fas(n):
    if n < 2:
        return n
    else:
        return fas(n-1)+fas(n-2)

new_num = []

num = int(input("請輸入幾項:"))

for i in range(num):
    new_num.append(fas(i))
    
    
total = sum(new_num)
print(total)

"""
費式25項除和
"""

def fas(n):
    if n < 2:
        return n
    else:
        return fas(n-1)+fas(n-2)

new_num = []

num = int(input("請輸入幾項:"))

for i in range(num):
    if fas(i-1) == 0:
        continue
    else:
        new_num.append(fas(i)/fas(i-1))
    
total = sum(new_num)
print(round(total,2))
