#You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

#Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.



def takeCharacters(s, k) -> int:
        ac=0
        bc=0
        cc=0
        for i in s:
            if i=='a':
                ac+=1
            elif i=='b':
                bc+=1
            elif i=='c':
                cc+=1
        if ac<k or bc<k or cc<k:
            return -1

        l=0
        r=0
        n=len(s)
        a=0
        b=0
        c=0
        ans=n
        while r<n:
            if s[r]=='a':a+=1
            if s[r]=='b':b+=1
            if s[r]=='c':c+=1
            r+=1
            while a>ac-k or b>bc-k or c>cc-k:
                if s[l]=='a':a-=1
                if s[l]=='b':b-=1
                if s[l]=='c':c-=1
                l+=1
            ans=min(ans,n-(r-l)) # update the size of sliding window
        return ans
    
print(takeCharacters("aabaaaacaabc",2))