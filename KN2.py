def f(x):
  return x**3-5*x+1
def bisection(a,b,e):
  i=1
  x=0
  condition = True
  while condition:
    g=f(x)
    x = (a+b)/2
    if f(x)==0:
      b = x
    else:
      a = x
    print("iterasi ke:",i, "c",x, "f(c):", f(x))
    i=i+1
    condition-abs (f(x)-g)>e
    print("akar yang diperlukan: ",x)
a = input("batas bawah: ")
b = input("batas atas: ")
e = input("error yang diperbolehkan: ")
a = float(a)
b = float (b)
e = float(e)

if f(a) *f(b)>0:
  print("batas yang dimasukkan tidak berada pada range akar")
  print("coba lagi dengan nilai yang berbeda")
else:
  bisection (a,b,e)