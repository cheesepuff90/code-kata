def get_prefix(strs):
  ans = ''
  
  if len(strs) == 0:
    return ''

  strs = sorted(strs)
  for idx,i in enumerate(strs[0]):
    if i == strs[-1][idx]:
      ans += i
    else:
      break
  
  return ans


# strs은 단어가 담긴 배열입니다.

# 공통된 시작 단어(prefix)를 반환해주세요.

# 예를 들어

# strs = ['start', 'stair', 'step']
# return은 'st'

# strs = ['start', 'wework', 'today']
# return은 ''