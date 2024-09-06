import math 

d = 263

r = d / 2

l = float(607)

for alt in range(0, 264):
    vCone = ((308.219 * alt) * 2) / 100
    a = pow(r, 2)
    b = math.acos(1 - (alt / r))
    c = math.sqrt((2 * alt * r) - (alt * alt))
    d = (r - alt)
    aBase = ((a * b) - (c * d))
    volume = (aBase * l) / 1000
    vFinal = volume + vCone

    print(f"Altura = {alt:.0f} | Vol. Cone = {vCone:.2f} | Volume Cilindro = {volume:.2f} | Volume Final = {vFinal:.2f}")