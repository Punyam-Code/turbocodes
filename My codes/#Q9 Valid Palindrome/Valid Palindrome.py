#Q9 Valid Palindrome
 
 class Solution:
    def isPalindrome(self, s: str) -> bool:
         #type 1 cons using built in function and using extra memory by creating new strings
        # st=""
        # for i in s:
        #     if i.isalnum():
        #         st=st+i.lower()
        # return st==st[::-1]


        #Type 2
        l=0
        r=len(s)-1
        while l<r:
            #using self if we want to call function inside of an object
            while l<r and not self.alphanum(s[l]):
                l=l+1
            while r>l and not self.alphanum(s[r]):
                r=r-1
            if s[l].lower()!=s[r].lower():
                print(s[l],s[r])
                return False
            l=l+1
            r=r-1
        return True
    def alphanum(self, c):
        # ord is used to check ascii value in python
        return (ord('A')<=ord(c)<=ord('Z') or ord('a')<=ord(c)<=ord('z') or ord('0')<=ord(c)<=ord('9'))
            