def pagamento(salario):
    salario = float(input("Digite seu salário: "))
    bonus = salario * 0.5
    pagamento = salario + bonus
    return(pagamento)

p = pagamento(pagamento)
print(f"Seu pagamento após o bônus é: {p}")