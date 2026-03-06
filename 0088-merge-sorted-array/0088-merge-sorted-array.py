class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l=0
        r=0
        answer=[]
        while l<n or r<m:
            if l<n and r<m:
                if nums2[l]>nums1[r]:
                    answer.append(nums1[r])
                    r+=1
                    continue
                else:
                    answer.append(nums2[l])
                    l+=1
                    continue

            if r<m:
                answer.append(nums1[r])
                r+=1

            if l<n:
                answer.append(nums2[l])
                l+=1
        nums1.clear()
        for i in answer:
            nums1.append(i)
        

        
        
        