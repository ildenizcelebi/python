all_seats={}
rowcolumn= {}
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]

def CREATECATEGORY():
    row_column = liste[i][1][1].split("x")
    row = int(row_column[0])
    column = int(row_column[1])
    seats = row*column
    if liste[i][1][0] not in rowcolumn:
        rowcolumn[liste[i][1][0]] = liste[i][1][1]
        all_seats[liste[i][1][0]] = dict()
        for s in range(row):
            for j in range(column):
                seat_name = alphabet[s] + str(j)
                all_seats[liste[i][1][0]][seat_name] = "X"
        print(f"The category ’{liste[i][1][0]}’ having {seats} seats has been created")
        return f"The category ’{liste[i][1][0]}’ having {seats} seats has been created\n"
    else:
        print(f"Warning: Cannot create the category for the second time. The stadium has already {liste[i][1][0]}")
        return f"Warning: Cannot create the category for the second time. The stadium has already {liste[i][1][0]}\n"

def SELLTICKET():
    sell_str = ""
    if liste[i][1][2] not in rowcolumn:
        print(f"Category {liste[i][1][2]} cannot be sold due to absence.")
        sell_str += f"Category {liste[i][1][2]} cannot be sold due to absence.\n"
    else:
        index = int(rowcolumn[liste[i][1][2]].find("x"))
        for j in range(len(liste[i][1][3:])):
            if len(liste[i][1][3:][j]) < 4:
                if int(liste[i][1][3:][j][1:]) <= int(rowcolumn[liste[i][1][2]][index+1:]):
                    if liste[i][1][3:][j][0] in alphabet[0:int(rowcolumn[liste[i][1][2]][0:index])+1]:
                        if all_seats[liste[i][1][2]][liste[i][1][3:][j]] == "X":
                            if liste[i][1][1][0:3] == "stu":
                                all_seats[liste[i][1][2]][liste[i][1][3:][j]] = "S"
                            elif liste[i][1][1][0:3] == "ful":
                                all_seats[liste[i][1][2]][liste[i][1][3:][j]] = "F"
                            else:
                                all_seats[liste[i][1][2]][liste[i][1][3:][j]] = "T"
                            print(f"Success: {liste[i][1][0]} has bought {liste[i][1][3:][j]} at {liste[i][1][2]}")
                            sell_str += f"Success: {liste[i][1][0]} has bought {liste[i][1][3:][j]} at {liste[i][1][2]}\n"
                        else:
                            print(f"Warning: The seat {liste[i][1][3:][j]} cannot be sold to {liste[i][1][0]} since it was already sold!")
                            return f"Warning: The seat {liste[i][1][3:][j]} cannot be sold to {liste[i][1][0]} since it was already sold!"
                    else:
                        print(f"Error: The category '{liste[i][1][2]}' has less row than the specified index {liste[i][1][3:][j]}!")
                        sell_str += f"Error: The category '{liste[i][1][2]}' has less row than the specified index {liste[i][1][3:][j]}!\n)"
                else:
                    if liste[i][1][3:][j][0] in alphabet[0:int(rowcolumn[liste[i][1][2]][0:index])]:
                        print(f"Error: The category '{liste[i][1][2]}' has less column than the specified index {liste[i][1][3:][j]}!")
                        sell_str += f"Error: The category '{liste[i][1][2]}' has less column than the specified index {liste[i][1][3:][j]}!\n"
                    else:
                        print(f"Error: The category '{liste[i][1][2]}' has less column and row than the specified index {liste[i][1][3:][j]}!")
                        sell_str += f"Error: The category '{liste[i][1][2]}' has less column and row than the specified index {liste[i][1][3:][j]}!\n"
            else:
                seat_range = int(liste[i][1][3:][j].find("-"))
                is_true = True
                if int(liste[i][1][3:][j][seat_range+1:]) > int(rowcolumn[liste[i][1][2]][index+1:]):
                    if liste[i][1][3:][j][0] in alphabet[0:int(rowcolumn[liste[i][1][2]][0:index])]:
                        print(f"Error: The category '{liste[i][1][2]}' has less column than the specified index {liste[i][1][3:][j]}!")
                        sell_str += f"Error: The category '{liste[i][1][2]}' has less column than the specified index {liste[i][1][3:][j]}!\n"
                    else:
                        print(f"Error: The category '{liste[i][1][0]}' has less column and row than the specified index {liste[i][1][3:][j]}!")
                        sell_str += f"Error: The category '{liste[i][1][0]}' has less column and row than the specified index {liste[i][1][3:][j]}!\n"
                elif int(liste[i][1][3:][j][seat_range+1:]) <= int(rowcolumn[liste[i][1][2]][index+1:]):
                    if liste[i][1][3:][j][0] not in alphabet[0:int(rowcolumn[liste[i][1][2]][0:index])+1]:
                        print(f"Error: The category '{liste[i][1][2]}' has less row than the specified index {liste[i][1][3:][j]}!")
                        sell_str += f"Error: The category '{liste[i][1][2]}' has less row than the specified index {liste[i][1][3:][j]}!\n)"
                    for k in range(int(liste[i][1][3:][j][1:seat_range]),int(liste[i][1][3:][j][seat_range + 1:]) + 1):
                        sıra = str(liste[i][1][3:][j][0]) + str(k)
                        if all_seats[liste[i][1][2]][sıra] != "X":
                            is_true = False
                        if is_true:
                            if liste[i][1][1][0:3] == "stu":
                                all_seats[liste[i][1][2]][sıra] = "S"
                            elif liste[i][1][1][0:3] == "ful":
                                all_seats[liste[i][1][2]][sıra] = "F"
                            else:
                                all_seats[liste[i][1][2]][sıra] = "T"
                    if is_true:
                        print(f"Success: {liste[i][1][0]} has bought {liste[i][1][3:][j]} at {liste[i][1][2]}")
                        sell_str += f"Success: {liste[i][1][0]} has bought {liste[i][1][3:][j]} at {liste[i][1][2]}\n"
                    else:
                        print(f"Warning: The seats {liste[i][1][3:][j]} cannot be sold to {liste[i][1][0]} due some of them have already been sold")
                        sell_str += f"Warning: The seats {liste[i][1][3:][j]} cannot be sold to {liste[i][1][0]} due some of them have already been sold\n"
        return sell_str

