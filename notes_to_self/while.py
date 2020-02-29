people = [
            ['Bilbo', 'Baggins'],
            ['Gollum'],
            ['Tom', 'Bombadil'],
            ['Aragorn']
        ]

length = 0

#my solution
while length<len(people):
    to_print = ""
    if len(people[length]) > 1:
        to_print += people[length][0] + " " + people[length][1]
    else:
        to_print += people[length][0] + " "
    length += 1
    print(to_print)


#real solution
i = 0
while i < len(people):
    person = people[i]
    to_print = ""
    j = 0
    while j < len(person):
        name = person[j]
        to_print += name + " "
        j += 1
    print(to_print)
    i += 1
