# 알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아
# 순서대로 붙여 출력하는 프로그램을 작성해보자.

a, b = input().split()
word = a + b
print(word)

# 2개의 단어니까 각각 a와b를 split으로 입력 받아 나눠준다.
# 문자열끼리 +하여 출력하여 준다.