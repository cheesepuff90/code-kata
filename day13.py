def min_path_sum(grid):
  
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if i == 0 and j == 0:
        continue
      elif i == 0:
        grid[i][j] += grid[i][j-1]
      elif j == 0:
        grid[i][j] += grid[i-1][j]
      else:
        grid[i][j] += min(grid[i-1][j], grid[i][j-1])
      print(grid)

  return grid[-1][-1]


#   양수로 이루어진 m x n 그리드를 인자로 드립니다. 상단 왼쪽에서 시작하여, 하단 오른쪽까지 가는 길의 요소를 다 더했을 때,가장 작은 합을 찾아서 return 해주세요.

# 한 지점에서 우측이나 아래로만 이동할 수 있습니다.

# Input: [    [1,3,1],    [1,5,1],    [4,2,1] ]

# Output: 7

# 설명: 1→3→1→1→1 의 합이 제일 작음