def is_valid(s):
	left = ['(', '[', '{']
	right = [')', ']', '}']
	stack = []

	for i in s:
		if i in left:
			stack.append(i)
		elif i in right:
			if len(stack) == 0:
				return False
			if left.index(stack.pop()) != right.index(i):
				return False
	return len(stack) == 0


# s는 여러 괄호들로 이루어진 String 인자입니다. s가 유효한 표현인지 아닌지 true/false로 반환해주세요.

# 종류는 '(', ')', '[', ']', '{', '}' 으로 총 6개 있습니다. 아래의 경우 유효합니다.

# 한 번 괄호를 시작했으면, 같은 괄호로 끝내야 한다. 괄호 순서가 맞아야 한다.

# 예를 들어 아래와 같습니다.

# s = "()"
# return true

# s = "()[]{}"
# return true

# s = "(]"
# return false

# s = "([)]"
# return false

# s = "{[]}"
# return true