       
#Q2 Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         if len(s)==len(t):
             a={}
             for i in s:
               a[i]=s.count(i)# creating a dict to store the count of each element
             for i in a:# iterating the dict to if same element count is there for the same element in the other string
               if a[i]!=t.count(i):
                   return False
             return True

         else:
             return False
  # TYPE 2
    #    return len(s)==len(t) and sorted(s)==sorted(t)
           return sorted(s)==sorted(t)