galletita=float(input("cantidad galletita"))*1000
queso=float(input("cantidad queso"))*1000
dulce=float(input("cantidad dulce"))*1000

tg=galletita//450
tq=queso//250
td=dulce//125
print(" tg: ",tg," tq: ",tq," td: ",td)

if tg<tq and tg<td:
    print("tg es ",tg)
else:
    if tq<tg and tq<td:
         print("tq es ",tq)
    else:
         print("td es ",td)
              
