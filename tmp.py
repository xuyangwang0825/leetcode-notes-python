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

# a = b = 1
# print(id(a),id(b))
# a = 2
# print(id(a),id(b))

# class Solution:
#     def minCharacters(self, a: str, b: str) -> int:
#         res = float('inf')
#         char_count_a = collections.Counter(a)
#         char_count_b = collections.Counter(b)
#         # print(char_count_a)
#         # print(char_count_b)
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
#         count_5 = len(a) + len(b) - max(cc.values())
#         # while Counter[0]
#         # print(count_1,count_2,count_3,count_4,count_5)
#         return min(res,count_1,count_2,count_3,count_4,count_5)

# class Solution:
#     def minCharacters(self, a: str, b: str) -> int:
#         baset = 0
#         ca, cb = collections.Counter(a), collections.Counter(b)
#         cc = ca + cb
#         baset = len(a) + len(b) - max(cc.values())
#         for max_s in 'abcdefghijklmnopqrstuvwxy' :
#             base_a, base_b = 0, 0
#             for c in ca :
#                 if c > max_s :
#                     base_a += ca[c] # a <= ms, b > ms
#                 else :
#                     base_b += ca[c] # a > ms, b <= ms
#             for c in cb :
#                 if c > max_s :
#                     base_b += cb[c] # a <= ms, b > ms
#                 else :
#                     base_a += cb[c] # a > ms, b <= ms
#             baset = min(baset, base_a, base_b)
#         return baset

# class Solution:
#     def maxAbsoluteSum(self, nums):
#         n = len(nums)
#         dp = [[0 for i in range(n)] for j in range(n)]
#         for i,num in enumerate(nums):
#             dp[i][i] = num
#         for i in range(n):
#             for j in range(i+1,n):
#                 dp[i][j] = dp[i][j-1] + nums[j]
# #        return max(max(dp),-min(dp))
#         res = float("-inf")
#         for i in dp:
#             tmp1 = max(i)
#             tmp2 = -min(i)
#             res = max(res,tmp1,tmp2)
#         return res

# sol = Solution()
# print(sol.maxAbsoluteSum([1,-3,2,3,-4]))

# class Solution:
#     def minimumLength(self, s: str) -> int:
#         while len(s) > 1 and s[0] == s[-1]:
#             l,r = 0,len(s)-1
#             while l+1 < len(s) and s[l+1] == s[l]: l += 1
#             while r-1 >= 0 and s[r-1] == s[r]: r -= 1
#             if not l < r: s = s[1:-1]
#             else: s = s[l+1:r]
#         return s

# class Solution:
#     def maximumScore(self, a, b, c):
#         res = 0
#         while (a > 0 and b > 0) or (b > 0 and c > 0) or (a > 0 and c > 0):
#             can1 = max(a,b,c)
#             if can1 == a:
#                 a -= 1
#                 if b < c:
#                     c -= 1
#                 else: b -= 1
#             elif can1 == b:
#                 b -= 1
#                 if a < c:
#                     c -= 1
#                 else: a -= 1
#             else:
#                 c -= 1
#                 if a < b:
#                     b -= 1
#                 else: a -= 1
#             res += 1
#         return res

# sol = Solution()
# print(sol.maximumScore(1,8,8))

# class Solution:
#     def largestMerge(self, word1, word2):
#         res = ""
#         while word1 and word2:
#             if word1[0] > word2[0]:
#                 res += word1[0]
#                 word1 = word1[1:]
#             elif word1[0] < word2[0]:
#                 res += word2[0]
#                 word2 = word2[1:]
#             else:
#                 i,j = 0,0
#                 while i+1 < len(word1) and word1[i] == word1[i+1]:
#                     i += 1
#                 while j+1 < len(word2) and word2[j] == word2[j+1]:
#                     j += 1
#                 if i+1 == len(word1) and j+1 == len(word2):
#                     return res + word1 + word2
#                 if i+1 == len(word1) and not j+1 == len(word2):
#                     if word2[j+1] > word1[0]:
#                         res += word2[:j+2]
#                         word2 = word2[j+2:]
#                     else:
#                         res += word1
#                         word1 = ""
#                         continue
#                 if not i+1 == len(word1) and j+1 == len(word2):
#                     if word1[i+1] > word2[0]:
#                         res += word1[:i+2]
#                         word1 = word1[i+2:]
#                     else:
#                         res += word2
#                         word2 = ""
#                         continue
#                 if word1[i+1] > word2[j+1]:
#                     res += word1[:i+2]
#                     word1 = word1[i+2:]
#                 elif word1[i+1] < word2[j+1]:
#                     res += word2[:j+2]
#                     word2 = word2[j+2:]
#                 else:
#                     res += word1[:i+1]
#                     word1 = word1[i+1:]
#                     res += word2[:j+1]
#                     word2 = word2[j+1:]
#         if not word1:
#             for c in word2:
#                 res += c
#         else:
#             for c in word1:
#                 res += c
#         return res

