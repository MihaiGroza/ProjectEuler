x=1
y =1
Multp_of_3 = []
Multp_of_5 = []
i=0
f=0
while i < 1000:
    i=3*x
    Multp_of_3.append(i)
    x=x+1

while f < 1000:
    f = 5*y
    Multp_of_5.append(f)
    y=y+1

list_of_multiples = Multp_of_5[:-1] + Multp_of_3[:-1]
list_of_multiples = list(set(list_of_multiples))
result = sum(list_of_multiples)
print(list_of_multiples)
print(result)
