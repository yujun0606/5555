s23 = 1276000
s233 = s23 // 24
print(f'{s233}원')

a = "EVERLAND"
b = a[4 : 6]
c = a[1 : 3]
d = a[-2 : ]
e = a[2 : 4]
print(b + c  + d + e)

c = 6
t = 2
print(f"제 방에는 의자 {c}개와 테이블 {t}개가 있습니다.")

a = ['e', 'b', 'd', 'a', 'c']
a.sort(reverse = True)
print(a)

a = []
a.extend([1, 2, 3, 4])
a.remove(1)
a.remove(2)
a.remove(3)
print(a)

id = "ilovepython"
pw = "mypass1234"
id1 = input("아이디를 입력하시오 :")
pw1 = input("패스워드를 입력하시오 :")

if id1 in id:
    if pw1 in pw:
        print("환영합니다")
else:
    print("아이디를 찾을수없습니다")

sum = 0
answer = "yes"
while answer == 'yes':
    number = int(input('숫자를 입력하세요'))
    sum = sum + number
    answer = input('계속?(yes/no) :')

print(f'합계는 {sum}')




    
