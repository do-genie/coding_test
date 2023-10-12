# 1. 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
# 2. 선택된 행에 포함된 카드 중 가장 숫자가 낮은 카드 뽑기
# 3. 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략 세우기

#전략
#행별로 가장 작은 숫자 선택한다
#가장 작은 행 숫자를 반환한다.

n, m = map(int, input().split())
# 숫자의 카드들은 N * M 형태로 놓여있다. N은 행, M은 열
result = 0
for i in range(n):
  data = list(map(int, input().split()))
  min_val = min(data)
  result = max(result, min_val)
  #크면 넣고 아님 말기

print(result)
