def get_len_of_str(s):
    # 아래 코드를 작성해주세요.
    #주형님 코드
    # result=int(0)
    # cnt=int(0)
    # letters=str()
    # for i in range(len(s)):
    #   if s[i] not in letters:
    #     letters+=s[i]
    #     print(letters)
    #     cnt+=1
    #     if result < cnt:
    #       result=cnt
    #   else:
    #     letters=s[i]
    #     cnt=1
    # return result

    

  strs = {}
  new = str()

  for i in range(len(s)):
    if s[i] in new:
      strs[new] = len(new)
      new = str()
      new += s[i]
    else:
      new += s[i]

    
    if i == len(s) - 1:    #마지막 인덱스일 경우엔 여태껏 담아왔던 요소들을 딕셔너리에 추가한다
      strs[new] = len(new)

  if strs == {}:
    ret = 0

  else:
    ret = max(strs.values())

  return ret