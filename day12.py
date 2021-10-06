def reverse_string(s):
  for i in range(len(s)//2):
    s[i], s[-i-1] = s[-i-1], s[i]
  
  return s

  # a, b = 0, len(s) - 1

  # while a < b:
  #   s[a], s[b] = s[b], s[a]
  #   a += 1
  #   b -= 1
  # return s


#   문자로 구성된 배열을 input으로 전달하면, 문자를 뒤집어서 return 해주세요.

# 새로운 배열을 선언하면 안 됩니다.
# 인자로 받은 배열을 수정해서 만들어주세요.

# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]