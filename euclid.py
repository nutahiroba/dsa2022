def euclid(m, n):
    # 課題１
  if(n > m):
    m,n = n,m
  while (n != 0):
    r = m % n
    m =n
    n = r

  return m

if __name__=='__main__':
    print(euclid(3,9))
    print(euclid(630,30))
    print(euclid(23566,2345))
