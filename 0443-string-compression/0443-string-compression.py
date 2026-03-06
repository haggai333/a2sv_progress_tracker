class Solution:
    def compress(self, chars: List[str]) -> int:
        s=""
        current=chars[0]
        count=0
        for i in chars:
            if i==current:
                count+=1
            else:
                s+=current
                if count>1:
                    s+=str(count)
                current=i
                count=1
        s+=current
        if count>1:
            s+=str(count)
        chars.clear()
        for i in s:
            chars.append(i)
            

        