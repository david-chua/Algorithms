# def duplicates(arr):
#     if len(arr) <=1:
#         return 0
#     counter_arr = [0] * (max(arr)+1)
#
#     for num in arr:
#         counter_arr[num] += 1
#
#     duplicate_count = 0
#     for num in counter_arr:
#         duplicate_count += num //2
#     return duplicate_count
# def duplicates(arr):
#     if len(arr) <=1:
#         return 0
#     counter_dict = {}
#
#     for num in arr:
#         if num not in counter_dict:
#             counter_dict[num] = 1
#         else:
#             counter_dict[num] += 1
#
#     duplicate_count = 0
#     for value in counter_dict.values():
#         duplicate_count += value //2
#     return duplicate_count

def palindrome(n):
    
