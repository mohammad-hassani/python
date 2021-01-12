import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "!@#$%^&*()[]?/><'\|:;=+_-`~"

make= lower+upper+number+symbol
tol=12

pas = "".join(random.sample(make,tol))
print(pas)