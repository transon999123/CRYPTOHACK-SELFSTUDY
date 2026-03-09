ints=[588,665,216,113,642,4,836,114,851,492,819,237]

#đây là những số theo dạng pow(x,n,p) đến pow(x,n+11,p) với n tăng dần, p là số nguyên dương có ba chữ số.
#hãy tìm x và p
# giả sử p là số nguyên dương có ba chữ số, ta sẽ thử tất cả các giá trị của p từ 100 đến 999
for p in range(100,1000):
    for x in range(1,p):
        for n in range(0,50):
            if pow(x,n,p)==588 and pow(x,n+1,p)==665 and pow(x,n+2,p)==216 and pow(x,n+3,p)==113 and pow(x,n+4,p)==642 and pow(x,n+5,p)==4 and pow(x,n+6,p)==836 and pow(x,n+7,p)==114 and pow(x,n+8,p)==851 and pow(x,n+9,p)==492 and pow(x,n+10,p)==819 and pow(x,n+11,p)==237:
                print(x,n,p) 

#x=209 n=25 p=919
