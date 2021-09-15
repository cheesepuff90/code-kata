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
  
  
  
#   String 형인 str 인자에서 중복되지 않은 알파벳으로 이루어진 제일 긴 단어의 길이를 반환해주세요.
  
#   str = "abcabcabc"
#   return 은 3
#   => 'abc' 가 제일 길기 때문
  
#   str = "aaaaa"
#   return 은 1
#   => 'a' 가 제일 길기 때문
  
#   str = "sttrg"
#   return 은 3
#   => 'trg' 가 제일 길기 때문

