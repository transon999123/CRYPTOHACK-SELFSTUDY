print(11%6) #5
print(8146798528947%17) #4

#Định lí nhỏ của Fermat: a^(p-1) = 1 (mod p) nếu p là số nguyên tố và a không chia hết cho p
#test 1:
print(pow(3,17,17)) #3
#test 2
print(pow(3,16,17)) #1
#flag:
print(pow(273246787654, 65536, 65537)) #1

#mũ ngược: trong miền xác định Fp, với mọi phần tử g có trong miền, luôn tồn tại một số d sao cho g^d = 1 (mod p) 
# => d tính bằng cách sử dụng pow(g, -1, p)

print(pow(3,-1,13)) #9