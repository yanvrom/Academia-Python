dist = int(input('Quantos km deseja percorrer? '))
if dist <= 200:
    preco = (dist * 0.50)
    round(preco, 2)
if dist > 200:
    preco = ((100.00 + (dist - 200)*0.45))
    round(preco, 2)
    
print("%.2f" % preco)