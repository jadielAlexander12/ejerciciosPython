pesos_comlombianos=float(input("indica la  cantidad en colombianos"))
soles_peruanos=float(input("indica la  cantidad en soles peruanos"))
reales_brasil=float(input("indica la  cantidad brasil"))

pesosco_a_dolar = pesos_comlombianos * 0.00025
soles_a_dolar = soles_peruanos * 0.27
reales_dolar = reales_brasil * 0.19

resultado= pesosco_a_dolar + soles_a_dolar + reales_dolar 
print("tu dinero es: ", resultado) 