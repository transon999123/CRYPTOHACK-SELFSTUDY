#SÔ DƯ TRUNG HOA
#Định lý: cho x%m1=a1, x%m2=a2, x%m3=a3,..., x%mn=an với m1,m2,...,mn là những số nguyên dương đôi một nguyên tố cùng nhau.
#Khi đó, ta có mô đun M=m1*m2*...*mn và hệ có nghiệm duy nhất là:
# x mod M = a1*M1*y1 + a2*M2*y2 + ... + an*Mn*yn
#với M1=M/m1, M2=</m2,..., Mn=M/mn, y1M1=1 mod m1, y2M2=1 mod m2,..., ynMn=1 mod mn

#exercise: x=2 mod 5, x=3 mod 11, x=5 mod 17, tìm a sao cho x=a mod 935

a1=2
a2=3
a3=5
m1=11*17
m2=5*17
m3=5*11 
y1=pow(m1,-1,5)
y2=pow(m2,-1,11)
y3=pow(m3,-1,17)
print((a1*m1*y1 + a2*m2*y2 + a3*m3*y3)%935)