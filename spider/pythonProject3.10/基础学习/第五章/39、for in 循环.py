# for b in range(0,10):
#     print(b)
# a=range(2,101,2)
# print(sum(a))
sum=0
for a in range(2,101,2):
    sum+=a
print(sum)

sum=0
for c in range(1,101):
    if c%2==0:
        sum+=c
    else:
        c+=1
print(sum)