def CANCELTICKET():
    sell_str = ""
    if liste[i][1][0] not in rowcolumn:
        print(f"Category {liste[i][1][0]} cannot be canceled due to absence.")
        sell_str += f"Category {liste[i][1][0]} cannot be canceled due to absence.\n"
    else:
        index = int(rowcolumn[liste[i][1][0]].find("x"))
        for j in range(len(liste[i][1][1:])):
            if int(liste[i][1][1:][j][1:]) <= int(rowcolumn[liste[i][1][0]][index+1:]):
                if liste[i][1][1:][j][0] in alphabet[0:int(rowcolumn[liste[i][1][0]][0:index])]: #+1 ekleyecek miyim????
                    if all_seats[liste[i][1][0]][liste[i][1][1:][j]] != "X":
                        all_seats[liste[i][1][0]][liste[i][1][1:][j]] = "X"
                        print(f"Success: The seat {liste[i][1][1:][j]} at {liste[i][1][0]} has been canceled and now ready to sell again")
                        return f"Success: The seat {liste[i][1][1:][j]} at {liste[i][1][0]} has been canceled and now ready to sell again\n"
                    else:
                        print(f"Error: The seat {liste[i][1][1:][j]} at {liste[i][1][0]} has already been free! Nothing to cancel")
                        return f"Error: The seat {liste[i][1][1:][j]} at {liste[i][1][0]} has already been free! Nothing to cancel\n"
                else:
                    print(f"Error: The category '{liste[i][1][0]}' has less row than the specified index {liste[i][1][1:][j]}!")
                    sell_str += f"Error: The category '{liste[i][1][0]}' has less row than the specified index {liste[i][1][1:][j]}!\n)"
            else:
                if liste[i][1][1:][j][0] in alphabet[0:int(rowcolumn[liste[i][1][0]][0:index])]:
                    print(f"Error: The category '{liste[i][1][0]}' has less column than the specified index {liste[i][1][1:][j]}!")
                    sell_str += f"Error: The category '{liste[i][1][0]}' has less column than the specified index {liste[i][1][1:][j]}!\n"
                else:
                    print(f"Error: The category '{liste[i][1][0]}' has less column and row than the specified index {liste[i][1][1:][j]}!")
                    sell_str += f"Error: The category '{liste[i][1][0]}' has less column and row than the specified index {liste[i][1][1:][j]}!\n"
        return sell_str

