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