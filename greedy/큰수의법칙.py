# 다양한 수가 있을 때, 주어진 수를 M번 더해 가장 큰 수를 만든다
# K번 연속으로 초과해서 더해질 수는 없다.
# 즉, 배열 중 가장 큰 수를 k번 더하고, 다음으로 작은 수를 1번 더한다. 그 뒤로 가장 큰 수를 다시 k번 더하고 1번 더한다.
# 이 때, M만큼인지 확인한다.
n, m, k = map(int, input().split())
# n은 자연수 개수, m은 더해야하는 횟수, k는 연속으로 더할수 있는 횟수
data = list(map(int, input().split()))
#data는 자연수 배열

sum = 0
num = 0
data = sorted(data, reverse=True)
while num != m:
  for j in range(k):
    sum += data[0]
    num += 1
    if num == m:
      break
  if num == m:
    break
  sum += data[1]
  num += 1

print(sum)

#큰수가 총 더해지는 횟수
#횟수계산한 뒤, 곱해서 값을 내는 방법이 100억개 이상의 데이터 사용 시 시간복잡도 줄일 수 있음
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * data[0]
result += (m - count) * data[1]

print(result)
