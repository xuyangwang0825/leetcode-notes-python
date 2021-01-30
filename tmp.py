import collections
import numpy as np
# class Solution:
#     def minimumTeachings(self, n, languages, friendships):
#         records = []
#         for friend_a,friend_b in friendships:
#             flag = 0
#             for language in languages[friend_a-1]:
#                 if language in languages[friend_b-1]:
#                     flag = 1
#                     break
#             if not flag: records.append([friend_a,friend_b])
#         print(records)
#         res = float('inf')
#         for language in range(1,n+1):
#             languages_tmp = languages
#             tmp = 0
#             for friend_a,friend_b in records:
#                 if language not in languages_tmp[friend_a-1]:
#                     tmp += 1
#                     languages_tmp[friend_a-1].append(language)
#                 if language not in languages_tmp[friend_b-1]:
#                     tmp += 1
#                     languages_tmp[friend_b-1].append(language)
#             res = min(tmp,res)
#         return res

# class Solution:
#     def decode(self, encoded):
#         num = len(encoded)+2
#         arr = [1] + [0]* (num-2)
#         i = 0
#         while i < num-2:
#             arr[i+1] = encoded[i] ^ arr[i]
#             if arr[i+1] < 1 or arr[i+1] > num-1:
#                 arr[0] += 1
#                 i = 0
#             i += 1
#         return arr

# class Solution:
#     def maximumTime(self, time):
#         time = list(time)
#         if time[0] == '?':
#             time[0] = '2' if time[1] in ('0','1','2','3') else '1'
#         if time[1] == '?':
#             time[1] = '9' if time[0] in ('0','1') else '3'
#         if time[3] == '?': time[3] = '5'
#         if time[4] == '?': time[4] = '9'
#         return "".join(time)

# class Solution:
#     def minCharacters(self, a, b):
#         res = float('inf')
#         char_count_a = collections.Counter(a)
#         char_count_b = collections.Counter(b)
#         print(char_count_a)
#         print(char_count_b)
#         mina,minb,maxa,maxb = 'z','z','a','a'
#         count_1,count_2,count_3,count_4 = 0,0,0,0
#         for c in a:
#             mina = min(mina,c)
#             maxa = max(maxa,c)
#         for c in b:
#             minb = min(minb,c)
#             maxb = max(maxb,c)
#         # print(mina,minb,maxa,maxb)

#         for c in a:
#             if c <= maxb: count_1 += 1 # ada
#             if c >= minb: count_2 += 1  # axiao
#         for c in b:
#             if c <= maxa: count_3 += 1 # ada
#             if c >= mina: count_4 += 1  # axiao
#         # print(count_1,count_2,count_3,count_4)
#         count_5 = float('inf')
#         i,j = char_count_a.most_common(1)[0],char_count_b.most_common(1)[0]
#         if i[0] == j[0]: count_5 = len(a) + len(b) - i[1] - j[1]
#         # while Counter[0]
#         return min(res,count_1,count_2,count_3,count_4,count_5)


# sol = Solution()
# print(sol.minCharacters("e","e"))

# def partition(arr, low, high):
#     i = (low-1)
#     pivot = arr[high]
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i = i+1
#             arr[i], arr[j] = arr[j], arr[i]

#     arr[i+1], arr[high] = arr[high], arr[i+1]
#     return (i+1)


# def quickSort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quickSort(arr, low, pi-1)
#         quickSort(arr, pi+1, high)


# def quickSort(array):
#     if len(array) < 2: return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i < pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quickSort(less) + [pivot] + quickSort(greater)


# def mergeSort(low,high):
#     if low == high: return [arr[low]]
#     if low + 1 == high: return [arr[high],arr[low]] if arr[low] > arr[high] else [arr[low],arr[high]]
#     mid = (low + high) // 2
#     partA = mergeSort(low,mid-1)
#     partB = mergeSort(mid,high)
#     i,j = 0,0
#     tmp = []
#     while i < len(partA) and j < len(partB):
#         if partA[i] <= partB[j]:
#             tmp.append(partA[i])
#             i += 1
#         else:
#             tmp.append(partB[j])
#             j += 1
#     if i == len(partA):
#         tmp += partB[j:]
#     else:
#         tmp += partA[i:]
#     return tmp

# arr = list(np.random.randint(100,size = 15))
# print(arr)
# n = len(arr)
# print(mergeSort(0,n-1))

# KMP
# class Solution:
#     def strStr(self, haystack,needle):
#         def KMP(s, p):
#             nex = getNext(p)
#             i = 0
#             j = 0
#             while i < len(s) and j < len(p):
#                 if j == -1 or s[i] == p[j]:
#                     i += 1
#                     j += 1
#                 else:
#                     j = nex[j]

#             if j == len(p):
#                 return i - j
#             else:
#                 return -1

#         def getNext(p):
#             nex = [0] * (len(p) + 1)
#             nex[0] = -1
#             i = 0
#             j = -1
#             while i < len(p):
#                 if j == -1 or p[i] == p[j]:
#                     i += 1
#                     j += 1
#                     nex[i] = j
#                 else:
#                     j = nex[j]

#             return nex
#         return KMP(haystack, needle)

# sol = Solution()
# print(sol.strStr("1233dasabcasaftqersegas","abc"))
def func(a, b):
    def line(x):
        nonlocal a
        a = 5
        return a * x - b

    return line


line = func(2, 3)
print(line(5))