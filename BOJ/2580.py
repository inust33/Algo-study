from sys import stdin
#백트래킹 문제
n = 9
a = [list(map(int, stdin.readline().split())) for _ in range(n)]
check_col = [[False] * 10 for _ in range(n)] #i번째 열에 j가 있ㅇ면 True
check_row = [[False]*10 for _ in range(n)] # i번째 행에 숫자 j가 있으면 True
check_square = [[False] *10 for _ in range(n)] #i번 정사각형에 숫자 j가 있으면 True i= (x//3)*3 +y/3 2
def squaure(i,j):
    return (i//3)*3 + j//3
def go(z): ## 1부터 81까
    if z== 81:
        for row in a:
            print(' '.join(map(str, row)))
        return True
    x = z//n #x행
    y= z%n #y열
    if a[x][y]!=0:
        go(z+1)
    else:
        for i in range(1,10):
            if check_col[y][i] is False and check_row[x][i] is False and check_square[squaure(x,y)][i] is False:
                check_col[y][i] = check_row[x][i] = check_square[squaure(x,y)][i] = True
                a[x][y] = i
                if go(z+1):
                    return True
                a[x][y] = 0
                check_col[y][i] = check_row[x][i] = check_square[squaure(x, y)][i] = False
    return False
for i in range(n):
    for j in range(n):
        if a[i][j] !=0:
            check_col[j][a[i][j]] = True
            check_row[i][a[i][j]] = True
            check_square[squaure(i,j)][a[i][j]] = True

go(0)