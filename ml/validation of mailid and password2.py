m = input("please provide valid mailid: ")
n = input("please provide valid mailpwd: ")
a = 0
spec =  "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
spec = list(spec)
flag = True

def password():
    k,c,d,j = 0,0,0,0
    for b in n:
        if b.isupper():
            k = k+1
        if b.islower():
            c = c+1
        if b.isdigit():
            d = d+1
        if (k and c and d)>0:
            break
    for s in spec:
        if s in n:
            j = j+1
    if (5<len(n)<15) and ((k and c and d and j) > 0):
        print("Valid password")
    else:
        print("Invalid password")     
for h in m:
    if ((h == "@") & (m[0] != ".") & (m[0] not in spec) & (m[-1] not in spec)):
        flag = False
        r = m.index(h)
        #for l in range(r+2,len(m)):
        if (("@" in m[r:]) & (m[r+1] != ".")):
            #if (m[l] == "."):
                print("Valid emailAdress")
                password()
                break
        else:
            print("Invalid emailAdress")
    
if flag == True:
  print("Invalid emailAdress")
