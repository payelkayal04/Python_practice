Input = [2, 3, 3, 4, 5, 6, 6, 7, 8, 8]
Output = [2, 3, 4, 5, 6, 7, 8]


def remove_duplicate(input_list):
    list_1 = []
    for i in range(len(input_list)):
        if input_list[i] not in list_1:
            list_1.append(input_list[i])
    print(list_1)
    #[List1.append(i) for i in Input if Input[i] not in List1]

remove_duplicate(Input)