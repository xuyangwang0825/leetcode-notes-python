# -*- coding: utf-8 -*-
# import collections
# import numpy as np
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


# class Solution:
#     def secondHighest(self, s):
#         first,second = -1,-1
#         for c in s:
#             if c.isdigit():
#                 if first == -1 and second == -1: first = int(c)
#                 elif first != -1 and second == -1:
#                     if int(c) > first:
#                         second = first
#                         first = int(c)
#                     else:
#                         second = int(c)
#                 else:
#                     if int(c) > first:
#                         second = first
#                         first = int(c)
#                     elif int(c) > second and int(c) != first:
#                         second = int(c)
#         print(first,second)
#         return second if second != first else -1

# sol = Solution()
# print(sol.secondHighest("ck077"))

# class Solution:
#     def getMaximumConsecutive(self, coins):
#         d = collections.defaultdict(int)
#         for coin in coins: d[coin] += 1
#         #d = sorted(d.items(),key=lambda item:item[0])
#         ctSet = set()
#         for k,v in d.items():
#             if not ctSet:
#                 for time in range(v+1):
#                     ctSet.add(k*time)
#             else:
#                 for ct in list(ctSet.copy()):
#                     for time in range(v+1):
#                         ctSet.add(k*time+ct)
#         print(ctSet)

# sol = Solution()
# print(sol.getMaximumConsecutive([1,3]))

# class Solution:
#     def maxValue(self, n, index, maxSum):
#         target = maxSum - n
#         base = 1
#         res = 0
#         while target:
#             target -= base
#             base += 1
#             res += 1
#         print(res)

# sol = Solution()
# print(sol.maxValue(4,2,6))

# class Solution:
#     def maxNiceDivisors(self, primeFactors):
#         if primeFactors == 1: return 1

#         def isprime(n):
#             for i in range(2, n):
#                 if n % i == 0:
#                     return False
#             return True

#         i = 2
#         facDict = collections.defaultdict(int)
#         while primeFactors:
#             while not isprime(i): i += 1
#             while primeFactors % i == 0:
#                 facDict[i] += 1
#                 primeFactors = primeFactors / i
#         print(facDict)

# sol = Solution()
# print(sol.maxNiceDivisors(5))

# class Solution:
#     def maxHappyGroups(self, batchSize, groups):
#         res = 0
#         tmp_dict = {}
#         for i in range(batchSize):
#             if i != 0:
#                 tmp_dict[i] = 0
#         for g in groups:
#             tmp = g % batchSize
#             if tmp == 0: res += 1
#             else:
#             # else:
#             #     if tmp_dict[batchSize - tmp] > 0:
#             #         res += 1
#             #         tmp_dict[batchSize - tmp] -= 1
#             #     else:
#             #         tmp_dict[tmp] += 1
#                 tmp_dict[tmp] += 1
#         print(tmp_dict)
#         for i in sorted (tmp_dict) :
#             # print ((i, tmp_dict[i]), end =" ")
#             tmp = tmp_dict[i]
#             while tmp_dict[i] and tmp:
#                 if batchSize - tmp != i and tmp_dict[batchSize - tmp] > 0:
#                     res += 1
#                     tmp_dict[i] -= tmp
#                     tmp_dict[batchSize - tmp] -= 1
#                 tmp -= 1
#         return res

# sol = Solution()
# print(sol.maxHappyGroups(4,[1,3,2,5,2,2,1,6]))

# class Solution:
#     def minAbsoluteSumDiff(self, nums1, nums2):
#         change_pos = []
#         diff_list = []
#         res = 0
#         for i in range(len(nums1)):
#             tmp_diff = abs(nums1[i] - nums2[i])
#             diff_list.append(tmp_diff)
#             res += tmp_diff
#         max_diff = max(diff_list)
#         for i,diff in enumerate(diff_list):
#             if diff == max_diff:
#                 change_pos.append(i)
#         print(diff_list)
#         res_list = []
#         for i in change_pos:
#             target1 = target2 = nums2[i]
#             while True:
#                 if target1 in nums1 or target2 in nums1:
#                     res_list.append(res - max_diff)
#                     break
#                 else:
#                     max_diff -= 1
#                     target1 += 1
#                     target2 -= 1
#         return min(res_list)

# sol = Solution()
# print(sol.minAbsoluteSumDiff([1,10,4,4,2,7],[9,3,5,1,7,4]))

# class Solution:
# def purchasePlans(self, nums, target):
#     num_dict = {}
#     res = 0
#     for i,num in enumerate(nums):
#         if num >= target: break
#         for k in range(1,target-num+1):
#             if k in num_dict:
#                 res += num_dict[k]
#                 res %= 1000000007
#         if i in num_dict: num_dict[i] += 1
#         else: num_dict[num] = 1
#     return res % 1000000007
#     def orchestraLayout(self, num, xPos, yPos):
#         yueqi = [i for i in range(1,10)]
#         matrix = [[0 for i in range(num)] for i in range(num)]
#         pos = 0

