import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def read_tsdata(filename):
    """
    load time series data from binary file
    return time,z,y,x (i.e. dim = 4 x nTimeStamps); time in ns
    """
    data = np.fromfile(filename, dtype=np.dtype('f'))
    lsize = int(len(data) / 4)
    normdata = np.reshape(data, (lsize, 4))
    return normdata.T


def vibro_image(i, yy):
    """
    plot slice of signal
    save to file
    """

    width = 199
    dst_fname = r'D:\Efim\thesis\vibro_images' + '\window' + str(i / width) + '.png'
    finish = i + width

    fig, ax = plt.subplots(2, figsize=(12, 5))
    fig.subplots_adjust(hspace=0.5)
    ax[0].plot(yy[0, i:i + width * 3] / 1e9, yy[1, i:i + width * 3])
    ax[0].axvline(i / 1e9, c='r')
    ax[1].plot(yy[0, i:finish] / 1e9, yy[1, i:finish])
    plt.savefig(dst_fname)
    plt.close(fig)


def main():

    myfn = r'D:\Efim\thesis\vibration-master\sampledata\dat0-07.bin'
    yy = read_tsdata(myfn)
    last = len(yy[0])

    for i in range(0, last, 199):
        vibro_image(i, yy)
        print(i / 199) #print current number


if __name__ == '__main__':

    main()