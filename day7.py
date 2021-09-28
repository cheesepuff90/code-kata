def more_than_half(nums):
  num_dic = {}

  for i in nums:
    if i not in num_dic:
      num_dic[i] = 1
    num_dic[i] += 1
  
  ans = max(num_dic, key=num_dic.get)

  return ans

  # over_half = len(nums)//2

  # for num in nums:
  #   count = sum(1 for i in nums if i == num)
  #   if count >= over_half:
  #     return num


# 숫자로 이루어진 배열인 nums를 인자로 전달합니다.

# 숫자중에서 과반수(majority, more than a half)가 넘은 숫자를 반환해주세요.

# 예를 들어,

# nums = [3,2,3]
# return 3

# nums = [2,2,1,1,1,2,2]
# return 2