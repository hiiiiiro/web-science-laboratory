# coding : utf-8
import math
import time

data_t = list()
FILE_NUM = 10


def input_d(file: str):
    term = dict()
    with open(file, 'r', encoding="shift-JIS") as f:
        for line in f:
            line = line.rstrip('\n')
            if line in term:
                term[line] += 1
            else:
                term[line] = 1
    data_t.append(term)


def output_d(text, ver):
    with open(text, 'w') as fout:
        for key, value in data_t[ver].items():
            fout.write(f'{key}\t{tf_cal(key, value)}\n')


def tf_cal(term, freq):
    count = 0
    i = 0
    while i < len(data_t):
        if term in data_t[i]:
            count += 1
        i += 1
    res = freq * math.log(len(data_t) / count)
    return res


t1 = time.time()
for num in range(FILE_NUM):
    input_d('/Users/user/documents/input/{}.txt'.format(num))

for num in range(FILE_NUM):
    output_d('{}.txt'.format(num), num)

t2 = time.time()
elapsed_time = t2 - t1
print(f"経過時間：{elapsed_time}秒")
