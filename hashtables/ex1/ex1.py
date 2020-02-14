#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)
    index = 0
    for weight in weights:
        hash_table_insert(ht, weight, (weight, index))
        index += 1

    for weight in weights:
        needed = limit - weight
        w1 = hash_table_retrieve(ht, needed)
        if w1 is not None:
            w2 = hash_table_retrieve(ht, limit - w1[0])
            if w1 is not None:
                w1_index = w1[1]
                w2_index = w2[1]
            if w1_index > w2_index:
                return((w1_index, w2_index))
            else:
                return(w2_index, w1_index)

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


weights_3 = [4, 6, 10, 15, 16]
answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
answer_3[0] == 3
answer_3[1] == 1

answer_3


weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
answer_4[0] == 6
answer_4[1] == 2

answer_4

# passed first 2
#
# def get_indices_of_item_weights(weights, length, limit):
#     ht = HashTable(16)
#     index = 0
#     for weight in weights:
#         hash_table_insert(ht, weight, index)
#         index += 1
#
#     w1_index = 0
#     indices = []
#     for weight in weights:
#         needed = limit - weight
#         w2_index = hash_table_retrieve(ht, needed)
#         if w2_index:
#             if w2_index != w1_index:
#                 indices = [w2_index, w1_index]
#         else:
#             w1_index += 1
#     if indices == []:
#         return(None)
#     else:
#         w1 = indices[0]
#         w2 = indices[1]
#         if w1 > w2:
#             ans = (w1, w2)
#         else:
#             ans = (w2, w1)
#     return ans
#
#
# def print_answer(answer):
#     if answer is not None:
#         print(str(answer[0] + " " + answer[1]))
#     else:
#         print("None")
