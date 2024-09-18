def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento basado en el monto total y el porcentaje de descuento.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento
# Llamadas a la función
# Primera llamada: porcentaje de descuento por defecto (10%)
monto_total1 = 500
descuento1 = calcular_descuento(monto_total1)
monto_final1 = monto_total1 - descuento1

# Segunda llamada: monto total y porcentaje de descuento especificado (20%)
monto_total2 = 1700
porcentaje_descuento2 = 20
descuento2 = calcular_descuento(monto_total2, porcentaje_descuento2)
monto_final2 = monto_total2 - descuento2

# Mostrar los resultados
print(f"Para un monto total de ${monto_total1} descuento del 10%:")
print(f"Descuento: ${descuento1:.2f}")
print(f"Monto final a pagar: ${monto_final1:.2f}\n")

print(f"Para un monto total de ${monto_total2} descuento del {porcentaje_descuento2}%:")
print(f"Descuento: ${descuento2:.2f}")
print(f"Monto final a pagar: ${monto_final2:.2f}")
