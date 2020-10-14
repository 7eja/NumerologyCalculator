import array as arr
import numpy as np
from operator import add
from tabulate import tabulate
import os.path

print("Enter your date of birth: \n")
day = input("Day: ")
month = input("Month: ")
year = input("Year: ")

print("Enter your name \n")
name = input()

save_path = "D:\\Documents_Sep2020\\Python_code_results\\NumerologyReports"
fname = name + ".txt"
cname = os.path.join(save_path, fname)
note = open(cname, "w+")

note.write("Date of birth:  " + day + " - " + month + " - " + year + '\n')
note.write("Name: " + name + '\n')
note.write('\n')


def single_digit(num):
    sum_of_digits = num
    while int(num) > 9:
        if num == 11 or num == 22:
            break
        sum_of_digits = 0
        for digit in str(num):
            sum_of_digits += int(digit)
        num = sum_of_digits
    return int(num)


def single_digit_complete(num):
    sum_of_digits = num
    while int(num) > 9:
        sum_of_digits = 0
        for digit in str(num):
            sum_of_digits += int(digit)
        num = sum_of_digits
    return int(num)


def life_path(day, month, year):
    dd = single_digit(day)
    dm = single_digit(month)
    dy = single_digit(year)
    LP = int(day) + int(month) + int(year)
    lp = dd + dm + dy
    lifepath = single_digit(LP)

    note.write("Your Life Path is: " + str(lp) + "/" + str(lifepath) + '\n')
    LP = lifepath
    pin1 = single_digit(dd + dm)
    pin2 = single_digit(dd + dy)
    pin3 = single_digit(pin1 + pin2)
    pin4 = single_digit(dm + dy)

    if LP == 11:
        sLP = 2
    elif LP == 22:
        sLP = 4
    else:
        sLP = LP
    p_start = 36 - sLP

    note.write("PINNACLES" + '\n')
    note.write('\n')
    note.write("1st Pinnacle: from   " + str(0) + "   to  " + str(int(p_start)) + "  is  " + str(pin1) + '\n')
    note.write(
        "2nd Pinnacle: from   " + str(int(p_start)) + "  to  " + str(int(p_start) + 9) + "  is  " + str(pin2) + '\n')
    note.write("3rd Pinnacle: from   " + str(int(p_start) + 9) + "  to  " + str(int(p_start) + 18) + "  is  " + str(
        pin3) + '\n')
    note.write("3rd Pinnacle: from   " + str(int(p_start) + 18) + "  to  " + str(int(p_start) + 27) + "  is  " + str(
        pin4) + '\n')

    chal1 = abs(int(single_digit_complete(dd) - single_digit_complete(dm)))
    chal2 = abs(int(single_digit_complete(dd) - single_digit_complete(dy)))
    mchal = abs(int(single_digit_complete(chal1) - single_digit_complete(int(chal2))))

    note.write('\n')
    note.write("CHALLENGES" + '\n')
    note.write("Challenge in the first half:  " + str(chal1) + '\n')
    note.write("Challenge in the second half  " + str(chal2) + '\n')
    note.write("Challenge overall   " + str(mchal) + '\n')

    return LP


lifepath = life_path(day, month, year)


def essence(pname, age, i):
    pname = pname.lower()
    escence_tab = np.full((age, 1), 0)
    for k in range(len(pname)):
        if pname[k] == "a" or pname[k] == "j" or pname[k] == "s":
            if i < len(escence_tab):
                escence_tab[i] = escence_tab[i] + 1
            i += 1
        elif pname[k] == "b" or pname[k] == "k" or pname[k] == "t":
            for ll in range(2):
                # print(ll)
                if i + ll < len(escence_tab):
                    escence_tab[i + ll] += 2
            i += 2
        elif pname[k] == "c" or pname[k] == "l" or pname[k] == "u":
            for ll in range(3):
                if i + ll < len(escence_tab):
                    escence_tab[i + ll] += 3
            i += 3
        elif pname[k] == "d" or pname[k] == "m" or pname[k] == "v":
            for ll in range(4):
                if i + ll < len(escence_tab):
                    escence_tab[i + ll] += 4
            i += 4
        elif pname[k] == "e" or pname[k] == "n" or pname[k] == "w":
            for ll in range(5):
                if i + ll < len(escence_tab):
                    escence_tab[i + ll] += 5
            i += 5
        elif pname[k] == "f" or pname[k] == "o" or pname[k] == "x":
            for ll in range(6):
                if i + ll < len(escence_tab):
                    escence_tab[i + ll] += 6
            i += 6
        elif pname[k] == "g" or pname[k] == "p" or pname[k] == "y":
            for ll in range(7):
                if i + ll < len(escence_tab):
                    escence_tab[i + ll] += 7
            i += 7
        elif pname[k] == "h" or pname[k] == "q" or pname[k] == "z":
            for ll in range(8):
                if i + ll < len(escence_tab):
                    escence_tab[i + ll] += 8
            i += 8
        elif pname[k] == "i" or pname[k] == "r":
            for ll in range(9):
                if i + ll < len(escence_tab):
                    escence_tab[i + ll] += 9
            i += 9

    return escence_tab, i


