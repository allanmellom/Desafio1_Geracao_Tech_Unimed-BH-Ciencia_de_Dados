#A empresa que você trabalha resolveu conceder um aumento salarial a todos funcionários, de acordo com a tabela abaixo:
#Salário					Percentual de Reajuste
#0 - 600.00					17%
#600.01 - 900.00			13%
#900.01 - 1500.00			12%
#1500.01 - 2000.00			10%
#Acima de 2000.00			5%
#Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.
#A entrada contém apenas um valor de ponto flutuante, que pode ser maior ou igual a zero, com duas casas decimais, conforme exemplos abaixo.

salario = int(input()) 
if salario>=0 and salario<=600:
	percentual=17
	novo=salario+(salario*0.17)
	novo=f'{novo:.2f}'
	reajuste=(salario*0.17)
	reajuste=f'{reajuste:.2f}'
elif salario>600 and salario<=900:
	percentual=13
	novo=salario+(salario*0.13)
	novo=f'{novo:.2f}'
	reajuste=(salario*0.13)
	reajuste=f'{reajuste:.2f}'
elif salario>900 and salario<=1500:
	percentual=12
	novo=salario+(salario*0.12)
	novo=f'{novo:.2f}'
	reajuste=(salario*0.12)
	reajuste=f'{reajuste:.2f}'
elif salario>1500 and salario<=2000:
	percentual=10
	novo=salario+(salario*0.10)
	novo=f'{novo:.2f}'
	reajuste=(salario*0.10)
	reajuste=f'{reajuste:.2f}'
else: 
	percentual=5
	novo=salario+(salario*0.5)
	novo=f'{novo:.2f}'
	reajuste=(salario*0.5)
	reajuste=f'{reajuste:.2f}'	
print(f'Novo salario: {novo}\nReajuste ganho: {reajuste}\nEm percentual: {percentual} %')