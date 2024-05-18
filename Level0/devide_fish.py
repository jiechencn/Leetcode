def devide_fish(people_count):
    fish = people_count + 1
    while True:
        is_enough = True
        total = fish
        for i in range(people_count):
            if (total-1) % people_count == 0:
                total = (total-1)/people_count * (people_count - 1)
            else:
                is_enough = False
                fish += people_count * 1
                break

        if is_enough:
            return fish

if __name__ == '__main__':
    count = int(input("how many people to devide fish?"))
    print(devide_fish(count))