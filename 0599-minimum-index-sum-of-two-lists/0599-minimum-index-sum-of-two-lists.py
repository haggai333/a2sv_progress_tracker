class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        answer=[]
        tempdic={}
        mini=99999
        for i in range(len(list1)):
            if list1[i] in list1 and list1[i] in list2 and list1[i] not in tempdic:
                tempdic[list1[i]]=i
        for i in range(len(list2)):
            if list2[i] in tempdic:
                tempdic[list2[i]]+=i
        
        for i in tempdic:
            mini=min(mini,tempdic[i])
        for i in tempdic:
            if tempdic[i]==mini:
                answer.append(i)
        return answer




        



            