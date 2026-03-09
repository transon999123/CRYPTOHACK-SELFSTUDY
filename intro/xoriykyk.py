from pwn import *
a='0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
b= bytes.fromhex(a)


#hint from the problem: remember the flag format => 'crypto{'
c='crypto{'
d=bytes(c,'utf-8')
print(xor(b,d))
#b'myXORke+y_Q\x0bHOMe$~seG8bGURN\x04DFWg)a|\x1dTM!an\x7f'

e='myXORkey'
f=bytes(e,'utf-8')
print(xor(b,f))
#b'crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}'
