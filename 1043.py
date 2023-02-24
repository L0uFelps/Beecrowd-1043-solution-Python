entrada = input().split()
entradaFloat = [float(i) for i in entrada]

a,b,c = entradaFloat

if a + b > c and a + c > b and b + c > a:
    p = a + b + c
    print("Perimetro = {:.1f}".format (p))
else:
    at = ((a + b) / 2) * c
    print("Area = {:.1f}".format (at))