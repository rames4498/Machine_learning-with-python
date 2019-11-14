m = input("please provide valid mailid: ")
n = input("please provide valid mailpwd: ")
a = 0
spec =  "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
spec = list(spec)
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
    if h == "@":
        r = m.index(h)
        for l in range(r,len(m)):
            if m[l] == ".":
                print("Valid emailid")
                password()
                break
            else:
                a = a+1
                if a == (len(m)-r):
                    print("Invalid emailid")
                
    

                        
