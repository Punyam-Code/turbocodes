#Q4 Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map(sorted,strs)
        lis={}
        for i in strs:# creating empty dict of sorted words by characters
            word=''.join(sorted(i))# join the characters of word broken into characters after sorting them
            if word in lis:# two sorted words are alrready in the dic join the word into the list at same location
                lis[word].append(i)
            else:# if not present  then create its new instance in the list
                lis[word]=[i]
        return lis.values()
