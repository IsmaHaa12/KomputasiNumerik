def f(x):
  return x**3-5*x+1
def bisection(a,b,n):
  i=1
  condition = True
  while condition:
    c = (a+b)/2
    if f(c)==0:
      b = c
    else:
      a = c
    print("iterasi ke:",i, "c",c, "f(c):",f(c))
    if i==n:
      condition=False
    else:
      condition=True
      i=i+1
    print("akar yang diperlukan adalah ", c)

a = input("batas bawah: ")
b = input("batas atas: ")
n = input("jumlah iterasi: ")
a = float(a)
b = float (b)
n = int(n)

if f(a)*f(b)>0:
  print("batas yang dimasukkan tidak berada pada range akar")
  print("coba lagi dengan nilai yang berbeda")
else:
  bisection (a,b,n)