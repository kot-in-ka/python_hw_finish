# Задача 1. Постройте график функции 𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно.
def task1():
    x = []
    y = []

    for i in range(-10, 10):
        x.append(i)
    for i in range(len(x)):
        y.append(5 * x[i] * x[i] + 10 * x[i] - 30)

    print(f'Значение функции отрицательно на участке между точками пересечения графика функции с осью X')

    plt.title("График функции f(x)=5x^2+10x-30")
    plt.axhline(0, color='g')
    plt.axvline(0, color='g')
    plt.grid()
    plt.plot(x, y)
    plt.show()

# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.
def task2():
    HouseАrea = list(randint(100, 300) for i in range(15))
    HousePrice = list(randint(3, 20) for i in range(15))
    OneMeterPrice = list(map(lambda x, y: round((x/y)*1000, 2), HousePrice, HouseАrea))
    RightHouses = list(i for i in range(15))
    line = [50]*15

    print(f'Площадь домов (м. кв.): {HouseАrea}')
    print(f'Стоимость домов (млн. руб.): {HousePrice}')
    print(f'Их цена за 1 квадратный метр (тыс. руб) {OneMeterPrice}')

    HousesList = []
    for i in range(15):
        if OneMeterPrice[i] < 50:
            HousesList.append(HouseАrea[i]) 
    HousesList.sort()
    print(f'Риелтору подойдут дома со следующей площадью (м. кв.) : {HousesList}')

    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel("Номера домов", fontsize=12, color='orange', labelpad=5)    # +
    ax.set_ylabel("Цена (т.р.)", fontsize=12, color='orange', labelpad=0, rotation=0)  # +
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.bar(RightHouses, OneMeterPrice)
    plt.plot(line, "g-")
    plt.show()


task2()
