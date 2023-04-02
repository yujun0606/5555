# 함수
# 이유 : 코드 간결하게

# 함수 정의
def hello():
    print('안녕하세요') # 함수 기능
    print('파이썬')

# 함수 호출
hello()
hello()

# 주소함수
def address():
    print('서울시')
    print('종로구')
address()
print(type(address()))

print('----------------------')

def address():
    return '서울시 종로구'
print(type(address()))
