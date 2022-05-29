def horzintal_stars(num_of_stars):
    counter = 1
    while counter <= num_of_stars:
        print("*", end="")
        counter += 1


def num_of_line(lines):
    counter = 1
    hulf_side = lines // 2

    while counter <= hulf_side:
        horzintal_stars(counter)
        counter += 1
        print("\n")
    horzintal_stars(counter)
    print("\n")
    while counter >= 1:
        counter -= 1
        horzintal_stars(counter)
        print("\n")


max_stars = int(input("Enter the number of stars in the tip :"))
num_of_line(2 * max_stars - 1)
