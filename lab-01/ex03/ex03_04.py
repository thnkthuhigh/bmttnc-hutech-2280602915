def truycapphantu(tupledata):
    firstelenment=tupledata[0]
    lastelenment=tupledata[-1]
    return firstelenment,lastelenment

inputtuple= eval(input("nhap tuple,vi du (1,2,3):"))
first,last=truycapphantu(inputtuple)

print("phan tu dau:",first)
print("phan tu cuoi:",last)