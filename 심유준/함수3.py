def triple(a = 5):
    result = a * 3
    return result
print(triple(2))
print(triple())

# 다수 연산 값 리턴
def cal(a, b):
    return a + b, a - b, a / b, a * b, a % b
print(cal(2, 3))
print(type(cal(2, 3)))

# 1~10까지의 합계를 함수로 작성!

def get_sum(start, end):
    sum = 0
    for i in range(start, end + 1):
        sum = sum + i
    return sum
print(get_sum(1, 10))
    
