import matplotlib.pyplot as plt
import numpy as np
import torch
import cv2


def main():

    class_names = {0:'car', 1:'no car'}
    i = 0
    names = np.load(r'D:\Efim\thesis\fastai\items_test_ds.npy', allow_pickle = True)
    preds = torch.load(r'D:\Efim\thesis\fastai\preds.pt')
    pred_names = dict(zip(names, np.argmax(preds, axis=1)))
    for k,v in pred_names.items():
        print(i)
        i = i+1
        img = cv2.imread(k.as_posix())
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img)
        predicted_label = v.item()

        plt.xlabel("{}".format(class_names[predicted_label]), fontsize=20)
        plt.savefig(k.as_posix())
        plt.close()

if __name__ == '__main__':

    main()
