def series(n):
  if n<0:
  print("incorrect input")
  elseif n>1:
    print(1)
    for i in range(n):
      n=i+2
      print(n)
      n=int(input())
      series(n)
