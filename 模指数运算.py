
#   课本上的模指数运算
# b, n, m = map(int, input().split())
# s = str(bin(n))[2:]
# x = 1
# power = b % m
# for i in s[::-1]:
#     if i == '1':
#         x = (x * power) % m
#     power = (power*power) % m
# print(x)



#   范神的模指数运算
b, n, m = map(int, input().split())
ans = 1
for i in range(1,n+1):
    ans = (ans * b) % m
print(ans)