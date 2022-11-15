# first basic encryption program using modular arithmetic
# version 0.01
# the program already is incomplete

print("equação y=a^x mod p, p é um numero primo")
print("lista de primos, https://docs.google.com/spreadsheets/d/1wQJX5oJKWVeQuDB7R4Gw5mqXIxlicX_JC5BN6ql7oa8/edit?usp=sharing")
u=input("aritmética modular, primo superior a 127: ")
p=int(u)
is_prime=True
for x in range(2,int(p)):
    if int(p)%x==0:
        is_prime=False
        break
if is_prime:
    v =input("valor a: ")
    a=int(v)

    for x in range(1, 127):
        if pow(a, x) % p > 32:
            print(" ", chr(x), "", chr(pow(a, x) % p), pow(a, x) % p, hex(pow(a, x) % p))
        else:
            # em nova versão corrigir pq pode gerar tabelas com o mesmo simbolo repetido
            print(" ", chr(x), "", chr(pow(a, x) % p + 32), pow(a, x) % p + 32, hex(pow(a, x) % p + 332))
else:
    print("p não é primo. Escolha um p primmo")



