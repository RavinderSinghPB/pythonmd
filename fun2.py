from gettext import dpgettext


def sellprice(mrp,discp):
    discount=(mrp*discp)/100
    sellingprice=mrp-discount
    return sellingprice

#mrp=1000
#discp=10


print(sellprice(1000,10))




