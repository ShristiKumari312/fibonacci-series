num=[1,1]

for i in range(0,10):
  num.append(num[-1]+num[-2]) 
for i in num:
    print(i)
