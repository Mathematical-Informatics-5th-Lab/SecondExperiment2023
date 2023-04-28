#指の数を対応させる場合
def code_id_fingar_sum(list):
    return sum(list)


#指の形を対応させる場合
def code_id_fingar_shape(list):
    id = 0
    for i in len(list):
        id += int(list[i]) * 2^i
    return id
