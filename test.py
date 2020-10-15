Q=int(input('請輸入Q值='))
W=int(input('請輸入W='))
Qout=1
Wout=1
out=1
for i in range(Q,1,-1):
    Qout=Qout*i
for g in range(W,1,-1):
    Wout=Wout*g
out=Qout*Wout
print('%s%d'%('Q!乘以W!是',out))