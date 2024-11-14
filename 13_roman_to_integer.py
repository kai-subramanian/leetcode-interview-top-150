
def romanToInt(s: str) -> int:
    romans={'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000}

    ans=0
    for i in range(0,len(s)-1):
        if s[i] in romans:
            if(romans[s[i]]<romans[s[i+1]]):
                ans-=romans[s[i]]
            else:
                ans+=romans[s[i]]
    return ans+romans[s[-1]]

print(romanToInt('MC'))