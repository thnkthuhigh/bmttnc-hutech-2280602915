def truy_cap_phan_tu(tupledata):
    firstelenment=tupledata[0]
    lastelenment=tupledata[-1]
    return firstelenment,lastelenment

inputtuple= eval(input("Nhập tuple, ví dụ (1,2,3):"))
first,last=truy_cap_phan_tu(inputtuple)

print("Phần tử đầu:",first)
print("Phần tử cuối:",last)