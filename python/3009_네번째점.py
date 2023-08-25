# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

x = []
y = []

def calc(list, num) :
    if num not in list :
        list.append(num)
    else :
        list.remove(num)

for i in range(3) :
    a, b = map(int, input().split())
    calc(x, a)
    calc(y, b)

print(x[0], y[0])




# pointsX = list()
# pointsY = list()

# for _ in range(3):
#     x, y = map(int, input().split())
#     pointsX.append(x)
#     pointsY.append(y)

# def calcMin(a, b, c) :
#     c_list = list([a, b, c])
#     return c_list.index(min(c_list))

# resultX = calcMin(pointsX.count(pointsX[0]), pointsX.count(pointsX[1]), pointsX.count(pointsX[2]))    
# resultY = calcMin(pointsY.count(pointsY[0]), pointsY.count(pointsY[1]), pointsY.count(pointsY[2]))    

# print(pointsX[resultX], pointsY[resultY])
