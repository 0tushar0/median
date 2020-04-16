# get median of 2 sorted arrays

nums1 = [1,3]
nums2 = [2,4]

c = nums1 + nums2
c.sort()
s = len(c)

if s % 2 == 1:
    print(c[(int)(s/2)])
else:
    print((c[(int)(s/2)] + c[(int)(s/2) - 1]) / 2)