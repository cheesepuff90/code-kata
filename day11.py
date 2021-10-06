def complex_number_multiply(a, b):
  # num1 = a[:-1].split('+')
  # num2 = b[:-1].split('+')

  # a1 = int(num1[0])
  # a2 = int(num1[1])

  # b1 = int(num2[0])
  # b2 = int(num2[1])

  a1, a2 = map(int, a[:-1].split('+'))
  b1, b2 = map(int, b[:-1].split('+'))

  return(f'{a1*b1 - a2*b2}+{a1*b2 + a2*b1}i')


# 두 개의 input에는 복소수(complex number)가 string 으로 주어집니다. 복소수란 a+bi 의 형태로, 실수와 허수로 이루어진 수입니다.

# input으로 받은 두 수를 곱해서 반환해주세요. 반환하는 표현도 복소수 형태의 string 이어야 합니다.

# 복소수 정의에 의하면 (i^2)는 -1 이므로 (i^2) 일때는 -1로 계산해주세요.

# 제곱 표현이 안 되어 i의 2제곱을 (i^2)라고 표현했습니다.