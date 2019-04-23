import os, random, pygame
Maps, PlayerPos, PlayerNames, Flags = [0 for i in range(100)], [0 for i in range(2)], ['', ''], [False, False]
def main():
    pygame.mixer.init()
    pygame.mixer.music.load('1.mp3')
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1, 0.0)
    PlayerNames[0] = input("请输入玩家A的姓名：")
    PlayerNames[1] = input("请输入玩家B的姓名：")
    print ("\n" * 100)
    print("玩家{0}用A表示，玩家{1}用B表示".format(PlayerNames[0], PlayerNames[1]))
    luckyturn = [6, 23, 40, 55, 69, 83]
    for i in range(len(luckyturn)):Maps[luckyturn[i]] = 1
    landMine = [5, 13, 17, 33, 38, 50, 64, 80, 94]
    for i in range(len(landMine)):Maps[landMine[i]] = 2
    pause = [9, 27, 60, 93, 2, 3, 4, 7, 8]
    for i in range(len(pause)):Maps[pause[i]] = 3
    DrawMap()
    while (PlayerPos[0] < 99 and PlayerPos[1] < 99):
        if (Flags[0] == False):PlayGame(0)
        if (PlayerPos[0] >= 99):
            print("玩家{0}无耻的赢了玩家{1}".format(PlayerNames[0], PlayerNames[1]))
            pygame.mixer.music.stop()
            pygame.mixer.music.load('2.mp3')
            pygame.mixer.music.play(1,0)
            while (1):
                s=input("玩家{0}是真正的秋名山逮虾户！！！（按E键以退出）".format(PlayerNames[0]))
                if(s=='e'or s=='E'):return
        if (Flags[1] == False):PlayGame(1)
        if (PlayerPos[1] >= 99):
            print("玩家{0}无耻的赢了玩家{1}".format(PlayerNames[1], PlayerNames[0]))
            pygame.mixer.music.stop()
            pygame.mixer.music.load('2.mp3')
            pygame.mixer.music.play(1,0)
            while (1):
                s=input("玩家{0}是真正的秋名山逮虾户！！！（按E键以退出）".format(PlayerNames[1]))
                if(s=='e'or s=='E'):return
        Flags[0], Flags[1] = False, False
def DrawMap():
    print("图例:幸运轮盘:※   地雷:☆   暂停:Δ   玩家1：A   玩家2：B   玩家重叠：<>")
    for i in range(30): print(DrawStringMap(i), end='')
    print()
    for i in range(30, 35):
        for j in range(29):print("  ", end='')
        print(DrawStringMap(i))
    for i in range(63, 34, -1):print(DrawStringMap(i), end='')
    for i in range(64, 69):print(DrawStringMap(i))
    for i in range(69, 100): print(DrawStringMap(i), end='')
    print()
def DrawStringMap(i):
    s = ""
    if (PlayerPos[0] == PlayerPos[1] and PlayerPos[0] == i):s = "<>"
    elif(PlayerPos[0] == i):s = "A"
    elif(PlayerPos[1] == i):s = "B"
    else:
        if(Maps[i] == 0):s = "★"
        if(Maps[i] == 1):s = "※"
        if(Maps[i] == 2):s = "☆"
        if(Maps[i] == 3):s = "Δ"
    return s
def PlayGame(playerNumber):
    rNumber = random.randint(1, 7)
    input("{0}按任意键开始掷骰子".format(PlayerNames[playerNumber]))
    input("{0}掷出了{1},按任意键开始行动".format(PlayerNames[playerNumber], rNumber))
    PlayerPos[playerNumber] += rNumber
    if (PlayerPos[playerNumber] < 0):PlayerPos[0] = 0
    if (PlayerPos[playerNumber] >= 99):PlayerPos[0] = 99
    if (PlayerPos[playerNumber] == PlayerPos[1 - playerNumber]):
        input("玩家{0}踩到了玩家{1}，玩家{1}退6格".format(PlayerNames[playerNumber], PlayerNames[1 - playerNumber]))
        PlayerPos[1 - playerNumber] -= 6
    else:
        if (Maps[PlayerPos[playerNumber]] == 0):input("什么事也没发生。")
        if (Maps[PlayerPos[playerNumber]] == 1):
            inp = input(
                "玩家{0}踩到了幸运轮盘，请选择 1--交换位置 2--轰炸对方".format(PlayerNames[playerNumber]))
            while (True):
                if (inp == "1"):
                    input("玩家{0}选择跟玩家{1}交换位置".format(PlayerNames[playerNumber], PlayerNames[1 - playerNumber]))
                    temp = PlayerPos[playerNumber]
                    PlayerPos[playerNumber] = PlayerPos[1 - playerNumber]
                    PlayerPos[1 - playerNumber] = temp
                    break
                elif (inp == "2"):
                    input("玩家{0}选择轰炸玩家{1},玩家{2}退6格".format(PlayerNames[playerNumber], PlayerNames[1 - playerNumber], PlayerNames[1 - playerNumber]))
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
    
    print ("\n" * 100)
    DrawMap()
main()