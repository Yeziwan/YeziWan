#五个知识点，and, or ,not, in, not in
a,b=5,7
print('------------and和------------')
print(a==5 and b==7)#对和对，结果对
print(a<5 and b==7)#对和错，结果错
print(a==5 and b>8)
print(a!=5 and b!=7)#错和错，结果错

print('------------or或-------------')
print(a==5 or b==7)#对或对，结果对
print(a==5 or b==8)
print(a<6 or b>9)#对或错，结果对
print(a<5 or b<5)#错或错，结果错

print('------------not-----------')
print(not (a==5 or b==7))
print(not (a!=5 and b!=7))

print('------------in-----------')
c='wanjiaqiwuyuan'
print('w' in c )
print('k' in c )
print('a' not in c)
print('k' not in c)