# sol = Solution()
# print(sol.largestMerge("uuurruuuruuuuuuuuruuuuu","urrrurrrrrrrruurrrurrrurrrrruu"))

# class Solution:
#     def minOperations(self, nums1, nums2):
#         min1,min2 = len(nums1),len(nums2)
#         max1,max2 = 6*min1,6*min2
#         if max1 < min2 or max2 < min1: return -1
#         sum1,sum2 = sum(nums1),sum(nums2)
#         if sum1 > sum2: nums1,nums2 = nums2,nums1
#         target = abs(sum1-sum2)
#         counter1 = collections.Counter(nums1)
#         counter2 = collections.Counter(nums2)
#         res = 0
#         for num in range(6,0,-1):
#             print(num)
#             tmpnum = counter1[6 - num + 1] + counter2[num]
#             while target > 0 and tmpnum:
#                 target -= (num-1)
#                 tmpnum -= 1
#                 res += 1
#             if target <= 0: return res
# sol = Solution()
# print(sol.minOperations([1,5,5,2,1,1,1,1,4,4,4,1,5,2,2,4,6,5,1,5,3,5,6,2,3,1,5,4,4,1,2,4,1,1,6,3,6,4,4,4,3,5,5,5,2,6,4,2,5,4,2,6,3,4,6,1,5,3,2,3,5,2,1,3,2,4,4,4,5,3,5,5,4,1,1,6,5,6,3,5,3,6,5,6,5,4,4,4,5,6,6,6,4,2,4,6,1,2,1,5,3,4,5,5,6,6,1,4,3,1,5,3,4,1,2,1,4,4,5,6,5,3,1,5,1,3,3,6,5,3,5,6,2,6,3,1,2,3,3,1,1,4,3,2,6,6,2,1,2,4,3,5,5,4,3,1,1,5,2,5,1,4,5,6,4,5,2,1,2,5,3,2,6,3,4,3,4,5,4,6,3,4,4,3,3,4,2,2,6,2,6,3,1,1,5,3,1,1,4,2,5,5,5,4,3,6,5,5,5,1,1,3,6,2,3,6,3,4,2,5,4,4,3,5,6,4,3,5,1,1,3,3,1,1,6,4,6,2,1,4,3,5,5],[1,2,5,4,3,3,5,1,1,6,2,5,4,4,5,6,6,4,2,5,6,2,3,4,5,2,4,4,3,6,6,5,4,1,2,1,2,3,3,2,6,1,1,1,1,3,5,6,2,1,1,1,4,6,5]))

# class Solution:
#     def checkPowersOfThree(self, n: int) -> bool:
#         base = 1
#         while base <= n:
#             base *= 3
#         base /= 3
#         while base >= 1:
#             n -= base
#             if n <= 0: break
#             base /= 3
#             while base > n:
#                 base /= 3
#         if n == 0: return True
#         return False
# class Solution:
#     def beautySum(self, s: str) -> int:
#         def getless(counter):
#             res = float("inf")
#             for key in counter:
#                 if counter[key] < res and counter[key]>0:
#                     res = counter[key]
#             return res

#         dp = [[0 for i in range(len(s))] for i in range(len(s))]
#         counter = collections.Counter(s)
#         for i in range(len(s)):
#             tmpcounter = counter.copy()
#             for j in range(i):
#                 tmpcounter[s[j]] -= 1
#             for j in range(len(s)-1,i+1,-1):
#                 dp[i][j] = tmpcounter.most_common(1)[0][1] - getless(tmpcounter)
#                 tmpcounter[s[j]] -= 1
#         res = 0
#         for list1 in dp:
#             res += sum(list1)
#         print(dp)
#         return res
# sol = Solution()
# print(sol.beautySum("aabcb"))

