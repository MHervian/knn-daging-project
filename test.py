# from collections import Counter

# def most_frequent(List): 
#     occurence_count = Counter(List) 
#     # return occurence_count.most_common(1)[0][0] 
#     return occurence_count.most_common(1)[0][0]

# arr = [
#     'Daging Sapi',
#     'Daging Sapi',
#     'Daging Babi',
#     'Daging Sapi',
#     'Daging Babi',
#     'Daging Babi',
#     'Daging Sapi',
# ] 
# print(most_frequent(arr)) 

arr = [1,2,3]

print(arr)

arr1 = [(8, 4),(7, 5)]

arr.append(list(arr1[0])[1])
arr.append(list(arr1[1])[1])

print(arr)