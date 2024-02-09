#Q5 Top K Frequent Elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:# create the dict which have count of each element 
            if i in dic:
                dic[i]=dic[i]+1
            else:
                dic[i]=1
        # dic={k: v for k, v in sorted(dic.items(), key=lambda item: item[1],reverse=True)}
        dic = sorted(dic.items(), key=lambda x:x[1],reverse=True)# sort the dict based on values in reverse order print top required number of element
        lis=[]
        for i in range(k):
            lis.append(dic[i][0])
        return lis