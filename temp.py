
def k_frequent_word(input_text, k):
    res = []

    words = input_text.split(" ")

    word_dic = {}

    for word in words:
        if word not in word_dic:
            word_dic[word] = 1
        else:
            word_dic[word] += 1

    word_dic = sorted(word_dic.items(), key=lambda x: x[1])

    for i in range(k):
        res.append(word_dic[i][0])

    return res

o(nlogn)


