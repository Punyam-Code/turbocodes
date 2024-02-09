#Q6 Product of Array Except Self
#input =[1,2,3,4]
#prefix array=[1,2,6,24]
#prefix calculation 1*1=1,1*2=2,2*3=6,6*4=24
#postfix array=[24,24,12,4]
#postfix calculation is in reverse order 4*1=1,4*3=12,12*2=24,24*1=24
#resultant array=[24,12,8,6]
#resultant array calculation prefix of current value * postfix of current index value i.e 
#0th index -1th index value prefix =1*0th index suffix value =24 (1*24)=24,
#1st index value 0th index value prefix =1 * 1st index value suffix =12 (1*12)=12,
#2nd index value 1st index value prefix =2 * 2nd index value suffix =4 (2*4)=8,
#3rd index 2nd index value prefix=  =6* 3rd index suffix value =1 if not exist (6*1)=6,
n=len(nums)
r=[0]*n
prefix_value=1
suffix_value=1
for i in range(n):
    r[i]=prefix_value
    prefix_value=prefix_value*nums[i]
for i in range(n-1,-1,-1):
    r[i]=suffix_value*r[i]
    suffix_value=suffix_value*nums[i]
return r