from sys import stdin
R, C = map(int, stdin.readline().split())
dx = [0,0,1,-1]
dy = [-1,1,0,0]
board = [list(stdin.readline()) for _ in range(R)]
check = [False] * 26 #알파벳 수만


def go(board, check, x, y , cnt):
    ans=0
    if cnt>ans: ans = cnt
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0<=nx<R and 0<=ny<C :
            ch = ord(board[nx][ny])-ord('A') #아스키값 계산
            if check[ch] is False:
                check[ch] = True
                temp = go(board, check, nx, ny, cnt+1)
                if ans<temp:
                    ans = temp
                check[ch] = False
    return ans+1
check[ord(board[0][0])-ord('A')] = True
print(go(board, check, 0,0,0))