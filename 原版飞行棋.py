import os
import random

Maps = [0 for i in range(100)]
PlayerPos = [0 for i in range(2)]
PlayerNames = ['', '']
Flags = [False, False]

def main():
    PlayerNames[0] = input("请输入玩家A的姓名：")
    PlayerNames[1] = input("请输入玩家B的姓名：")
    os.system('cls')
    print("{0}的士兵用A表示".format(PlayerNames[0]))
    print("{0}的士兵用B表示".format(PlayerNames[1]))
    InitailMap()
    DrawMap()
    while (PlayerPos[0] < 99 and PlayerPos[1] < 99):
        if (Flags[0] == False):
            PlayGame(0)
        else:
            Flags[0] = False
        if (PlayerPos[0] >= 99):
            print("玩家{0}无耻的赢了玩家{1}".format(PlayerNames[0], PlayerNames[1]))
            break
        if (Flags[1] == False):
            PlayGame(1)
        else:
            Flags[1] = False
        if (PlayerPos[1] >= 99):
            print("玩家{0}无耻的赢了玩家{1}".format(PlayerNames[1], PlayerNames[0]))
            break
    input("胜利！！！！！（按任意键以退出）")

def InitailMap():
    luckyturn = [6, 23, 40, 55, 69, 83]
    for i in range(len(luckyturn)):
        Maps[luckyturn[i]] = 1
    landMine = [5, 13, 17, 33, 38, 50, 64, 80, 94]
    for i in range(len(landMine)):
        Maps[landMine[i]] = 2
    pause = [9, 27, 60, 93, 2, 3, 4, 7, 8]
    for i in range(len(pause)):
        Maps[pause[i]] = 3
    timeTunnel = [20, 25, 45, 63, 72, 88, 90]
    for i in range(len(timeTunnel)):
        Maps[timeTunnel[i]] = 4

def DrawMap():
    print("图例:幸运轮盘:※   地雷:☆   暂停:Δ   时空隧道:♇")
    for i in range(30):
        print(DrawStringMap(i), end='')
    for i in range(30, 35):
        for j in range(28):
            print("  ", end='')
        print(DrawStringMap(i))
    for i in range(64, 34, -1):
        print(DrawStringMap(i), end='')
    for i in range(65, 70):
        print(DrawStringMap(i))
    for i in range(70, 100):
        print(DrawStringMap(i), end='')

def DrawStringMap(i):
    s = ""
    if (PlayerPos[0] == PlayerPos[1] and PlayerPos[0] == i):
        s = "<>"
    elif(PlayerPos[0] == i):
        s = "A"
    elif(PlayerPos[1] == i):
        s = "B"
    else:
        if(Maps[i] == 0):
            s = "★"
        if(Maps[i] == 1):
            s = "※"
        if(Maps[i] == 2):
            s = "☆"
        if(Maps[i] == 3):
            s = "Δ"
        if(Maps[i] == 4):
            s = "♇"
    return s

def PlayGame(playerNumber):
    rNumber = random.randint(1, 7)
    input("{0}按任意键开始掷骰子".format(PlayerNames[playerNumber]))
    print("{0}掷出了{1}".format(PlayerNames[playerNumber], rNumber))
    PlayerPos[playerNumber] += rNumber
    ChangePos()
    input("{0}按任意键开始行动".format(PlayerNames[playerNumber]))
    input("{0}行动完了".format(PlayerNames[playerNumber]))
    if (PlayerPos[playerNumber] == PlayerPos[1 - playerNumber]):
        input("玩家{0}踩到了玩家{1}，玩家{1}退6格".format(
            PlayerNames[playerNumber], PlayerNames[1 - playerNumber]))
        PlayerPos[1 - playerNumber] -= 6
    else:
        if (Maps[PlayerPos[playerNumber]] == 0):
            input("什么事也没发生。")
        if (Maps[PlayerPos[playerNumber]] == 1):
            inp = input(
                "玩家{0}踩到了幸运轮盘，请选择 1--交换位置 2--轰炸对方".format(PlayerNames[playerNumber]))
            while (True):
                if (inp == "1"):
                    input(
                        "玩家{0}选择跟玩家{1}交换位置".format(PlayerNames[playerNumber], PlayerNames[1 - playerNumber]))
                    temp = PlayerPos[playerNumber]
                    PlayerPos[playerNumber] = PlayerPos[1 -
                                                        playerNumber]
                    PlayerPos[1 - playerNumber] = temp
                    break
                elif (inp == "2"):
                    input(
                        "玩家{0}选择轰炸玩家{1},玩家{2}退6格".format(PlayerNames[playerNumber], PlayerNames[1 - playerNumber], PlayerNames[1 - playerNumber]))
                    PlayerPos[1 - playerNumber] -= 6
                    break
                else:
                    inp = input("只能输入1或者2  1--交换位置 2--轰炸对方")
        if (Maps[PlayerPos[playerNumber]] == 2):
            input("玩家{0}踩到了地雷,退6格".format(PlayerNames[playerNumber]))
            PlayerPos[playerNumber] -= 6
        if (Maps[PlayerPos[playerNumber]] == 3):
            input("玩家{0}踩到了暂停，暂停一回合".format(PlayerNames[playerNumber]))
            Flags[playerNumber] = True
        if (Maps[PlayerPos[playerNumber]] == 4):
            input("玩家{0}踩到了时空隧道，前进10格".format(PlayerNames[playerNumber]))
            PlayerPos[playerNumber] += 10
    ChangePos()
    os.system('cls')
    DrawMap()

def ChangePos():
    if (PlayerPos[0] < 0):
        PlayerPos[0] = 0
    if (PlayerPos[0] >= 99):
        PlayerPos[0] = 99
    if (PlayerPos[1] < 0):
        PlayerPos[1] = 0
    if (PlayerPos[1] >= 99):
        PlayerPos[1] = 99

main()