# 캐릭터가 있는 장소는 N * M 크기의 직사각형
# 각각의 칸은 육지 혹은 바다
# 캐릭터는 동서남북 중 한 곳을 바라봄
# (A, B) A: 북쪽으로부터 떨어진 칸의 개수, B: 서쪽으로부터 떨어진 칸의 개수 (A는 y, B: x)
# 바다로 되어 있는 공간엔 갈 수 없음

# 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을  정함
# 바로 왼쪽방향에 가보지 않은 칸이 존재하면 왼쪽 방향으로 회전 + 왼쪽으로 한 칸 전진
# 왼쪽 방향에 가보지 않은 칸이 없으면 왼쪽 방향으로 회전만
# 네 방향 모두 이미 가본 칸, 바다칸이면 바라보는 방향 유지한 채 한칸 뒤로
# 뒤쪽 방향이 바다인 칸이라 뒤로 못가면 움직임 멈춤

# 0은 육지, 1은 바다
# 캐릭터가 방문한 칸의 수를 출력
# 캐릭터가 있는 칸의 좌표(N, M)와 바라보는 방향 d가 각각 서로 공백으로 구분되어 주어짐
# 0: 북, 1: 동, 2: 남, 3: 서
N, M = map(int, input().split())
n, m, d = map(int, input().split())
game_map = []
for i in range(N):
  maps = list(map(int, input().split()))
  game_map.append(maps)
#[[1, 0, 1, 0],[1, 1, 0, 0]]
# (1, 1)이면 1번째 리스트의 1번째 요소에 있다는 말

#방위
dA = [-1, 0, 1, 0]
dB = [0, 1, 0, -1]


def turn_left():
  global d
  d -= 1
  if d == -1:
    d = 3


count = 1
turn_time = 0
game_map[n][m] = 1  #시작위치 1로 바꾸고 시작
while True:
  turn_left()
  nn = n + dA[d] - 1
  nm = n + dB[d] - 1
  if game_map[n + dA[d] - 1][m + dB[d] - 1] == 1:
    turn_time += 1  #방향 바꾼 횟수 설정
  else:
    game_map[nn][nm] = 1
    n = nn
    m = nm  # 이동시키기
    count += 1
    turn_time = 0  #초기화
    pass
  if turn_time == 4:  #4번 다 봤는데 아닐 경우
    nn = n - dA[d]  # 바라보는 방향 유지한 태로 한칸 뒤로가기
    nm = m - dB[d]
    if game_map[nn][nm] == 0:  #육지면 이동
      n = nn
      m = nm
    else:
      break
    turn_time = 0  #방향 전환 초기화

print(count)