def BALANCE():
    total = ""
    for x in all_seats[liste[i][1][0]]:
        total += all_seats[liste[i][1][0]][x]
    total = list(total)
    sum_of_students = total.count("S")
    sum_of_full_pay = total.count("F")
    sum_of_season_ticket = total.count("T")
    Revenues = sum_of_students*10 + sum_of_full_pay*20 + sum_of_season_ticket*250
    firstline = f"category report of '{liste[i][1][0]}'\n"
    secondline = "-------------------------------\n"
    thirdline = f"Sum of students = {sum_of_students}, Sum of full pay = {sum_of_full_pay}, Sum of season tickets = {sum_of_season_ticket}, and Revenues = {Revenues} Dollars\n"
    output = firstline+secondline+thirdline
    thirdline2 = f"Sum of students = {sum_of_students}, Sum of full pay = {sum_of_full_pay}, Sum of season tickets = {sum_of_season_ticket}, and Revenues = {Revenues} Dollars"
    output2 = firstline + secondline + thirdline2
    print(output2)
    return output

def SHOWCATEGORY():
    row_column = rowcolumn[liste[i][1][0]].split("x")
    row = int(row_column[0])
    column = int(row_column[1])
    string=""
    output_show=""
    son = ""
    print(f"Printing category layout of {liste[i][1][0]}\n")
    output_show=f"Printing category layout of {liste[i][1][0]}\n\n"
    reversed_alphabet=alphabet[0:row]
    reversed_alphabet.reverse()
    sayılar=""
    for sayı in range(column):
        if len(str(sayı))==2:
            sayılar+=" "+str(sayı)
        else:
            sayılar+="  "+str(sayı)
    for harf in reversed_alphabet:
        string=""
        for seats in all_seats[liste[i][1][0]]:
            if seats[0]==harf:
                son=""
                string+=all_seats[liste[i][1][0]][seats]+"  "
                son=harf+" "+string
        print(son)
        output_show+=son+"\n"
    output_show+=sayılar+"\n"
    print(sayılar)
    return output_show

def input_file():
    global liste
    liste = f.readlines()
    for j in range(len(liste)):
        liste[j] = liste[j].split(" ",1)
        liste[j][1] = liste[j][1].replace("\n","")
        liste[j][1] = liste[j][1].split(" ")

def output_file():
    global i
    for i in range(len(liste)):
        if liste[i][0] == "CREATECATEGORY" :
            file.write(CREATECATEGORY())

        elif liste[i][0] == "SELLTICKET" :
            file.write(SELLTICKET())

        elif liste [i][0]== "CANCELTICKET" :
            file.write(CANCELTICKET())

        elif liste[i][0]== "SHOWCATEGORY" :
            file.write(SHOWCATEGORY())

        elif liste[i][0]== "BALANCE" :
            file.write(BALANCE())
        else:
            pass

import sys
file_name=sys.argv[1]
with open("output.txt", "w", encoding = "utf-8") as file:
    with open(file_name, "r", encoding = "utf-8") as f:
        input_file()
        output_file()