# import bisect
# class Solution:
#     def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
#         cnt_pair = []
#         for i in range(1,n):
#             for j in range(i+1,n+1):
#                 cnt_pair.append([i,j])
#         length = len(cnt_pair)
#         neighbours = [0 for i in range(length)]
#         print(cnt_pair)
#         counter = collections.defaultdict(int)
#         for edge in edges:
#             counter[edge[0]] += 1
#             counter[edge[1]] += 1
#         print(counter)
#         counter2 = collections.defaultdict(int)
#         for edge in edges:
#             counter2[tuple(edge)] += 1
#         print(counter2)
#         for i,pair in enumerate(cnt_pair):
#             neighbours[i] = counter[pair[0]] + counter[pair[1]]
#             neighbours[i] -= counter2[(pair[1],pair[0])]
#             neighbours[i] -= counter2[(pair[0],pair[1])]
#         print(neighbours)
#         neighbours = sorted(neighbours)
#         # print(neighbours)
#         res = []
#         for query in queries:
#             res.append(len(cnt_pair) - bisect.bisect_right(neighbours,query))
#         return res

# class Solution:
#     def checkOnesSegment(self, s: str) -> bool:
#         check = False
#         i = 0
#         while i < len(s):
#             if s[i] == 1:
#                 tmp = i
#                 while i < len(s) and s[i] == 1: i += 1
#                 if i - tmp >= 1:
#                     if not check: check = True
#                     else: return False
#             else: i += 1
#         return True

# sol = Solution()
# print(sol.checkOnesSegment([2,2,2,5,1,-2],5
# 126614243))

# import heapq
# import math
# class Solution:
#     def countRestrictedPaths(self, n, edges) -> int:
#         def init_distance(graph, s):
#             distance = {s: 0}
#             for vertex in graph:
#                 if vertex != s:
#                     distance[vertex] = math.inf
#             return distance

#         def dijkstra(graph, s):
#             pqueue = []
#             heapq.heappush(pqueue, (0, s))
#             seen = set()
#             parent = {s: None}
#             distance = init_distance(graph, s)

#             while len(pqueue) > 0:
#                 pair = heapq.heappop(pqueue)
#                 dist = pair[0]
#                 vertex = pair[1]
#                 seen.add(s)
#                 nodes = graph[vertex].keys()
#                 for w in nodes:
#                     if w not in seen:
#                         if dist + graph[vertex][w] < distance[w]:
#                             heapq.heappush(pqueue, (dist + graph[vertex][w], w))
#                             parent[w] = vertex
#                             distance[w] = dist + graph[vertex][w]
#             return parent, distance

#         edge_map = {}
#         for edge in edges:
#             if edge[0] not in edge_map:
#                 edge_map[edge[0]] = {edge[1]:edge[2]}
#             else:
#                 edge_map[edge[0]][edge[1]] = edge[2]

#             if edge[1] not in edge_map:
#                 edge_map[edge[1]] = {edge[0]:edge[2]}
#             else:
#                 edge_map[edge[1]][edge[0]] = edge[2]
#         print(edge_map)
#         parent_dict, distance_dict = dijkstra(edge_map, 5)
#         print(parent_dict)
#         print(distance_dict)

# sol = Solution()
# print(sol.countRestrictedPaths(5,[[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]))

# 2021.3.12 didi
# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.left = None
#         self.right = None

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

# def main(root):
#     quene = collections.deque()
#     quene.append(root)
#     res = []
#     while quene:
#         tmpNode = quene.popleft()
#         res.append(tmpNode.val)
#         if tmpNode.left != None: quene.append(tmpNode.left)
#         if tmpNode.right != None: quene.append(tmpNode.right)
#     return res

# # print(main(root))

# numlist = [3,4,5,7,9,1,2]

# def find(num,numlist):
#     def search(num,start,end):
#         if start > end: return -1
#         if start == end: return start
#         mid = len(numlist) // 2
#         res = 0
#         if numlist[mid] > num: res = search(num,0,mid)
#         elif numlist[mid] < num: res = search(num,mid+1,end)
#         else: return mid
#         return res

#     pos = -1
#     for i in range(len(numlist)-1):
#         if numlist[i+1] < numlist[i]:
#             numlist = numlist[i+1:] + numlist[:i+1]
#             pos = len(numlist) - i - 1
#             break
#     return search(num,0,len(numlist)) - pos

# print(find(4,numlist))

