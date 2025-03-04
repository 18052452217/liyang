# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

name = "abc"
def print_hi2():
    global name
    name = "abc2"
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def print_hi3():
    a = 10
    b = 11
    c = 12
    list1 = (a, b, c)
    a, b, c = c, a, b
    print(list1)  # Press ⌘F8 to toggle the breakpoint.
    return a, b, c

print(print_hi3())

def demo(num, name = "a",num_list = (10,11)):

    print("函数内部")

    # 赋值语句
    num = 200
    num_list = [1, 2, 3]

    print(num)
    print(num_list)

    print("函数代码完成")


gl_num = 99
gl_list = [4, 5, 6]
gl_list.sort(reverse=True)
demo(gl_num,"")
print(gl_num)
print(gl_list)

def demo2(num, *args, **kwargs):

    print(num)
    print(args)
    print(kwargs)

demo2(1, 2, 3, 4, 5, name="小明", age=18, ab={"a":"b","b":"c"}, **{"a":"b","b":"c"})


class My_Demo:
    def __new__(cls, *args, **kwargs):
        print("new")
        return super().__new__(cls)
    def __init__(self):
        self._name = "小明"
        self.__age = 18

demo1 = My_Demo()
print(demo1._name)
print(demo1._My_Demo__age)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print_hi2()

print(100)
##print(100,20)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