#         rows = columns = num
#         visited = [[False] * columns for _ in range(rows)]
#         total = rows * columns

#         directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#         row, column = 0, 0
#         directionIndex = 0
#         for i in range(total):
#             matrix[row][column] = yueqi[pos]
#             if pos < 8: pos += 1
#             else: pos = 0
#             visited[row][column] = True
#             nextRow, nextColumn = row + directions[directionIndex][0], column + directions[directionIndex][1]
#             if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
#                 directionIndex = (directionIndex + 1) % 4
#             row += directions[directionIndex][0]
#             column += directions[directionIndex][1]
#         for i in matrix:
#             print(i)
#             # print("\n")
#         return matrix[xPos][yPos]
#     def orchestraLayout2(self, num, xPos, yPos):
#         xr,xl,yr,yl = num-1,0,num-1,0
#         start = 0
#         while xPos not in (xr,xl) and yPos not in (yr,yl):
#             start += ((xr - xl - 1) * 4 + 4)
#             start = start % 9
#             xr -= 1
#             xl += 1
#             yr -= 1
#             yl += 1
#         n = (xr - xl)

#         if xPos == xl:
#             tmp = (start + yPos - yl + 1)
#             if tmp % 9 == 0: return 9
#             else: return tmp % 9
#         else: start += n

#         if yPos == yr:
#             tmp = (start + xPos - xl + 1)
#             if tmp % 9 == 0: return 9
#             else: return tmp % 9
#         else: start += n

#         if xPos == xr:
#             tmp = (start + yr - yPos + 1)
#             if tmp % 9 == 0: return 9
#             else: return tmp % 9
#         else: start += n

#         if yPos == yl:
#             tmp = (start + xr - xPos + 1)
#             if tmp % 9 == 0: return 9
#             else: return tmp % 9
#         else: start += n
# sol = Solution()
# print(sol.orchestraLayout(9,7,7))
# print(sol.orchestraLayout2(9,3,3))
# print(sol.orchestraLayout(4,1,1))
# print(sol.orchestraLayout(4,1,2))
# print(sol.orchestraLayout(4,2,2))
# print(sol.orchestraLayout(4,2,1))

# import math
# import heapq

# class Solution:
#     def storeWater(self, bucket, vat):
#         times = []
#         res = 0
#         for i in range(len(vat)):
#             if bucket[i] == 0:
#                 res += 1
#                 bucket[i] += 1

#             tmp = math.ceil(vat[i]/bucket[i])
#             if tmp == 0 and vat[i]!=0: tmp += 1
#             times.append([-tmp,i])

#         print(times)
#         heapq.heapify(times)
#         print(times)
#         tmpres = res - times[0][0]
#         while True:
#             _, i = heapq.heappop(times)
#             res += 1
#             bucket[i] += 1
#             heapq.heappush(times,[- math.ceil(vat[i]/bucket[i]),i])
#             if res - times[0][0] > tmpres:
#                 break
#             else:
#                 tmpres = res - times[0][0]
#         return tmpres


# sol = Solution()
# print(sol.storeWater([3,2,1],[6,6,6]))


# def processStr(str):
#     i = 0
#     res = ""
#     flag = 0
#     while i < len(str):
#         j = i + 1
#         while j < len(str) and str[j] == str[i]: j+= 1
#         if j - i >= 3:
#             if flag == 1:
#                 res += str[i]
#                 flag = 0
#             else:
#                 res += str[i:i+2]
#                 flag = 1
#         elif j - i == 2:
#             if flag == 0:
#                 res += str[i:j]
#                 flag = 1
#             else:
#                 res += str[i]
#                 flag = 0
#         else:
#             res += str[i]
#             flag = 0
#         i = j
#     print(res)

# processStr("yyybeettxjjjpppddsrxxxkkkyyyooowwwwwkyyxxppplllwwwiivvssnrvvvccclyydddhaaayiic")
# print("yybeetxjjpddsrxxkyyowwkyyxpplwwivvsnrvvclyydhaayiic")

# import itertools
# n,d = 4,3
# posList = [1,2,3,4]
# diff = {}
# res = 0
# res = 0
# for i in range(n-2):
#     for j in range(n-1,i,-1):
#         if posList[j] - posList[i] <= d:
#             break
#     if j - i >= 2:
#         comb = (j-i)*(j-i-1) // 2
#         res += comb
# print(res)

# sol = Solution()
# print(sol.minAbsoluteSumDiff([1,10,4,4,2,7],[9,3,5,1,7,4]))

