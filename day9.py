def top_k(nums, k):

  num_dict = {num:nums.count(num) for num in nums}

  # sort_dict = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)
  # ans = []
  
  # for key, value in sort_dict:
  #   ans.append(key)
  # return ans[:k]
  
  return [a for a, b in sorted(num_dict.items(), key=lambda x: x[1], reverse=True)[:k]]


# nums는 숫자로 이루어진 배열입니다.

# 가장 자주 등장한 숫자를 k 개수만큼 return 해주세요.

# nums = [1,1,1,2,2,3],
# k = 2

# return [1,2]

# nums = [1]
# k = 1

# return [1]