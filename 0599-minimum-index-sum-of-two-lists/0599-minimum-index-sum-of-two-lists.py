class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        answer=[]
        tempdic={}
        mini=99999
        for i in list1:
            if i in list1 and i in list2 and i not in tempdic:
                tempdic[i]=list1.index(i)+list2.index(i)
        for i in tempdic:
            mini=min(mini,tempdic[i])
        for i in tempdic:
            if tempdic[i]==mini:
                answer.append(i)
        return answer




        



            