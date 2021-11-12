def bubble_sort(my_list: list):
    for numpass in range(len(my_list)-1, 0, -1):
        for i in range(numpass):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    return my_list


if __name__ == "__main__":
    print(bubble_sort([55, 44, 10, 5, 6, -2, -44]))
