import math 

h = float(input('Qual a altura do líquido?'))
r = 1.30
L = 6
if h < 0 or h > 2 * r:
    print("Altura inválida. Deve estar entre 0 e 2 vezes o raio.")
else: 
    def volume_cilindro(h, L, r):
        
        area_h = r**2 * math.acos((r - h) / r) - (r - h) * math.sqrt(2 * r * h - h**2)

        volume = area_h * L

        return volume 

    print(f"O volume do cilindro deitado é {volume_cilindro(h, L, r):.4f} m³")