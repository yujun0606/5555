a = int(input("윗변의 길이를 입력하세요"))
b = int(input("밑변의 길이를 입력하세요"))
c = int(input("높이를 입력하세요"))
def s(a, b, c):
    area = ((a + b) * c) / 2
    return area
d = (s(a, b, c))
print(f'사다리꼴의 면적은 {d}입니다.')


