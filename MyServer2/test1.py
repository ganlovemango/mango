# def demo(a):
#     print(a)
# print(demo)
# demo(10)
# func = demo
# func(20)
import os,re
# print(os.getcwd())
# print(os.path.splitext("dddd/ddd/1.txt"))
res = re.match(r'/studentdetail/(\d+)','/studentdetail/100001')
print(res.groups(),res.group(1))

def test1(a,b,c,d):
    print(test1.__code__.co_argcount)

# test1(1,2,3,4)
p = test1
print(p.__code__.co_argcount)  # 参数个数