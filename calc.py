import math
bubble = 7.97469162940979
bubble2 = 7.774115800857544
bubble21 = 15.024044513702393

quick = 0.027555465698242188
quick2 =  0.027975797653198242
quick21 = 0.059162139892578125

merge = 0.06773900985717773
merge2 = 0.08680391311645508
merge21 = 0.13428521156311035

def nlogn(x):
  return  math.log2(x ** x)

def bubble_sort(b):
  return b * 4, b * 25

def quick_sort(q):
  return q * nlogn(2), q * nlogn(5)

def merge_sort(m):
  return m * nlogn(2), m * nlogn(5)

print(bubble_sort(bubble2))
print(quick_sort(quick2))
print(merge_sort(merge2))

