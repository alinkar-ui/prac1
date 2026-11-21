temp = []

def avg(values):
    return sum(values) / len(values)

def calc_min_max(values):
    return [min(values), max(values)]

num = int(input('enter a number'))
for i in range(num):
    values = float(input('enter temp: '))
    temp.append(values)

sorted_temp = sorted(temp)

def calc_median(values):
    sorted_temp = sorted(values)
    n = len(sorted_temp)

    if n % 2 == 1:
        return sorted_temp[n // 2]
    else:
        middle1 = sorted_temp[n // 2 - 1]
        middle2 = sorted_temp[n // 2]

        return (middle1 + middle2) / 2
        


print("Average:", avg(temp))
print("Maximum:", calc_min_max(temp))
print("Median:", calc_median(temp))
print("Sorted:", sorted_temp)


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    user_input = input("Enter numbers: ")

    numbers = user_input.split(",")

    float_numbers = []

    for i in numbers:
        float_numbers.append(float(i))

    return float_numbers


display_main_menu()

values = get_user_input()

print("Your numbers:", values)

calc_average_temperature = avg
calc_min_max_temperature = calc_min_max


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

    print("Average = " + str(avg(num_list)))

    min_max = calc_min_max(num_list)
    print("Minimum = " + str(min_max[0]))
    print("Maximum = " + str(min_max[1]))

    print("Sorted = " + str(sorted_temp(num_list)))
    print("Median = " + str(calc_median(num_list)))


if __name__ == "__main__":
    main()

