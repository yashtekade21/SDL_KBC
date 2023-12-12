import random
questions = [
    ["The International Literacy Day is observed on ",
        "Sep 8", "Nov 28", "May 2", "Sep 22", 1],

    ["The language of Lakshadweep. a Union Territory of India, is ",
     "Hindi", "Marathi", "Malayalam", "Telugu", 3],

    ["Which day is observed as the World Standards Day? ",
     "Jun 8", "Aug 2", "Oct 14", "Nov 15", 3],

    ["Bahubali festival is related to ", "Hinduism",
     "Islam", "Buddhism", "Jainism", 4],

    ["Who is the author of the epic 'Meghdoot? ",
     "Vishakadatta", "Valmiki", "Banabhatta", "Kalidas", 4],

    ["Van Mahotsav was started by ", "Maharshi Karve",
     "Bal Gangadhar Tilak", "K.M. Munshi", "Sanjay Gandhi", 3],

    ["The Krithi system was perfected and Carnatic music was given by ",
     "Arunagirinathan", "Purandaradasa", "Shyama Shastri", "Swati Tirunal", 4],

    ["Writers Building is the headquarters of ", "The time of India Group",
     "All India Writers Association", "West Bengal Government", "Press trust of India", 4],

    ["The Konark Temple is dedicated to ",
     "Vishnu", "Shiva", "Krishna", "Sun-God", 4],

    ["The 227 year old 'Nawab Saheb Ki Haveli' is Iocated at ",
     "Hyderabad", "Jaipur", "New Delhi", "Agra", 2],

    ["Which of the following Academy is responsible for fostering the development of dance, drama and music in India? ",
     "Lalit Kala Academy", "Sahitya Academy", "National School of Drama", "Sangeet Academy", 4],

    ["In which of the following countries has India not organised 'India Festival' ? ",
     "Russia", "Japan", "France", "West Germany", 4],

    ["The Indian National Calendar is based on ",
     "Christian era", "Saka era", "Vikram era", "Hiji era", 2],

    ["The abbreviation 'fob' stands for ", "Free on Board",
     "Free of Bargain", "Fellow of Britain", "None of these", 1],

    ["Which British Army unit was given the motto 'Primus in Indis' because it was the first to serve in India? ",
     "41st (Welsh) Regiment of Foot", "1st Coldstream Guards", "5th Light Infantry", "39th Regiment of Foot", 4],
]

flip = ["Which party was founded by Sampat Pal Devi to stop violence against women in Bundelkhand?",
        " Laxmibai Sena", "Gulabi Gang", "Nari Mukti Vahini", "Mahila Morcha", 2]

price = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000,
         160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]


def fifty_fifty(i):
    correct = questions[i][5]
    options = [1, 2, 3, 4]
    options.remove(correct)
    wrong1 = random.choice(options)
    options.remove(wrong1)
    wrong2 = random.choice(options)

    print(f"50-50 LifeLine : Options {wrong1} and {wrong2} are removed\n")


def flip_question(i):
    print(flip[0])

    print(f"1.{flip[1]}                    2.{flip[2]}")
    print(f"3.{flip[3]}                    4.{flip[4]}\n")


def ask_audience(i):
    correct = questions[i][5]
    print(
        f"Ask the Audience LifeLine: Audience suggests the answer is option {correct}\n")


def two_attempts(i):
    correct = questions[i][5]
    attempts = 0

    print("Two Attempts LifeLine : You have two attempts to answer\n")
    while attempts <= 1:
        attempts += 1
        option = int(input(
            f"Attempt {attempts}\nEnter your Answer's Option Number [1 or 2 or 3 or 4] : "))

        if option == correct:
            print("Correct Answer\n")
            return option
        else:
            print("Wrong Answer\n")

    print("Your both attempts were wrong\n")
    return 0


