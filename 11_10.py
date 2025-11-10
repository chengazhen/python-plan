# 将整数转换为浮点数并打印结果
f = float(2)
print(f)

print(eval("2 + 3"))

# 三元表达式
x = 10
y = 11
print('三元表达式晦涩难懂') if x > y else print("通俗易懂")

# 猜拳小游戏

# person = int(input("请输入你要出的拳（石头0/剪刀1/布2）："))

# import random

# compute = random.randint(0,2)

# print('你赢了')

# count = 0

# while(count < 100):
#   print(f'{count}')
#   count += 1


# 罚你三天，每天跪三次榴莲
# i = 0 

# while(i < 2):
#   print(f'第{i}天')
#   i += 1
#   y = 0
#   while(y < 2):
#     print(f'第{i}天跪{y}次跪榴莲')
#     y += 1

# for i in range(5):
#   print(f'当前是第{i}次循环')


# for i in range(5):
#   if i == 2:
#     break
#   print(f'当前是第{i}次循环')

for i in range(6):
  if i == 2:
    continue
  print(f'当前是第{i}次循环')