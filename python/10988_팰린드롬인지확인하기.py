word = list(input())

print(int(word == word[::-1]))  # 리스트 순서를 뒤집어 비교

# length = len(word)
# result = 0

# for i in range(length) :
#   if word[i] == word[-i-1] :
#     result += 1
#   else :
#     break

# if result > length/2 :
#   print(1)
# else :
#   print(0)