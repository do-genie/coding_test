# 어떤 수 N이 1이 될 때까지 두가지 과정중 하나 반복 가능
# 1. N에서 1을 빼거나
# 2. N을 K로 나누거나 -> 이때는 N이 K로 나누어 떨어질 때만 가능

#전략
# N을 K로 나눈 값 -> 2번 실행 횟수
# N을 K으로 나눈 나머지 값 -> 1번의 실행 횟수

n, k = map(int, input().split())
result = 0
result += n % k
while True:
  if n < k:
    break
  else:
    n = n // k
    result += 1

print(result)
