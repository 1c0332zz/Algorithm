# a = '1 2 3'
# print(a.split())
# 문자열을 특정 단위로 쪼개줌!
# 리스트! 
# # ['1', '2', '3']
# input().split(':') 를 사용하면 콜론 ':' 기호를 기준으로 자른다.
# print(?, ?, sep=':') 를 사용하면 콜론 ':' 기호를 사이에 두고 값을 출력한다.


a, b = input().split(':') # 터미널에서도 1:2 처럼 :를 사용해주어야 출력된다.
print(a, b, sep=':') #sep 는 분류기호(seperator)를 의미한다.