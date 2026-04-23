class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index=0
        l=0
        r=len(letters)-1
        
        if ord(letters[r])<=ord(target):
            return letters[0]
        while r>=l:
            mid=(r+l)//2
            
            if ord(letters[mid])>ord(target):
                r=mid-1
            else:
                l=mid+1
            
        return letters[l]

        