# import heapq
# class Solution:
#     def maximumNumber(self, num, change) -> str:
#         res = ""
#         flag = -1
#         for i in range(len(num)):
#             i_c = int(num[i])
#             if change[i_c] <= i_c:
#                 res += num[i]
#             else:
#                 flag = i
#                 break
#         if flag == -1: return res
#         while flag < len(num):
#             i_c = int(num[flag])
#             if change[i_c] > i_c:
#                 res += str(change[i_c])
#             else:
#                 break
#             flag += 1
#         while flag < len(num):
#             res += num[flag]
#             flag += 1
#         return res

# sol = Solution()
# print(sol.maximumNumber("5",[1,4,7,5,3,2,5,6,9,4]))

# class Solution:
#     def isThree(self, n) -> bool:
#         i = 1
#         flag = 0
#         while n != 1:
#             if flag > 3: return False
#             if n % i == 0:
#                 n //= i
#                 flag += 1
#             i += 1
#         if flag == 3: return True
#         else: return False

# sol = Solution()
# print(sol.isThree(4))

# class Solution:
#     def minimumPerimeter(self, neededApples: int) -> int:
#         base = 1
#         tmp = 8
#         tmp_all = 8
#         while tmp < neededApples:
#             tmp += (base*2 + 1)*4 + 8
#             tmp_all += tmp
#             base += 1
#         return base * 8

# class Solution:
#     def minimizeTheDifference(self, mat, target):
#         res1 = float("inf")
#         m,n = len(mat),len(mat[0])
#         def dfs(tmp,line):
#             global res1
#             if line == n:
#                 res1 = min(res1,abs(tmp-target))
#                 return
#             for i in range(n):
#                 if (tmp+mat[line][i] - target) < res1:
#                     dfs(tmp+mat[line][i],line)
#         dfs(0,0)
#         return res1


# twitch oa
# def solution(streamerInformation, commands):

#     ret = []

#     # initialization
#     pos = 0

#     # dict record the position of info
#     streamerDict = {}
#     while pos < len(streamerInformation):
#         streamerDict[streamerInformation[pos].strip()] = pos
#         pos += 3
#     pos = 0
#     while pos < len(commands):
#         if commands[pos].strip() == "StreamerOnline":
#             if commands[pos+1].strip() not in streamerDict:
#                 streamerInformation.append(commands[pos+1].strip())
#                 streamerInformation.append(commands[pos+2].strip())
#                 streamerInformation.append(commands[pos+3].strip())
#             pos += 4
#         elif commands[pos].strip() == "UpdateViews":
#             if commands[pos+1].strip() in streamerDict:
#                 editPos = streamerDict[commands[pos+1].strip()] + 1
#                 if streamerInformation[editPos+1].strip() == commands[pos+3].strip():
#                     streamerInformation[editPos] = commands[pos+2].strip()
#             pos += 4
#         elif commands[pos].strip() == "UpdateCategory":
#             if commands[pos+1].strip() in streamerDict:
#                 editPos = streamerDict[commands[1].strip()] + 2
#                 if streamerInformation[editPos].strip() == commands[pos+2].strip():
#                     streamerInformation[editPos] = commands[pos+3]
#             pos += 4
#         elif commands[pos].strip() == "StreamerOffline":
#             if commands[pos+1].strip() in streamerDict:
#                 editPos = streamerDict[commands[pos+1].strip()]
#                 if streamerInformation[editPos+2].strip() ==  commands[pos+2].strip():
#                     del streamerDict[streamerInformation[editPos].strip()]
#                     streamerInformation[editPos] = ""
#                     streamerInformation[editPos+1] = ""
#                     streamerInformation[editPos+2] = ""
#             pos += 3
#         elif commands[pos].strip() == "ViewsInCategory":
#             res = 0
#             for key,value in streamerDict.items():
#                 if streamerInformation[value+2].strip() == commands[pos+1].strip():
#                     res += int(streamerInformation[value+1].strip())
#             pos += 2
#             ret.append(str(res))
#         elif commands[pos].strip() == "TopStreamerInCategory":
#             res = ""
#             tmpNum = float("-inf")
#             for key,value in streamerDict.items():
#                 if streamerInformation[value+2].strip() == commands[pos+1].strip():
#                     if int(streamerInformation[value+1].strip()) > tmpNum:
#                         res = streamerInformation[value]
#             pos += 2
#             ret.append(str(res))
#         elif commands[pos].strip() == "TopStreamer":
#             res = ""
#             tmpNum = float("-inf")
#             for key,value in streamerDict.items():
#                 if int(streamerInformation[value+1].strip()) > tmpNum:
#                     res = streamerInformation[value].strip()
#                     tmpNum = int(streamerInformation[value+1].strip())
#             ret.append(str(res))
#             pos += 2
#     return ret


# print(solution(["Ninja", " 100000", " Fortnite", " Pokimane", " 40000", " Valorant"], ["UpdateCategory", "  Ninja", " Fortnite", " Warzone", " ViewsInCategory", " Fortnite", " ViewsInCategory", " Warzone"]))
# print('\",\"')