# contest 232
# class Solution:
#     def maxAverageRatio(self, classes, extraStudents):
#         def calDiff(tmpClass):
#             return (tmpClass[0] + 1) / (tmpClass[1] + 1) - tmpClass[0] / tmpClass[1]
#         diffList = []
#         for i,tmpClass in enumerate(classes):
#             diffList.append(calDiff(tmpClass))
#         while extraStudents:
#             changeClass = 0
#             diff = float("-inf")
#             for i,tmpDiff in enumerate(diffList):
#                 if tmpDiff > diff:
#                     changeClass = i
#                     diff = tmpDiff
#             classes[changeClass][0] += 1
#             classes[changeClass][1] += 1
#             diffList[changeClass] = calDiff(classes[changeClass])
#             extraStudents -= 1
#         res = 0
#         for tmpClass in classes:
#             res += tmpClass[0] / tmpClass[1]
#         return res / len(classes)

# sol = Solution()
# print(sol.maxAverageRatio([[290,966],[396,948],[153,345],[257,352],[4,855],[147,897],[193,264],[219,642],[7,60],[952,1000],[38,664],[471,879],[228,292],[537,772],[658,936],[113,767],[80,619],[154,874],[208,969],[183,910],[32,447],[161,176],[451,975],[54,329],[458,634],[367,515],[294,725],[131,593],[557,995],[900,968],[631,921],[54,535],[117,250],[464,956],[236,504],[325,527],[115,963],[314,687],[848,959],[155,273],[430,656],[118,272],[19,979],[5,937],[380,514],[59,189],[163,336],[36,44],[31,268],[32,254],[299,743],[494,738],[613,740],[661,938],[346,512],[92,602],[180,205],[360,736],[92,767],[379,805],[148,369],[199,937],[388,473],[356,459],[602,630],[81,888],[239,253],[98,242],[91,749],[320,536],[84,379],[125,602],[612,852],[370,946],[256,570],[291,793],[905,936],[318,645],[829,932],[128,924],[172,733],[217,417],[476,969],[140,794],[202,856],[82,445],[75,391],[158,585],[250,948],[263,309],[524,617],[588,743],[491,912],[396,880],[112,121],[676,912],[369,466],[494,675],[405,920],[218,909],[342,601],[154,643],[275,333],[653,976],[201,907],[47,613],[677,949],[273,413],[330,828],[111,647],[136,209],[383,951],[482,647],[333,578],[45,57],[470,727],[138,466],[511,522],[219,773],[822,880],[264,285],[160,631],[122,291],[326,996],[229,350],[202,321],[125,778],[426,875],[217,431],[137,799],[525,840],[91,545],[398,904],[30,396],[143,404],[355,634],[529,780],[407,617],[150,750],[96,673],[783,989],[536,703],[237,773],[205,988],[485,499],[388,791],[326,732],[259,571],[894,993],[10,542],[537,773],[716,861],[756,944],[267,750],[25,998],[391,759],[403,535],[149,175],[266,626],[102,417],[117,724],[414,490],[55,936],[84,500],[578,962],[82,228],[346,925],[396,936],[626,696],[676,849],[352,875],[365,856],[682,731],[773,952],[257,945],[248,420],[141,771],[227,700],[411,942],[640,745],[48,253],[193,582],[152,581],[192,348],[112,961],[790,925],[214,431],[54,952],[341,526],[550,884],[735,775],[358,371],[676,725],[448,939],[234,359],[793,952],[74,390],[231,930],[480,868],[132,366],[642,982],[95,378],[475,528],[820,978],[387,429],[270,797],[76,469],[479,681],[153,270],[721,967],[712,938],[15,804],[541,964],[372,434],[243,948],[360,879],[477,721],[340,824],[452,533],[12,771],[149,826],[736,778],[247,806],[102,709],[231,280],[230,374],[579,866],[189,986],[367,456],[377,855],[40,716],[688,720],[187,399],[362,545],[356,678],[835,865],[566,956],[419,585],[310,522],[267,470],[55,85],[107,571],[276,761],[318,942],[218,831],[438,571],[600,815],[205,892],[252,286],[95,428],[402,697],[519,869],[295,300],[498,620],[975,985],[833,846],[95,423],[230,718],[205,494],[125,528],[368,995],[583,867],[769,885],[86,557],[33,84],[251,331],[454,881],[93,198],[34,906],[136,452],[88,703],[67,483],[813,905],[52,148],[129,507],[507,707],[447,491],[12,302],[257,622],[558,649],[122,612],[94,915],[642,875],[547,573],[852,942],[375,633],[35,239],[553,965],[574,683],[156,877],[23,770],[391,950],[43,136],[342,687],[393,569],[824,846],[75,617],[462,798],[316,336],[212,438],[496,975],[66,390],[779,931],[259,917],[803,856],[5,666],[644,679],[893,942],[108,310],[749,837],[226,581],[388,592],[14,996],[78,401],[602,672],[93,864],[65,250],[430,881],[540,871],[458,567],[319,873],[517,787],[34,148],[497,506],[377,638],[154,561],[120,212],[275,556],[15,804],[509,641],[604,679],[148,464],[152,324],[410,453],[280,855],[470,621],[607,979],[804,895],[380,723],[407,926],[787,970],[633,691],[86,590],[23,221],[229,563],[253,625],[356,689],[444,992],[571,784],[99,977],[30,85],[240,797],[662,878],[246,340],[744,951],[206,542],[168,563],[87,523],[63,166],[308,653],[257,601],[727,909],[342,700],[888,910],[357,434],[381,788],[2,211],[596,628],[512,953],[135,183],[3,391],[18,187],[272,375],[844,934],[224,792],[417,675],[194,821],[250,429],[678,914],[208,601],[426,585],[45,389],[176,599],[2,855],[643,837],[103,213],[59,299],[151,561],[403,625],[189,369],[604,960],[681,783],[168,173],[525,915],[840,984],[151,983],[512,879],[91,661],[459,929],[188,809],[295,800],[274,359],[249,454],[587,722],[45,750],[235,667],[223,876],[826,887],[276,805],[246,832],[721,767],[441,841],[849,964],[755,897],[287,731],[734,934],[241,369],[802,864],[502,910],[421,901],[207,826],[470,526],[543,693],[324,818],[48,239],[228,553],[159,434],[127,558],[76,780],[427,953],[437,525],[391,616],[97,470],[208,816],[61,401],[214,559],[217,718],[443,539],[764,860],[523,734],[631,874],[525,618],[483,771],[384,656],[108,994],[386,652],[695,961],[302,781],[521,815],[377,976],[321,877],[181,899],[432,870],[680,815],[253,556],[195,979],[77,876],[88,233],[261,699],[431,759],[229,505],[263,657],[35,882],[404,959],[353,412],[476,945],[210,427],[56,293],[238,940],[147,155],[345,958],[675,896],[675,894],[554,763],[694,921],[304,626],[596,993],[463,932],[436,691],[309,384],[321,753],[233,266],[404,465],[763,984],[40,338],[593,797],[216,819],[698,796],[98,676],[140,641],[254,361],[148,902],[513,734],[458,890],[409,773],[13,257],[324,427],[147,887],[71,327],[212,966],[216,396],[410,630],[523,566],[93,694],[480,653],[217,991],[116,142],[832,951],[390,940],[115,396],[530,790],[603,992],[744,853],[820,887],[777,865],[251,840],[479,791],[495,557],[84,166],[6,773],[362,929],[58,977],[579,971],[140,471],[512,774],[207,393],[745,871],[194,618],[63,349],[202,491],[288,764],[183,562],[510,518],[761,870],[428,541],[50,938],[159,197],[11,859],[315,429],[74,711],[189,664],[25,386],[297,523],[152,919],[142,293],[175,942],[306,955],[240,521],[814,826],[316,684],[830,887],[460,638],[217,521],[200,719],[54,211],[386,621],[336,994],[365,676],[393,788],[46,689],[91,405],[162,506],[158,361],[317,918]],61848))

# class Solution:
#     def maximumScore(self, nums, k):
#         N = len(nums)
#         res = 0
#         minnum = [[0 for i in range(N)] for i in range(N)]
#         dp = [[0 for i in range(N)] for i in range(N)]
#         for i in range(N):
#             minnum[i][i] = nums[i]
#         for i in range(0,k+1):
#             for j in range(i,N):
#                 if j != i: minnum[i][j] = min(minnum[i][j-1],nums[j])
#                 if j < k: continue
#                 if minnum[i][j] != minnum[i][j-1] or dp[i][j-1] == 0: dp[i][j] = minnum[i][j] * (j-i+1)
#                 else: dp[i][j] = dp[i][j-1] + minnum[i][j]
#                 res = max(res,dp[i][j])
#         return res

# sol = Solution()
# print(sol.maximumScore([6569,9667,3148,7698,1622,2194,793,9041,1670,1872],5))
import heapq
heapq.heappush