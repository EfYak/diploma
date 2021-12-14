# importing os module
import os


def main():
    i = 0
    folder = r'D:\Efim\thesis\fastai\signal_mel'
    for filename in os.listdir(folder):
        print(i)
        dst = "\car_" + str(i) + ".png"
        src = folder + '\\' + filename
        dst = folder + dst
        # rename() function will
        # rename all the files
        os.rename(src, dst)
        i += 1


if __name__ == '__main__':
    main()