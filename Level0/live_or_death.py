print("--------------------------")
def live(total_count, death_number, live_count):
    people = list(range(1, total_count + 1))


    current_pos = 0
    while (len(people) > live_count):
        current_pos = (current_pos + death_number -1) % len(people)
        print("{} is dead".format(people[current_pos]))
        del people[current_pos]

    return people


live_peope = live(30, 9, 15)
print("Live people: ", live_peope)