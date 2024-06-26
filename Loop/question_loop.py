#question 1 
list = [1,4,9,16,25,36,49,64,81,100]
for nums in list:
   print(nums)

#question 2
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
s = 100

idx = 0
for el in list:
    if el == s:
        print("number found at idx", idx)
    idx += 1
