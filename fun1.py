from gettext import dpgettext


def sellprice(mrp,discp):
    discount=(mrp*discp)/100
    sellingprice=mrp-discount
    return sellingprice

mrp=1000
discp=10


sp=sellprice(mrp,discp)
print(sp)