# import collections
# class Solution:
#     def firstDayBeenInAllRooms(self, nextVisit):
#         visitNum = collections.defaultdict(int)
#         n = len(nextVisit)
#         day = 0
#         room = nextVisit[0]
#         checkset = set()
#         while True:
#             if room not in checkset:
#                 checkset.add(room)
#             if len(checkset) == n:
#                 return day % 1000000007
#             visitNum[room] += 1
#             day += 1
#             if visitNum[room] % 2:
#                 room =  nextVisit[day]
#             else:
#                 room = (room + 1) % n

# sol = Solution()
# print(sol.firstDayBeenInAllRooms([0,0,2]))


# def countHighlyProfitableMonths(stockPrices, k):
#     print(stockPrices,k)
#     # Write your code here
#     r = 1
#     res = 0
#     strInc = 1
#     n = len(stockPrices)
#     while r < n:
#         if stockPrices[r] > stockPrices[r-1]:
#             strInc += 1
#         else:
#             if strInc >= k:
#                 res += strInc - k + 1
#                 strInc = 1
#         r += 1
#     if strInc >= k:
#         res += strInc - k + 1
#     return res

# print(countHighlyProfitableMonths([6426, 9445, 8772, 81, 3447, 629, 3497, 7202, 7775, 4325, 3982, 4784, 8417, 2156, 1932, 5902, 5728, 8537, 3857, 739, 6918, 9211, 9679, 8506, 3340, 6568, 1868, 16, 7940, 6263, 4593, 1449, 6991, 310, 3355, 7068, 1431, 8580, 1757, 9218, 4934, 4328, 3676, 9355, 6221, 9080],3))


# def getUnallottedUsers(bids, totalShares):
#     print(bids, totalShares)
#     # Write your code here
#     sortedBids = sorted(sorted(bids, key = lambda x:x[3], reverse = False), key = lambda x:x[2], reverse = True)
#     share = {}
#     if len(sortedBids) == 1:
#         if totalShares < sortedBids[0][1]:
#             return [sortedBids[0][0]]
#         else:
#             return []
#     for i in range(len(sortedBids)):
#         if totalShares > 0:
#             if i == len(sortedBids) -1 or sortedBids[i][2] > sortedBids[i+1][2]:
#                 share[sortedBids[i][0]] = "get"
#                 if totalShares < sortedBids[i][1]:
#                     return sorted([x[0] for x in sortedBids if x[0] not in list(share.keys())])
#                 totalShares -= sortedBids[i][1]
#             else:
#                 sumShare = sortedBids[i][1]
#                 end = i
#                 for j in range(i,len(sortedBids)-1):
#                     end = j
#                     if sortedBids[j][2] == sortedBids[j+1][2]:
#                         sumShare += sortedBids[j+1][1]
#                     else:
#                         break
#                 if totalShares < end-i:
#                     for x in range(i,len(sortedBids)):
#                         if totalShares > 0:
#                             share[sortedBids[x][0]] = "get"
#                             totalShares -= 1
#                         else:
#                             sorted([x[0] for x in sortedBids if x[0] not in list(share.keys())])
#                 elif totalShares > sumShare:
#                     for x in range(i, end+1):
#                         share[sortedBids[x][0]] = "get"
#                     totalShares -= sumShare
#                 else:
#                     for x in range(i, end+1):
#                         share[sortedBids[x][0]] = "get"
#                     return sorted([x[0] for x in sortedBids if x[0] not in list(share.keys())])
#         else:
#             return sorted([x[0] for x in sortedBids if x[0] not in list(share.keys())])

# print(getUnallottedUsers([[1, 2, 1, 3535], [2, 2, 2, 346]],3))

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 2021.9.11 Okta OA
# def solution(B):
#     B = [list(row) for row in B]
#     termX, termY = len(B)-1, len(B[0])-1
#     startX, startY = 0,0
#     for i, row in enumerate(B):
#         for j, block in enumerate(row):
#             if block == '>':
#                 for k in range(j+1, len(row)):
#                     if B[i][k] in ['X', '>', '<', '^', 'v']:
#                         break
#                     B[i][k] = 'C'
#             elif block == '<':
#                 for k in range(j):
#                     if B[i][k] in ['X', '>', '<', '^', 'v']:
#                         break
#                     B[i][k] = 'C'
#             elif block == '^':
#                 for k in range(i):
#                     if B[k][j] in ['X', '>', '<', '^', 'v']:
#                         break
#                     B[k][j] = 'C'
#             elif block == 'v':
#                 for k in range(i+1,len(B)):
#                     if B[k][j] in ['X', '>', '<', '^', 'v']:
#                         break
#                     B[k][j] = 'C'
#             elif block == 'A':
#                 startX, startY = i, j

