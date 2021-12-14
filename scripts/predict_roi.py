import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from keras.models import load_model


def read_images(path):
    """
    read images from directory
    """

    lst_im = []
    with os.scandir(path) as entries:
        for entry in entries:
            lst_im.append(cv2.imread(path + '\\' + entry.name))

    return lst_im


def plot_image(prediction, img, i):
    """
    plot image, mark it regarding prediction and save it
    """

    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = prediction[0]
    class_names = {0: 'car', 1: 'no car'}

    plt.xlabel("{}".format(class_names[round(predicted_label)]), fontsize=20)
    plt.savefig(r'D:\Efim\thesis\roi\footage' + r'\roi_%05d.png' % i)
    plt.close()


def main():

    car_path = r'D:\Efim\thesis\roi\all'
    images_car = read_images(car_path)
    all_images = np.array(images_car)
    model = load_model(r'D:\Efim\thesis\video_model_1.h5')
    predictions = model.predict(all_images)
    print(predictions.shape)
    np.save(r'D:\Efim\thesis\predictions_video_2.npy', predictions)
    for x in range(0, len(predictions)):
        plot_image(predictions[x], all_images[x], x)


if __name__ == '__main__':

    main()
