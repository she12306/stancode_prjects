"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your program should be case-insensitive.
If the user input -1 for class name, your program would output
the maximum, minimum, and average among all the inputs.
"""


EXIT = '-1'


def main():
    """
    According to the input class, output the respective highest score, lowest score and average.
    """
    max_001 = -float("inf")
    max_101 = -float("inf")
    min_001 = float("inf")
    min_101 = float("inf")
    total_001 = 0
    total_101 = 0
    num_001 = 0
    num_101 = 0

    while True:
        cls = str(input(f"Which class? ")).lower()
        if cls == EXIT:
            break
        if cls == 'sc001':
            scr_001 = int(input(f"Score: "))
            if scr_001 > max_001:
                max_001 = scr_001
            if scr_001 < min_001:
                min_001 = scr_001
            total_001 += scr_001
            num_001 += 1
        if cls == 'sc101':
            scr_101 = int(input(f"Score: "))
            if scr_101 > max_101:
                max_101 = scr_101
            if scr_101 < min_101:
                min_101 = scr_101
            total_101 += scr_101
            num_101 += 1

    if num_001 == 0 and num_101 == 0:
        print('No class score were entered.')
    else:
        print(f'==========SCOO1==========')
        if num_001 != 0:
            print(f'Max (001): {max_001}')
            print(f'Min (001): {min_001}')
            print(f'Avg (001): {total_001/num_001}')
        else:
            print('No score for SCOO1')
        print(f'==========SC1O1==========')
        if num_101 != 0:
            print(f'Max (101): {max_101}')
            print(f'Min (101): {min_101}')
            print(f'Avg (101): {total_101/num_101}')
        else:
            print('No score for SC1O1')


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