#     checkSet = set()
#     def dfs(x,y):
#         # out of space
#         if str((x, y)) in checkSet:
#             return False
#         if x < 0 or x > termX or y < 0 or y > termY:
#             return False
#         # sneak success
#         if B[x][y] in ['X', '>', '<', '^', 'v', 'C']:
#             return False
#         if x == termX and y == termY:
#             return True
#         checkSet.add(str((x, y)))
#         return dfs(x+1,y) or dfs(x-1,y) or dfs(x,y+1) or dfs(x,y-1)

#     return dfs(startX, startY)


# print(solution(['A.v', '...']))

# class Solution:
#     def bicycleYard(self, position: List[int], terrain: List[List[int]], obstacle: List[List[int]]) -> List[List[int]]:
#         self.res = []
#         self.visit = [[0 for i in range(len(terrain[0]))] for j in range(len(terrain))]

#         def dfs(self,x,y,v):
#             if v <= 0:
#                 return
#             if self.visit[x][y] == 1:
#                 return
#             self.visit[x][y] = 1
#             if v == 1 and [x,y] != position:
#                 self.res.append([x,y])
#             if x < len(terrain)-1:
#                 dfs(self,x+1,y,v + terrain[x][y]-terrain[x+1][y] - obstacle[x+1][y])
#             if x > 0:
#                 dfs(self,x-1,y,v + terrain[x][y]-terrain[x-1][y]-obstacle[x-1][y])
#             if y < len(terrain[0])-1:
#                 dfs(self,x,y+1,v + terrain[x][y]-terrain[x][y+1]-obstacle[x][y+1])
#             if y > 0:
#                 dfs(self,x,y-1,v + terrain[x][y]-terrain[x][y-1]-obstacle[x][y-1])

#         dfs(self,position[0],position[1],1)
#         return sorted(self.res)

# sol = Solution()
# sol.bicycleYard()

# stripe screen 1 MutualRank / WishList / ChangePair
# dic = {}
# dic['a'] = ['b','c','d']
# dic['b'] = ['a','c','d']
# dic['c'] = ['d','a']
# dic['d'] = ['a','c']

# def hasMutualFirstChoice(name):
#     if name not in dic:
#         return False

#     fChoice = dic[name][0]
#     return dic[fChoice][0] == name

# # set rank
# def hasMutualFirstChoice1(name, index):
#     if name not in dic or index >= len(dic[name]):
#         return False

#     fChoice = dic[name][index]
#     return dic[fChoice][index] == name

# # swap index, index-1
# def hasMutualFirstChoice2(name, index):
#     res = []

#     if hasMutualFirstChoice1(name, index):
#         res.append(dic[name][index])

#     if name in dic and index < len(dic[name]):
#         fChoice = dic[name][index-1]

#         if dic[fChoice][index] == name:
#             res.append(fChoice)

#     return res

# print(hasMutualFirstChoice('d'))
# print(hasMutualFirstChoice1('a',1))
# print(hasMutualFirstChoice2('c',1))

# stripe screen 2 HTTP Header Parsing
# Part 1

# In an HTTP request, the Accept-Language header describes the list of
# languages that the requester would like content to be returned in. The header
# takes the form of a comma-separated list of language tags. For example:

# Accept-Language: en-US, fr-CA, fr-FR

# means that the reader would accept:

# 1. English as spoken in the United States (most preferred)
# 2. French as spoken in Canada
# 3. French as spoken in France (least preferred)

# We're writing a server that needs to return content in an acceptable language
# for the requester, and we want to make use of this header. Our server doesn't
# support every possible language that might be requested (yet!), but there is a
# set of languages that we do support. Write a function that receives two arguments:
# an Accept-Language header value as a string and a set of supported languages,
# and returns the list of language tags that that will work for the request. The
# language tags should be returned in descending order of preference (the
# same order as they appeared in the header).

# In addition to writing this function, you should use tests to demonstrate that it's
# correct, either via an existing testing system or one you create.

# Examples:

# parse_accept_language(
# "en-US, fr-CA, fr-FR", # the client's Accept-Language header, a string
# ["fr-FR", "en-US"] # the server's supported languages, a set of strings
# )
# returns: ["en-US", "fr-FR"]

# parse_accept_language("fr-CA, fr-FR", ["en-US", "fr-FR"])
# returns: ["fr-FR"]

# parse_accept_language("en-US", ["en-US", "fr-CA"])
# returns: ["en-US"]

# def headerPase(cLan, sLan):
#     res = []
#     lan_dic = {}
#     cLan = cLan.split(", ")

#     for lan in sLan:
#         lan_dic[lan] = 1

#     for lan in cLan:
#         if lan in lan_dic:
#             res.append(lan)

#     return res

# print(headerPase("en-US, fr-CA, fr-FR", ["fr-FR", "en-US"]))

# Part 2

# Accept-Language headers will often also include a language tag that is not
# region-specific - for example, a tag of "en" means "any variant of English". Extend
# your function to support these language tags by letting them match all specific
# variants of the language.

