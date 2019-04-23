# coding: utf-8

from config import *
import data
import model

def defineArgs():
    """define args"""
    parser = argparse.ArgumentParser(description = "AI诗人.")
    parser.add_argument("-m", "--mode", help = "select mode by 'train' or test or head",
                        choices = ["train", "test", "head"], default = "test")
    return parser.parse_args()

if __name__ == "__main__":
    args = defineArgs()
    trainData = data.POEMS(trainPoems)
    MCPangHu = model.MODEL(trainData)
    if args.mode == "train":
        MCPangHu.train()
    else:
        if args.mode == "test":
            poems = MCPangHu.test()
        else:
            characters = input("please input chinese character:")
            poems = MCPangHu.testHead(characters)