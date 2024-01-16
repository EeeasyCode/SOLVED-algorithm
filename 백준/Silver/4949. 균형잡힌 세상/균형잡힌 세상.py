while True:
  s = input()
  q = ['']
  if s=='.': break
  else:
      for w in s:
          if w=='[' or w=='(':
              q.append(w)
          elif w==']':
              if q[-1]=='[':
                  q.pop()
              else: q.append(w);break
          elif w==')':
              if q[-1]=='(':
                  q.pop()
              else: q.append(w);break
      print('no' if q[-1] else 'yes')