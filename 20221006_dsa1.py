def cuclid(n,m):
  if(n > m):
    m,n = n,m
  while (n != 0):
    r = m % n
    m =n
    n = r

  return m

print(cuclid(200,30))