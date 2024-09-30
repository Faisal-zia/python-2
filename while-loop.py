count = 1
while count <= 5 :
    print("Faisal-zia", count)
    count += 1

print("loop-ended")

# reversed

i = 5
while i >= 1:
    print("mohid-zia", i)
    i -= 1
    
print("reversed-ended")

# exercise
# 1
# print number 100 to 1
i = 100
while i >= 1:
  print(i)
  i -= 1

# print multiplication table of number n
i = 1
while i <= 10:
  print(3*i)
  i += 1
  
  # print the element of fo;;owing list in a loop
nums = [1,4,9,16,25,56,87,91,100]
idx = 0
while idx < len(nums) :
     print(nums[idx])
     idx += 1
     
     
# search a number X in tuples using loop
num1 = (1,4,9,16,36,56,87,91,100)

x = 36
i = 0
while i < len(num1):
    if (num1[i] == x):
      print("founded at idx", i) 
    else: 
        print("finding...")
    i += 1
    # break concept 
    
    nums1 = 1
    while nums1<= 5:
        print(nums1)
    if(nums1 == 3):
             break
    nums1 += 1