# Examples:

# parse_accept_language("en", ["en-US", "fr-CA", "fr-FR"])
# returns: ["en-US"]

# parse_accept_language("fr", ["en-US", "fr-CA", "fr-FR"])
# returns: ["fr-CA", "fr-FR"]

# parse_accept_language("fr-FR, fr", ["en-‍‌‌‌‌‌‌‍‌‍‌‌‌‌‌‌‍‌‌‍US", "fr-CA", "fr-FR"])
# returns: ["fr-FR", "fr-CA"]


# def headerPase2(cLan, sLan):
#     res = []
#     # lan_dic = {}
#     cLan = cLan.split(", ")

#     # for lan in sLan:å
#     #     lan_dic[lan] = 1

#     for lan in cLan:
#         for k in sLan:
#             if lan in k and k not in res:
#                 res.append(k)
#     return res

# print(headerPase2("fr-FR, fr", ["en-‍‌‌‌‌‌‌‍‌‍‌‌‌‌‌‌‍‌‌‍US", "fr-CA", "fr-FR"]))

# Part 3

# Accept-Language headers will sometimes include a "wildcard" entry, represented
# by an asterisk, which means "all other languages". Extend your function to
# support the wildcard entry.

# Examples:

# parse_accept_language("en-US, *", ["en-US", "fr-CA", "fr-FR"])
# returns: ["en-US", "fr-CA", "fr-FR"]

# parse_accept_language("fr-FR, fr, *", ["en-US", "fr-CA", "fr-FR"])
# returns: ["fr-FR", "fr-CA", "en-US"]

# def headerPase3(cLan, sLan):
#     res = []
#     # lan_dic = {}
#     cLan = cLan.split(", ")

#     # for lan in sLan:
#     #     lan_dic[lan] = 1

#     for lan in cLan:
#         for k in sLan:
#             if (lan in k or lan == '*') and k not in res:
#                 res.append(k)
#     return res

# print(headerPase3("fr-FR, fr, *", ["en-US", "fr-CA", "fr-FR"]))

# stripe screen 3 Server Remove Penalty
# Throughout this interview, we'll write code to analyze a simple server process uptime log.
# These logs are much simplified, and are just strings of space separated 0's and 1's.
# The log is a string of binary digits (e.g. "0 0 1 0"). Each digit corresponds to
# 1 hour of the server running:

# "1" = <crashed>, "down" // server process crashed during the hour
# "0" = <didn't crash>, "up" // server process did not crash during the hour

# EXAMPLE: A server with log "0 0 1 0" ran for 4 hours and its process crashed during hour #3

#    hour: |1|2|3|4|
#    log : |0|0|1|0|
#               ^
#               |
#              down during hour #3

# We can *permanently remove* a server at the beginning of any hour during its operation.
# A server is on the network until it is removed. Note that a server stays POWERED ON after
# removal, it's just not on the network.

# We'd like to understand the best times to remove a server. So let's introduce an aggregate
# metric called a "penalty" for removing a server at a bad time.


# EXAMPLE: Remove a server with log "0 0 1 0"
#     hour :  | 1 | 2 | 3 | 4 |
#     log  :  | 0 | 0 | 1 | 0 |
# remove_at:  0   1   2   3   4   // remove_at being `x` means "server removed before hour `x+1`"
#             ^               ^
#             |               |
#      before hour #1         after hour #4

# Further Examples:

# EXAMPLE:

#    hour :   1 2 3 4     // total penalty = 3  (3 server-up hours after remove)
#    log  :   0 0 1 0
#            ^
#            |
#          remove_at = 0

#    hour :   1 2 3 4     // total penalty = 1  (1 server-down hour before remove)
#    log  :   0 0 1 0
#                    ^
#                    |
#                  remove_at = 4

# Note that for a server log of length `n` hours, the remove_at variable can range from 0,
# meaning "before the first hour" to n, meaning "after the final hour".

# 1a) Write a function: compute_penalty, that computes the total penalty, given a server log
# (as a string) AND a time at which we removed the server from the network (call that  variable
# remove_at). In addition to writing this function, you should use tests to demonstrate
# that it's correct.

# ## Examples
# compute_penalty("0 0 1 0", 0) should return 3
# compute_penalty("0 0 1 0", 4) should return 1

# def compute_penalty(serverLog, removeTime):
#     penalty = 0
#     serverLog = serverLog.split(" ")

#     for t in range(removeTime):
#         if serverLog[t] == "1":
#             penalty += 1

#     for t in range(removeTime,len(serverLog)):
#         if serverLog[t] == "0":
#             penalty += 1

#     return penalty

# 1b) Use your answer for compute_penalty to write another function:
# find_best_removal_time, that returns the best remove_at hour, given a server log.
# Again, you should use tests to demonstrate that it's correct.