def name_number(name):
    global daymon
    L = len(name)
    name_num = 0
    soul_urge = 0
    low_name = name.lower()
    for i in range(0, L):
        if low_name[i] == "a" or low_name[i] == "j" or low_name[i] == "s":
            name_num = name_num + 1
            if low_name[i] == "a":
                soul_urge = soul_urge + 1
        elif low_name[i] == "b" or low_name[i] == "k" or low_name[i] == "t":
            name_num = name_num + 2
        elif low_name[i] == "c" or low_name[i] == "l" or low_name[i] == "u":
            name_num = name_num + 3
            if low_name[i] == "u":
                soul_urge = soul_urge + 3
        elif low_name[i] == "d" or low_name[i] == "m" or low_name[i] == "v":
            name_num = name_num + 4
        elif low_name[i] == "e" or low_name[i] == "n" or low_name[i] == "w":
            name_num = name_num + 5
            if low_name[i] == "e":
                soul_urge = soul_urge + 5
        elif low_name[i] == "f" or low_name[i] == "o" or low_name[i] == "x":
            name_num = name_num + 6
            if low_name[i] == "o":
                soul_urge = soul_urge + 6
        elif low_name[i] == "g" or low_name[i] == "p" or low_name[i] == "y":
            name_num = name_num + 7
        elif low_name[i] == "h" or low_name[i] == "q" or low_name[i] == "z":
            name_num = name_num + 8
        elif low_name[i] == "i" or low_name[i] == "r":
            name_num = name_num + 9
            if low_name[i] == "i":
                soul_urge = soul_urge + 9

    return name_num, soul_urge


def essence_cal(name):
    name = name.lower()
    sp_name = name.split()
    spl = len(sp_name)
    age = 100
    essence_tab = np.full((age, 1), 0)
    # print("Calculating.", end=" ")
    ind = np.full((spl, 1), 0)
    temp = [np.full((spl, 1), 0)]
    for i in range(spl):
        temp, ind[i] = essence(sp_name[i], age, 0)
        essence_tab = np.add(essence_tab, temp)
        while ind[i] <= age:
            temp, ind[i] = essence(sp_name[i], age, int(ind[i]))
            essence_tab = np.add(essence_tab, temp)
    Py = single_digit(int(day) + int(month))
    sum_of_digits = 0
    daymon = Py
    space = ' '

    note.write('\n')
    note.write("ESSENCE" + '\n')
    note.write(3 * space + "Year" + 4 * space + "Essence Year" + 4 * space + "Personal year" + '\n')
    for i in range(len(essence_tab)):
        personal_year = int(daymon) + int(year) + i

        fstop = "."
        note.write(
            3 * space + "%d" % (int(i + int(year))) + 10 * space + "%d" % single_digit(int(
                essence_tab[i])) + 10 * space + "%d" % single_digit(
                int(personal_year)) + '\n')
        note.write(30 * fstop + '\n')

    return essence_tab


def missing_numbers(name):
    name = name.lower()
    missing = np.full((9, 1), 1)
    number_of_times = np.full((9, 1), 0)
    L = len(name)
    for i in range(0, L):
        if name[i] == "a" or name[i] == "j" or name[i] == "s":
            missing[0] = 0
            number_of_times[0] = number_of_times[0] + 1
        elif name[i] == "b" or name[i] == "k" or name[i] == "t":
            missing[1] = 0
            number_of_times[1] = number_of_times[1] + 1
        elif name[i] == "c" or name[i] == "l" or name[i] == "u":
            missing[2] = 0
            number_of_times[2] = number_of_times[2] + 1
        elif name[i] == "d" or name[i] == "m" or name[i] == "v":
            missing[3] = 0
            number_of_times[3] = number_of_times[3] + 1
        elif name[i] == "e" or name[i] == "n" or name[i] == "w":
            missing[4] = 0
            number_of_times[4] = number_of_times[4] + 1
        elif name[i] == "f" or name[i] == "o" or name[i] == "x":
            missing[5] = 0
            number_of_times[5] = number_of_times[5] + 1
        elif name[i] == "g" or name[i] == "p" or name[i] == "y":
            missing[6] = 0
            number_of_times[6] = number_of_times[6] + 1
        elif name[i] == "h" or name[i] == "q" or name[i] == "z":
            missing[7] = 0
            number_of_times[7] = number_of_times[7] + 1
        elif name[i] == "i" or name[i] == "r":
            missing[8] = 0
            number_of_times[8] = number_of_times[8] + 1

    return missing, number_of_times


