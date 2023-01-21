# 1157
# 단어공부
# dictionary 생성과 요소추가
# method : get(x), values(), items()
'''
Mississipi
'''

input_str = input().upper()

dict = {}

for x in input_str:
  if dict.get(x):
    dict[x] += 1
  else:
    dict[x] = 1

dict_max = 0
max_num = 0
max_alphabet = ''

for k, v in dict.items():
  if dict_max < v:
    dict_max = v

for k, v in dict.items():
  if v == dict_max:
    max_num += 1
    max_alphabet = k


if max_num > 1:
  print('?')
else:
  print(max_alphabet)
