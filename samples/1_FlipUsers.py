

def flip_s2Pass (arr ):
    F_inter = []
    B_inter = []

    current_base = arr [0]
    start_index = 0
    for i in range(len(arr)) :
        if arr[i] == current_base:
            # increment i
            end_index = i

        else:
            if current_base == 'F':
                F_inter.append((start_index, end_index))
            else:
                B_inter.append((start_index, end_index))
            start_index = i
            current_base= arr[i]
    end_index = len(arr) - 1
    if arr[end_index] == 'F':
        F_inter.append((start_index, end_index))
    else:
        B_inter.append((start_index, end_index))

    print(len(F_inter))
    print(len(B_inter))
    print((F_inter))
    print((B_inter))
    if len(B_inter) >= len(F_inter):
        print ( "Flip F")
    else:
        print("Flip B")

def flip_s1Pass (arr ):
    F_inter = []
    B_inter = []

    current_base = arr [0]
    start_index = 0
    for i in range(len(arr)) :
        if arr[i] == current_base:
            # increment i
            end_index = i

        else:
            if current_base == 'F':
                F_inter.append((start_index, end_index))
            else:
                B_inter.append((start_index, end_index))
            start_index = i
            current_base= arr[i]
    end_index = len(arr) - 1
    if arr[end_index] == 'F':
        F_inter.append((start_index, end_index))
    else:
        B_inter.append((start_index, end_index))

    print(len(F_inter))
    print(len(B_inter))
    print((F_inter))
    print((B_inter))


if __name__ == '__main__':
    input = "BFFBFBBFFBFB"
    flip_s2Pass([char for char in input])
