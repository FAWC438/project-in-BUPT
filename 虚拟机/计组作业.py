import time
import os
import logging

PC = 0
AR = 0
AC = 0
TF = 0
RANGE = 20
PSW = ''
DR = ''
IR = ''
# 设置日志文件，以便在控制台输出同时在文件中输出
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt", encoding="utf-8", mode="w")
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

logger.addHandler(handler)
logger.addHandler(console)


if __name__ == '__main__':
    begin = int(input('请输入指令起始PC地址:'))
    RANGE = int(input('请输入内存总大小（请根据指令的范围选择稍大的内存！）:'))
    end = begin
    PC = begin  # PC初始化
    exceptionFlag = 0  # 跳转指令死循环判断器
    flag = ''  # 接收调试模式用户输入
    data = ['' for i in range(RANGE)]  # 内存

    # 从文件中读取
    with open(r'test.txt', 'r') as in_file:
        s = in_file.readline()
        while s != '':
            data[end] = s.strip()
            end += 1
            s = in_file.readline()
        in_file.close()

    while PC < RANGE:

        # 调试模式
        if TF == 1:
            os.system('cls')  # 清屏
            logger.info('\n\n\n')
            if flag is not '':
                logger.info('输入为' + flag + '，已进入下一步调试\n')
            for i in range(RANGE):
                # 输出100块内存空间的内容，并高亮显示当前运行的代码
                if i == PC:
                    logger.info('> 第' + str(i) + '行：' + data[i])
                else:
                    logger.info('第' + str(i) + '行：' + data[i])
            logger.info(
                '-----------------------------------------------------------')
            logger.info('正在调试模式中，现在执行的PC地址（行数）是：' + str(PC))
            logger.info('当前参数值    AR:' + str(AR) + '    AC:' + str(AC) + '    DR:' + DR + '    IR:' + IR)
            logger.info('输入q键并按回车键退出，输入其它按键并按回车键继续：')
            flag = input()
            if flag == 'q'or flag == 'Q':
                TF = 0
                logger.info('退出调试模式！')
                time.sleep(2)
                os.system('cls')
                continue

        # exceptionFlag代表重复执行了多少次相同的跳转代码，若超过一定程度认为是死循环
        if exceptionFlag >= 10:
            logger.info('成功从死循环中退出！循环执行次数为' + str(exceptionFlag) + '次')
            time.sleep(2)
            break

        # 取指流程 T1
        logger.info('已进入第' + str(PC) + '行指令的取指流程')
        AR = PC  # 计数器地址存入地址寄存器
        PC += 1  # 计数器加一
        PSW = 0  # 默认状态
        DR = data[AR]  # 每次读取一条指令
        if DR == '\n' or DR == '' or (ord(DR[0]) >= ord('0') and ord(DR[0]) <= ord('9')):
            # 如果遇到立即数而非指令，或是内存中这个地址没有指令
            logger.info('指令文本第' + str(PC - 1) + '行不是一个指令！程序退出...')
            time.sleep(2)
            break
        DR = DR.upper()
        if ' ' in DR:
            # 读取某些带目标地址的指令
            temp = DR.split()
            AR = int(temp[1])
            IR = temp[0]
        else:
            # 不带目标地址的指令
            IR = DR

        # 执行流程 T2
        logger.info('已进入第' + str(PC - 1) + '行指令的执行流程')
        if IR == 'CLA':
            # 清零
            logger.info('执行第' + str(PC - 1) + '行的CLA指令')
            AC = 0
        elif IR == 'ADD':
            # 累加
            logger.info('执行第' + str(PC - 1) + '行的ADD指令')
            DR = data[AR]
            if not DR.isdigit():
                logger.info('第' + str(PC - 1) + '行的ADD指令目标地址错误！程序退出...')
                time.sleep(2)
                break
            AC += int(DR)
            if AC > 999999:
                # 溢出
                AC = AC % 1000000
                PSW = 'V'
                logger.info('状态寄存器改变，值为：' + PSW)
            elif AC == 0:
                # 为零
                PSW = 'Z'
                logger.info('状态寄存器改变，值为：' + PSW)
        elif IR == 'STA':
            # 存入
            logger.info('执行第' + str(PC - 1) + '行的STA指令')
            data[AR] = str(AC)
        elif IR == 'JMP':
            # 跳转指令容易发生死循环，设置exceptionFlag，当循环超过一定次数时将退出程序
            if AR <= PC:
                exceptionFlag += 1
            else:
                exceptionFlag = 0
            # 跳转
            logger.info('执行第' + str(PC - 1) + '行的JMP指令')
            PC = AR
        elif IR == 'NOP':
            # NOP产生延迟
            t = 2
            logger.info('执行第' + str(PC - 1) + '行NOP延时中，延时为' + str(t) + '秒')
            time.sleep(t)
        elif IR == 'STOP':
            # 单步调试暂停命令
            TF = 1
            logger.info('第' + str(AR) + '行执行STOP指令，3秒后进入调试模式')
            time.sleep(3)
        else:
            logger.info('无法处理第' + str(PC - 1) + '行命令，程序退出')
            time.sleep(2)
            break
        logger.info(
            '-----------------------------------------------------------\n')

    os.system('cls')
    logger.info('\n\n\n')
    logger.info('------------以下是所有内存的情况------------')
    for i in range(RANGE):
        logger.info('第' + str(i) + '行：' + data[i])
    logger.info('------------以上是所有内存的情况------------')
    logger.info('程序结束，请到目录下log.txt文件查看运行日志')
    os.system('pause')
