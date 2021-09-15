def reverse(number):

  minus = 1
  if number < 0:
    number *= -1
    minus = -1

  result = 0
  for _ in range(len(str(number))):
      result += (number % 10)
      result *= 10
      number = number // 10
  result /= 10

  return minus * result
  
  
# reverse 함수에 정수인 숫자를 인자로 받습니다.

# 그 숫자를 뒤집어서 return해주세요.

# x: 숫자

# return: 뒤집어진 숫자를 반환!

# 예들 들어,

# x: 1234
# return: 4321

# x: -1234
# return: -4321

# x: 1230
# return: 321
