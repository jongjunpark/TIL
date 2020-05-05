a = input()
b = (''.join(reversed(a)))
print(b)
if a == b:
    print("입력하신 단어는 회문(Palindrome)입니다.")