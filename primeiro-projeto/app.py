aparelho = input("qual é o nome do aparelho: ")
potencia = float(input("qual o número da potência em watts (W)"))
tempomedio = float(input("qual o tempo médio em horas"))
consumomensal = (potencia * tempomedio * 30) / 1000
print(f"aparelho: {aparelho}")
print(f"consumo estimado: {consumomensal} kWh/mês")