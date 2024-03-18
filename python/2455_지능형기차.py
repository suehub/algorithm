sum = 0
result = []

for _ in range(4) :
  in_people, out_people = (map(int, input().split()))
  sum -= in_people
  result.append(sum)
  sum += out_people
  result.append(sum)

print(max(result))