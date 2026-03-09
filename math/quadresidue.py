#THẶNG DƯ BẬC HAI MODULO
#ví dụ: cho modulo p=19, a=11
# ta có pow(a,2,p)=5
#=> căn bậc hai của 5 là 11 với modulo 19 (wtf lmao :))))))))))

#=> 5 là thặng dư bậc hai (quadratic residue) vì nó tồn tại một số a sao cho pow(a,2,p)=5
#vậy trường hợp không tồn tại một số a nào thì sao? => số đó không là thặng dư bậc hai (quadratic non-residue)

#bài tập: cho p=29 và ba số a=[14,6,11], hai trong ba số a là những thặng dư không bậc hai, hãy tìm số còn lại là thặng dư bậc hai

p = 29
a = [14,6,11]

for i in a:
    for j in range(1,p):
        if pow(j,2,p)== i:
            print(i) #tìm quadratic residue, a=6
            print(j) #tìm j, j=8



