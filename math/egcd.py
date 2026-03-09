p = 26513
q = 32321

g = 1 # gcd of two different primes

# note that as p*u + q*v = g
# q*v = g (mod p)
# v = g/q (mod p)

v = pow(q,-1,p)
v -= p # subtract p to make v negative 
u = (g - (q*v))//p

print(u,v)

#giải tay đi má, code lụm trên mạng chứ giải tay cũng ra
#-8404