# -*- coding: utf-8 -*-
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
# a = [10,4,5,1,3,-1,4,6]
# quickSort(a,0,len(a)-1)
# print(a)

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
# def func(a, b):
#     def line(x):
#         nonlocal a
#         a = 5
#         return a * x - b

#     return line


# line = func(2, 3)
# print(line(5))

# class Solution:
#     def countBalls(self, lowLimit, highLimit):
#         res = float("-inf")
#         nums = collections.defaultdict(int)
#         for ball in range(lowLimit,highLimit+1):
#             ball_num = sum(map(int,str(ball)))
#             nums[ball_num] += 1
#         return max(nums.values())
# class Solution:
#     def restoreArray(self, adjacentPairs):
#         # u,v = adjacentPairs[0]
#         # res = adjacentPairs[0]
#         # del adjacentPairs[0]
#         # deque = collections.deque()
#         # deque.append(u)
#         # deque.append(v)
#         # while deque and adjacentPairs:
#         #     tmp = deque.popleft()
#         #     flag = 0
#         #     index = res.index(tmp)
#         #     for pair_index,pair in enumerate(adjacentPairs):
#         #         if pair[0] == tmp or pair[1] == tmp:
#         #             tmp_2 = pair[1] if pair[0] == tmp else pair[0]
#         #             flag = 1
#         #             break
#         #     if flag:
#         #         if not index:
#         #             res = [tmp_2] + res
#         #         else:
#         #             res.append(tmp_2)
#         #         del adjacentPairs[pair_index]
#         #         deque.append(tmp_2)
#         # return res
#         adjacent_dict = collections.defaultdict(list)
#         for pair in adjacentPairs:
#             adjacent_dict[pair[0]].append(pair[1])
#             adjacent_dict[pair[1]].append(pair[0])
#         start = adjacentPairs[0][0]
#         deque = collections.deque()
#         deque.append(start)
#         res = [start]
#         visited = set()
#         visited.add(start)
#         while deque:
#             tmp = deque.popleft()
#             index = res.index(tmp)
#             tmp_nb = adjacent_dict[tmp]
#             if len(tmp_nb) == 1 and tmp_nb[0] not in res:
#                 if not index:
#                     res = tmp_nb + res
#                 else:
#                     res += tmp_nb
#                 for i in tmp_nb:
#                     if i not in visited: deque.append(i)
#                     visited.add(i)
#             elif len(tmp_nb) == 2:
#                 if tmp_nb[0] in res and tmp_nb[1] not in res:
#                     res = res + [tmp_nb[1]] if tmp_nb[0] == res[index-1] else [tmp_nb[1]] + res
#                 elif tmp_nb[1] in res and tmp_nb[0] not in res:
#                     res = res + [tmp_nb[0]] if tmp_nb[1] == res[index-1] else [tmp_nb[0]] + res
#                 elif tmp_nb[0] not in res and tmp_nb[1] not in res:
#                     res = [tmp_nb[0]] + res + [tmp_nb[1]]
#                 for i in tmp_nb:
#                     if i not in visited: deque.append(i)
#                     visited.add(i)
#         return res

# class Solution:
#     def canEat(self, a, queries):
#         # res = []
#         # favoriteTypei, favoriteDayi, dailyCapi = queries[24]
#         # candyNums = sum(candiesCount[i] for i in range(favoriteTypei))
#         # ability_l = (favoriteDayi)*dailyCapi
#         # ability_h = candyNums + candiesCount[favoriteTypei]
#         # if candyNums > ability_l or ability_h <= favoriteDayi: res.append(False)
#         # else: res.append(True)
#         # return res
#         n = len(a)
#         accum = [a[0]] * n
#         for i in range(1, n):
#             accum[i] = accum[i - 1] + a[i]
#         ans = [False] * len(queries)
#         for idx, (i, day, cap) in enumerate(queries):
#             if i > 0 and accum[i - 1] >= (day + 1) * cap:
#                 continue
#             if day >= accum[i]:
#                 continue
#             ans[idx] = True
#         return ans[24]
# sol = Solution()
# print(sol.canEat([46,5,47,48,43,34,15,26,11,25,41,47,15,25,16,50,32,42,32,21,36,34,50,45,46,15,46,38,50,12,3,26,26,16,23,1,4,48,47,32,47,16,33,23,38,2,19,50,6,19,29,3,27,12,6,22,33,28,7,10,12,8,13,24,21,38,43,26,35,18,34,3,14,48,50,34,38,4,50,26,5,35,11,2,35,9,11,31,36,20,21,37,18,34,34,10,21,8,5],[[80,2329,69],[14,1485,76],[33,2057,83],[13,1972,27],[11,387,25],[24,1460,47],[22,1783,35],[1,513,33],[66,2124,85],[19,642,26],[15,1963,79],[93,722,96],[15,376,88],[60,1864,89],[86,608,4],[98,257,35],[35,651,47],[96,795,73],[62,2077,18],[27,1724,57],[34,1984,75],[49,2413,95],[76,1664,5],[28,38,13],[85,54,42],[12,301,3],[62,2016,29],[45,2316,37],[43,2360,28],[87,192,98],[27,2082,21],[74,762,37],[51,35,17],[73,2193,4],[60,425,65],[11,1522,58],[21,1699,66],[42,1473,5],[30,2010,48],[91,796,74],[82,2162,31],[23,2569,65],[24,684,23],[70,1219,51],[5,1817,15],[81,2446,34],[96,771,60],[49,1171,60],[41,567,67],[39,799,59],[90,957,81],[84,2122,27],[82,1707,44],[11,1889,20],[80,1697,83],[24,1786,60],[90,1847,99],[51,114,21],[44,466,85],[56,469,20],[44,350,96],[66,1946,10],[14,2470,12],[69,1175,18],[98,1804,25],[77,2187,40],[89,2265,45],[19,2246,45],[40,2373,79],[60,2222,17],[37,385,5],[97,1759,97],[10,903,5],[87,842,45],[74,2398,66],[62,49,94],[48,156,77],[76,2310,80],[64,2360,95],[70,1699,83],[39,1241,66],[92,2312,21],[63,2148,29],[95,594,74],[89,90,51],[82,137,70],[54,301,97],[15,819,43],[47,1402,60],[17,2377,43],[50,1937,95],[62,1174,74],[67,1411,87],[39,1151,48]]))

# import time
# def timer(function):
#     """
#     装饰器函数timer
#     :param function:想要计时的函数
#     :return:
#     """

#     def wrapper(*args, **kwargs):
#         time_start = time.time()
#         res = function(*args, **kwargs)
#         cost_time = time.time() - time_start
#         print("【%s】运行时间：【%s】秒" % (function.__name__, cost_time))
#         return res

#     return wrapper


# @timer
# def test(n):
#     sum = 0
#     for i in range(n + 1):
#         sum += i
#     return sum

# if __name__ == '__main__':
#     test(10000000)


# class Solution(object):
#     def characterReplacement(self, s, k):
#         """
#         :type s: str
#         :type k: int
#         :rtype: int
#         """
#         N = len(s)
#         left, right = 0, 0 # [left, right] 都包含
#         counter = collections.Counter()
#         res = 0
#         while right < N:
#             counter[s[right]] += 1
#             while right - left + 1 - counter.most_common(1)[0][1] > k:
#                 counter[s[left]] -= 1
#                 left += 1
#             res = max(res, right - left + 1)
#             right += 1
#         return res
# sol = Solution()
# print(sol.characterReplacement("AABABBA",1))

a = b = 1
print(id(a),id(b))
a = 2
print(id(a),id(b))