# ## Example
# find_best_removal_time("0 0 1 1") should return 2

# def find_best_removal_time(serverLog):
#     serverLog = serverLog.split(" ")

#     res = 0
#     minPenalty = len([i for i in serverLog if i == "0"])
#     penalty = minPenalty

#     for i, log in enumerate(serverLog):
#         if log == "1":
#             penalty += 1
#         else:
#             penalty -= 1
#         if penalty < minPenalty:
#             minPenalty = penalty
#             res = i+1

#     return res

# 2a) Now that we're able to analyze single server logs, let's analyze some aggregate logs.
# Aggregate logs are text files that contain lots of logs. The files contain only
# BEGIN, END, 1, 0, spaces and newlines. Aggregate logs include some servers that aren’t
# actually finished, so we might have some BEGINs scattered throughout. We'll only consider
# inner BEGINs and ENDs to be valid log sequences. Put another way, any sequence of 0s and 1s
# surrounded by BEGIN and END forms a valid sequence. For example, the sequence
#  "BEGIN BEGIN BEGIN 1 1 BEGIN 0 0 END 1 1 BEGIN" has only one valid sequence "BEGIN 0 0 END".

# Write a function get_best_removal_times, that takes the file's contents as a parameter,
# and returns an ar‍‌‌‌‌‌‌‍‌‍‌‌‌‌‌‌‍‌‌‍ray of best removal hours for every valid server log in that file.

# Note: that logs can span 1 or many lines.

# Again, you should use tests to demonstrate that your solution is correct.

# ## Example
# get_best_removal_times("BEGIN BEGIN \nBEGIN 1 1 BEGIN 0 0\n END 1 1 BEGIN") should return
# an array: [2]

# def analyse_agg_logs(aLogs):
#     aLogs = aLogs.split(" ")
#     aLogs = [s.replace("\n","") for s in aLogs]

#     valid_log_list = []
#     res = []

#     i = 0
#     while i < len(aLogs):
#         if aLogs[i] == "BEGIN":
#             i += 1
#             tmpLog = []
#             while i < len(aLogs):
#                 word = aLogs[i]
#                 if word == "BEGIN":
#                     break
#                 elif word == "END":
#                     valid_log_list.append(tmpLog)
#                 else:
#                     tmpLog.append(word)
#                 i += 1
#         else:
#             i += 1

#     for validLog in valid_log_list:
#         tmpLog = ""
#         for word in validLog:
#             tmpLog += word + " "
#         res.append(find_best_removal_time(tmpLog))

#     return res


# stripe screen Bot Defender


# import unittest

# class TestStringMethods(unittest.TestCase):

#     def test_compute_penalty_low(self):
#         self.assertEqual(compute_penalty("0 0 1 0", 0), 3)

#     def test_compute_penalty_high(self):
#         self.assertEqual(compute_penalty("0 0 1 0", 4), 1)

#     def test_compute_penalty_mid(self):
#         self.assertEqual(compute_penalty("0 0 1 0", 2), 1)

#     def test_find_best_removal_time(self):
#         self.assertEqual(find_best_removal_time("0 0 1 1"), 2)

#     def test_analyse_agg_logs(self):
#         self.assertEqual(analyse_agg_logs("BEGIN BEGIN \nBEGIN 1 1 BEGIN 0 0\n END 1 1 BEGIN"), [2])

# def test_upper(self):
#     self.assertEqual('foo'.upper(), 'FOO')

# def test_isupper(self):
#     self.assertTrue('FOO'.isupper())
#     self.assertFalse('Foo'.isupper())

# def test_split(self):
#     s = 'hello world'
#     self.assertEqual(s.split(), ['hello', 'world'])
#     # check that s.split fails when the separator is not a string
#     with self.assertRaises(TypeError):
#         s.split(2)

# unittest.main()


# class CustomError(Exception):
#     def __init__(self,ErrorInfo):
#         super().__init__(self) #初始化父类
#         self.errorinfo=ErrorInfo
#     def __str__(self):
#         return self.errorinfo

# if __name__ == '__main__':
#     try:
#         raise CustomError('客户异常')
#     except CustomError as e:
#         print(e)


# class Solution:
#     def minTransfers(self, transactions: List[List[int]]) -> int:

#         tuplify = lambda balance: tuple((k, v) for k, v in balance.items())

#         @lru_cache(None)
#         def dfs(balances):
#             if not balances:
#                 return 0
#             res = math.inf
#             balances = {k: v for k, v in balances}
#             for size in range(2, len(balances) + 1):
#                 # pruning trick
#                 if res <= size - 1: # added
#                     break

#                 for group in itertools.combinations(balances.keys(), size):
#                     if sum(balances[k] for k in group) == 0:
#                         remaining_balances = {k: v for k, v in balances.items() if k not in group}
#                         res = min(res, size - 1 + dfs(tuplify(remaining_balances)))
#                         # pruning trick
#                         if len(group) == 2: # added
#                             return res

