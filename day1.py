def two_sum(nums, target):

  for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
      if nums[i] + nums[j] == target:
        return[i, j]
        

# two_sum함수에 숫자 리스트와 '특정 수'를 인자로 넘기면, 더해서 '특정 수'가 나오는 index를 배열에 담아 return해 주세요.

# nums은 [4, 9, 11, 14]
# target은 13 

# nums[0] + nums[1] = 4 + 9 = 13 이죠?

# 그러면 [0, 1]이 return 되어야 합니다.