def name_details(name, missing, number_of_times):
    name = name.lower()
    sp_name = name.split()
    spl = len(sp_name)
    growth_number, so_ur = name_number(sp_name[0])
    note.write('\n')
    note.write('The growth number is  ' + str(growth_number))
    note.write('\n')
    note.write('INTENSITY TABLE:   ')
    note.write('\n')
    for i in range(0, 9):
        note.write('The number of times ' + str(i + 1) + '  appeared is- ' + str(nam2num(number_of_times[i])) + '  ')
        note.write('\n')

    note.write('\n')
    note.write('KARMIC LESSONS:   ')
    note.write('\n')
    for i in range(0, 9):
        if missing[i] == 1:
            note.write(str(i + 1) + '  ')

    intensity_points = np.full((9, 1), 0)
    if number_of_times[0] > 3:
        intensity_points[0] = 10
    if number_of_times[1] > 1:
        intensity_points[1] = 10
    if number_of_times[2] > 2:
        intensity_points[2] = 10
    if number_of_times[3] > 1:
        intensity_points[3] = 10
    if number_of_times[4] > 5:
        intensity_points[4] = 10
    if number_of_times[5] > 2:
        intensity_points[5] = 10
    if number_of_times[6] > 1:
        intensity_points[6] = 10
    if number_of_times[7] > 1:
        intensity_points[7] = 10
    if number_of_times[8] > 3:
        intensity_points[8] = 10

    note.write('\n')
    note.write('INTENSITY POINTS (0 means none)   ')
    for i in range(0, 9):
        if intensity_points[i] == 10:
            note.write(str(nam2num(i + 1)) + '   ')
    note.write('\n')
    note.write('PRIME INTENSIFIER   ')
    maxpos = int(np.argmax(number_of_times))
    note.write(str(maxpos + 1))
    note.write('\n')


def nam2num(digit):
    numname = ''
    if digit == 1:
        numname = 'one'
    elif digit == 2:
        numname = 'two'
    elif digit == 2:
        numname = 'two'
    elif digit == 3:
        numname = 'three'
    elif digit == 4:
        numname = 'four'
    elif digit == 5:
        numname = 'five'
    elif digit == 6:
        numname = 'six'
    elif digit == 7:
        numname = 'seven'
    elif digit == 8:
        numname = 'eight'
    elif digit == 9:
        numname = 'nine'

    return numname


def karmic_debts(name, day, month, year):
    name_no, soul_ur = name_number(name)
    dd = single_digit(day)
    dm = single_digit(month)
    dy = single_digit(year)
    LP = int(dd) + int(dm) + int(dy)
    kb_13 = 0
    kb_14 = 0
    kb_16 = 0
    kb_19 = 0
    if int(day) == 13 or int(name_no) == 13 or int(LP) == 13:
        kb_13 = 13
    if int(day) == 14 or int(name_no) == 14 or int(LP) == 14:
        kb_14 = 14
    if int(day) == 16 or int(name_no) == 16 or int(LP) == 16:
        kb_16 = 16
    if int(day) == 19 or int(name_no) == 19 or int(LP) == 19:
        kb_19 = 19

    return kb_13, kb_14, kb_16, kb_19


name_no, soul_ur = name_number(name)
note.write('\n')
note.write("Your expression number is:  " + str(name_no) + '\n')
note.write("Your soul urge number is:  " + str(soul_ur) + '\n')
miss, num_times = missing_numbers(name)
name_details(name, miss, num_times)
kb1, kb2, kb3, kb4 = karmic_debts(name, day, month, year)
note.write("Your karmic debt numbers are:  ")
if kb1 == 13:
    note.write(str(kb1) + '   ')
if kb2 == 14:
    note.write(str(kb2) + '   ')
if kb3 == 16:
    note.write(str(kb3) + '   ')
if kb4 == 19:
    note.write(str(kb4) + '   ')
note.write('\n')
essence_tab = essence_cal(name)
# from scipy.io import loadmat
# annots = loadmat('cars_train_annos.mat')
