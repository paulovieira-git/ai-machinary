print("equação y=a^x mod p, p é um numero primo")
p=input("aritmética modular: ")
is_prime=True
for x in range(2,int(p)):
    if int(p)%x==0:
        is_prime=False
        break
if is_prime:
    a =input("valor a: ")
    y=input("valor y: ")

    print("soluções x:")
    val=True
    for x in range(1,int(p)):
        if int(y)==(pow(int(a),int(x))%int(p)):
            val=False
            print(x)
    if val:
        print("sem solução")
else:
    print("p não é primo. Escolha um p primmo")