i = 0
fifty_flag = 1
skip_flag = 1
two_att_flag = 1
ask_flag = 1
flag = 0
while i < 15:
    print("-----------------------------------------------------------------")
    print(f"Question for Rs. {price[i]}\n")

    print(questions[i][0])

    print(f"1.{questions[i][1]}                    2.{questions[i][2]}")
    print(f"3.{questions[i][3]}                    4.{questions[i][4]}\n")

    ans = int(input(
        "Enter your Answer's Option Number [1 or 2 or 3 or 4] \nEnter '-1' for LifeLine OR '0' to Quit : "))
    if ans == 0:
        if i > 4 and i < 10:
            print("You have quit the game with price amount of Rs. ", price[4])
        elif i > 9 and i < 15:
            print("You have quit the game with price amount of Rs. ", price[i])
        print("**** GAME OVER ****")
        break

    elif (ans == -1):
        if fifty_flag:
            print("1] 50-50 LifeLine")
        if skip_flag:
            print("2] Flip Question")
        if ask_flag:
            print("3] Ask Audience")
        if two_att_flag:
            print("4] Two Attempt")

        if (fifty_flag or skip_flag or ask_flag or two_att_flag):
            option = int(input("Enter option : "))
        else:
            print("All LifeLines Exhausted")
            flag = 1

        if flag:
            continue

        elif option == 1:
            fifty_flag = 0
            fifty_fifty(i)
            llans = int(input(
                "Enter your Answer's Option Number [1 or 2 or 3 or 4] \nEnter '0' to Quit : "))

            if (llans == 0):
                if i > 4 and i < 10:
                    print(
                        "You have quit the game with price amount of Rs. ", price[4])
                elif i > 9 and i < 15:
                    print(
                        "You have quit the game with price amount of Rs. ", price[i])
                print("**** GAME OVER ****")
                break
            if llans == questions[i][5]:
                print("\nCorrect Answer\n")
                print(f"Congrats!!, You have won Rs. {price[i]}\n")
                if (i == 4 or i == 9):
                    print(
                        "Congrats!!,You have Secured Amount of RS.", price[i])

                elif (i == 14):
                    print("\nCorrect Answer\n")
                    print(
                        f"Hurray..!!, You have won the GAME with price amount of Rs. {price[i]}\n")
                    print("**** GAME OVER ****")
                    break

            elif llans != questions[i][5]:
                if (i >= 0 and i < 4):
                    print("Sorry You haven't won any prize money...:(")
                    print(" **** GAME OVER **** ")
                    break

                elif (i >= 4 and i < 9):
                    print("Opps!!, Wrong Answer")
                    print("You have won price amount of RS. ", price[4])
                    print(" **** GAME OVER **** ")
                    break

                elif (i >= 9):
                    print("Opps!!, Wrong Answer")
                    print("You have won price amount of RS. ", price[8])
                    print(" **** GAME OVER **** ")
                    break

        elif option == 2:
            skip_flag = 0
            flip_question(i)
            llans = int(input(
                "Enter your Answer's Option Number [1 or 2 or 3 or 4] \nEnter '0' to Quit : "))

            if (llans == 0):
                if i > 4 and i < 10:
                    print(
                        "You have quit the game with price amount of Rs. ", price[4])
                elif i > 9 and i < 15:
                    print(
                        "You have quit the game with price amount of Rs. ", price[i])
                print("**** GAME OVER ****")
                break
            if llans == flip[5]:
                print("\nCorrect Answer\n")
                print(f"Congrats!!, You have won Rs. {price[i]}\n")
                if (i == 4 or i == 9):
                    print(
                        "Congrats!!,You have Secured Amount of RS.", price[i])

                elif (i == 14):
                    print("\nCorrect Answer\n")
                    print(
                        f"Hurray..!!, You have won the GAME with price amount of Rs. {price[i]}\n")
                    print("**** GAME OVER ****")
                    break
            elif llans != flip[5]:
                if (i >= 0 and i < 4):
                    print("Sorry You haven't won any prize money...:(")
                    print(" **** GAME OVER **** ")
                    break

                elif (i >= 4 and i < 9):
                    print("Opps!!, Wrong Answer")
                    print("You have won price amount of RS. ", price[4])
                    print(" **** GAME OVER **** ")
                    break

                elif (i >= 9):
                    print("Opps!!, Wrong Answer")
                    print("You have won price amount of RS. ", price[8])
                    print(" **** GAME OVER **** ")
                    break

        elif option == 3:
            ask_flag = 0
            ask_audience(i)
            llans = int(input(
                "Enter your Answer's Option Number [1 or 2 or 3 or 4] \nEnter '0' to Quit : "))

            if (llans == 0):
                if i > 4 and i < 10:
                    print(
                        "You have quit the game with price amount of Rs. ", price[4])
                elif i > 9 and i < 15:
                    print(
                        "You have quit the game with price amount of Rs. ", price[i])
                print("**** GAME OVER ****")
                break
            if llans == questions[i][5]:
                print("\nCorrect Answer\n")
                print(f"Congrats!!, You have won Rs. {price[i]}\n")
                if (i == 4 or i == 9):
                    print(
                        "Congrats!!,You have Secured Amount of RS.", price[i])

                elif (i == 14):
                    print("\nCorrect Answer\n")
                    print(
                        f"Hurray..!!, You have won the GAME with price amount of Rs. {price[i]}\n")
                    print("**** GAME OVER ****")
                    break
            elif llans != questions[i][5]:
                if (i >= 0 and i < 4):
                    print("Sorry You haven't won any prize money...:(")
                    print(" **** GAME OVER **** ")
                    break

                elif (i >= 4 and i < 9):
                    print("Opps!!, Wrong Answer")
                    print("You have won price amount of RS. ", price[4])
                    print(" **** GAME OVER **** ")
                    break

                elif (i >= 9):
                    print("Opps!!, Wrong Answer")
                    print("You have won price amount of RS. ", price[8])
                    print(" **** GAME OVER **** ")
                    break

        elif option == 4:
            two_att_flag = 0
            llans = two_attempts(i)

            if (llans == 0):
                if i > 4 and i < 10:
                    print(
                        "You have quit the game with price amount of Rs. ", price[4])
                elif i > 9 and i < 15:
                    print(
                        "You have quit the game with price amount of Rs. ", price[i])
                print("**** GAME OVER ****")
                break
            if llans == questions[i][5]:
                print("\nCorrect Answer\n")
                print(f"Congrats!!, You have won Rs. {price[i]}\n")
                if (i == 4 or i == 9):
                    print(
                        "Congrats!!,You have Secured Amount of RS.", price[i])

                elif (i == 14):
                    print("\nCorrect Answer\n")
                    print(
                        f"Hurray..!!, You have won the GAME with price amount of Rs. {price[i]}\n")
                    print("**** GAME OVER ****")
                    break
            elif llans != questions[i][5]:
                if (i >= 0 and i < 4):
                    print("Sorry You haven't won any prize money...:(")
                    print(" **** GAME OVER **** ")
                    break

                elif (i >= 4 and i < 9):
                    print("Opps!!, Wrong Answer")
                    print("You have won price amount of RS. ", price[4])
                    print(" **** GAME OVER **** ")
                    break

                elif (i >= 9):
                    print("Opps!!, Wrong Answer")
                    print("You have won price amount of RS. ", price[8])
                    print(" **** GAME OVER **** ")
                    break

    elif (ans == questions[i][5]):
        print("\nCorrect Answer\n")
        print(f"Congrats!!, You have won Rs. {price[i]}\n")
        if (i == 4 or i == 9):
            print("Congrats!!,You have Secured Amount of RS.", price[i])

        elif (i == 14):
            print("\nCorrect Answer\n")
            print(
                f"Hurray..!!, You have won the GAME with price amount of Rs. {price[i]}\n")
            print("**** GAME OVER ****")
            break

    elif (ans != questions[i][5]):
        if (i >= 0 and i < 4):
            print("Sorry You haven't won any prize money...:(")
            print(" **** GAME OVER **** ")
            break

        elif (i >= 4 and i < 9):
            print("Opps!!, Wrong Answer")
            print("You have won price amount of RS. ", price[4])
            print(" **** GAME OVER **** ")
            break

        elif (i >= 9):
            print("Opps!!, Wrong Answer")
            print("You have won price amount of RS. ", price[8])
            print(" **** GAME OVER **** ")
            break
    i += 1
