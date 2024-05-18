
# 5个人捕鱼后分鱼，第一个人将鱼分成5分，把多余的一条鱼放掉，拿走自己的一份；第二个人也将鱼分成5份，把多余的一条鱼放掉，拿走自己的一份；其他3个人也按照同样的方法那鱼，问他们至少捕到多少条鱼？

def devide_fish(people_count):
    fish = people_count + 1
    while True:
        is_enough = True
        total = fish
        for i in range(people_count):
            if (total-1) % people_count == 0:
                total = (total-1)/people_count * (people_count - 1)
                # 当前总数是，扔掉一条后平均分成5份，又被拿走一份
            else:
                is_enough = False
                fish += people_count * 1
                # 当前不够分，每人再多一条
                break

        if is_enough:
            return fish

if __name__ == '__main__':
    count = int(input("how many people to devide fish?"))
    print(devide_fish(count))
