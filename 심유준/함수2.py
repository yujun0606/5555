# 함수 예제2
def ni_er():
    return 3.14
print(ni_er())
print(type(ni_er()))

# 예제3
def return_test():
    return 100
print(return_test())

print()

def return_test():
    return
print(return_test())

# 매개변수 vs 인자
def address(name): # 매개변수
    print('서울시')
    print('종로구')
    print(name)
address('홍길동')# 인자
address('파이썬')