#             return res

#         balances = collections.defaultdict(int)
#         for u, v, z in transactions:
#             balances[u] += z
#             balances[v] -= z
#         return dfs(tuplify({k: v for k, v in balances.items() if v}))


# LRU Cache
# class DLinkedNode:

#     def __init__(self):
#         self.value = 0
#         self.prev = None
#         self.next = None

# class DLinkedNode:

#     def __init__(self):
#         self.key = 0
#         self.value = 0
#         self.prev = None
#         self.next = None

# class LRUCache:

#     def _remove_node(self, node):
#         node.prev.next, node.next.prev = node.next, node.prev

#     def _move_to_head(self, node):
#         node.prev, node.next = self.head, self.head.next
#         self.head.next.prev, self.head.next = node, node

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.size = 0
#         self.cache = {}
#         self.head = DLinkedNode()
#         self.tail = DLinkedNode()
#         self.head.next, self.tail.prev = self.tail, self.head

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             node = self.cache[key]
#             self._remove_node(node)
#             self._move_to_head(node)

#             return node.value
#         else:
#             return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             node = self.cache[key]
#             self._remove_node(node)
#             self._move_to_head(node)
#         else:
#             newNode = DLinkedNode()
#             newNode.key = key
#             newNode.value = value
#             self.cache[key] = newNode
#             self._move_to_head(newNode)
#             self.size += 1

#             if self.size > self.capacity:
#                 removeNode = self.tail.prev
#                 self._remove_node(removeNode)
#                 del self.cache[removeNode.key]
#                 self.size -= 1

# # Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(2)
# obj.put(1,1)
# obj.put(2,2)
# print(obj.get(1))
# obj.put(3,3)
# print(obj.get(2))
# obj.put(4,4)
# print(obj.get(1))
# print(obj.get(3))
# print(obj.get(4))

# # ["LRUCache","put","put","get","put","get","put","get","get","get"]
# # [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

# doordash compare tree
class Node:
    def __init__(self, n, k, v):
        self.name = n
        self.key = k
        self.value = v
        self.children = []

def get_node_count(root):
    if root == None:
        return 0
    res = 1
    for node in root.children:
        res += get_node_count(node)
    return res


def compute_diff(old_tree, new_tree) -> int:
    if old_tree is None and new_tree is None:
        return 0
    elif old_tree is None:
        return get_node_count(new_tree)
    elif new_tree is None:
        return get_node_count(old_tree)
    elif old_tree.key != new_tree.key:
        return get_node_count(old_tree) + get_node_count(new_tree)


    ret = 0
    if old_tree.value != new_tree.value:
        ret += 1

    new_tree_children = {c.key: c for c in new_tree.children}
    for old_child in old_tree.children:
        ret += compute_diff(old_child, new_tree_children.pop(old_child.key, None))
    for remaining_new_tree_child in new_tree_children.values():
        ret += get_node_count(remaining_new_tree_child)
    return ret


a = Node("a", 1, True)
b = Node("b", 2, True)
c = Node("c", 3, True)
d = Node("d", 4, True)
e = Node("e", 5, True)
f = Node("f", 6, True)

a.children.append(b)
a.children.append(c)

b.children.append(d)
b.children.append(e)

c.children.append(f)


a1 = Node("a", 1, True)
# b1 = Node("b", 2, True)
c1 = Node("c", 3, False)
# d1 = Node("d", 4, True)
# e1 = Node("e", 5, True)
f1 = Node("f", 66, True)
# g1 = Node("g", 7, False)

# a1.children.append(b1)
a1.children.append(c1)

# b1.children.append(d1)
# b1.children.append(e1)
# b1.children.append(f1)

c1.children.append(f1)

res = compute_diff(a, a1)
print(res)


# Python 3 program for the above approach
# Python3 program to check if two
# strings are k anagram or not.
MAX_CHAR = 26

# Function to check that is
# k-anagram or not
def arekAnagrams(str1, str2, k) :

	# If both strings are not of equal
	# length then return false
	n = len(str1)
	if (len(str2)!= n) :
		return False

	count_dict = [0] * MAX_CHAR

	# Store the occurrence of all
	# characters in a hash_array
	for i in range(n):
		count_dict[ord(str1[i]) - ord('a')] += 1
		count_dict[ord(str2[i]) - ord('a')] -= 1

	count = 0

	# Count number of characters that
	# are different in both strings
	for i in range(MAX_CHAR):
		if (count_dict[i] > 0) :
			count += count_dict[i]

	# Return true if count is less
	# than or equal to k
	return (count <= k)

# Driver Code
if __name__ == '__main__':
	str1 = "geeks"
	str2 = "eggkf"
	k = 2
	if (arekAnagrams(str1, str2, k)):
		print("Yes")
	else:
		print("No")
