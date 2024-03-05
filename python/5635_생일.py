# 어떤 반에 있는 학생들의 생일이 주어졌을 때, 가장 나이가 적은 사람과 가장 많은 사람을 구하는 프로그램을 작성하시오.

# 첫째 줄에 반에 있는 학생의 수 n이 주어진다. (1 ≤ n ≤ 100)
# 다음 n개 줄에는 각 학생의 이름과 생일이 "이름 dd mm yyyy"와 같은 형식으로 주어진다. 
# 이름은 그 학생의 이름이며, 최대 15글자로 이루어져 있다. 
# dd mm yyyy는 생일 일, 월, 연도이다. (1990 ≤ yyyy ≤ 2010, 1 ≤ mm ≤ 12, 1 ≤ dd ≤ 31) 주어지는 생일은 올바른 날짜이며, 연, 월 일은 0으로 시작하지 않는다.
# 이름이 같거나, 생일이 같은 사람은 없다.

# import datetime

# students = []
# birth = []

# n = int(input())


# for i in range(n) :
#     name, day, month, year = input().split()
#     cal_date = str(datetime.datetime(int(year), int(month), int(day)))
#     students.append([name, cal_date])
#     birth.append(cal_date)

# max_birth = max(birth)
# min_birth = min(birth)

# for i in range(len(students)) :
#   if students[i][1] == max_birth :
#     print(students[i][0])

# for i in range(len(students)) :
#   if students[i][1] == min_birth :
#     print(students[i][0])


students = []

n = int(input())

for _ in range(n) :
  n, d, m, y = input().split()
  d, m, y = map(int, (d, m, y))
  students.append((y, m, d, n))

students.sort()

print(students[-1][3])
print(students[0][3])