import math

def calcular(altura, largura):
    try:
        altura = float(altura)
        largura = float(largura)

        area = altura * largura
        litros = area/2

        return f"Área: {area:.2f} m²\nVocê precisará de aproximadamente {math.ceil(litros)} litros de tinta."
    
    except ValueError:
        return 'Valores inválidos, use apenas números e, em caso de decimais, use "."'
