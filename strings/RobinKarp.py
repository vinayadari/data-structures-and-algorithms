#RABIN KARP EXP - 3
d = 256 
def search(pat,txt,q):
    m=len(pat)
    n=len(txt)
    i=j=p=t=0
    h=1
    for i in range(m-1): h=(h*d)%q
    for i in range(m):
        p=(d*p+ord(pat[i]))%q
        t=(d*t+ord(txt[i]))%q
    for i in range(n-m+1):
        if p==t:
            print("Pattern found at index: "+str(i))
        if i<n-m:
            t=(d*(t-(ord(txt[i])*h))+ord(txt[i+m]))%q
            if t<0: t+=q    

txt = "GEEKS FOR GEEKS"
pat = "GEEK"
q = 11
search(pat, txt, q)