import re
mul_re = re.compile(r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)')
cond_mul_re = re.compile(r'(?:(mul)\((\d{1,3}),(\d{1,3})\))|(?:(do)\(\))|(?:(don\'t)\(\))')
with open('day3_input1') as f:
  buffer = f.read()
  sum = 0
  for i in mul_re.finditer(buffer):
    sum += int(i.group(1)) * int(i.group(2))
  print(f"sum = {sum}")
  sum = 0
  count_mul = True
  for i in cond_mul_re.finditer(buffer):
    print(i.group(0))
    if i.group(0) == 'do()':
      print("do")
      count_mul = True
    elif i.group(0) == 'don\'t()':
      print("dont")
      count_mul = False
    elif i.group(1) == 'mul':
      if count_mul:
        sum += int(i.group(2)) * int(i.group(3))
  print(f"cond sum = {sum}")

