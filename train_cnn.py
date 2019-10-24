from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend
from keras import optimizers
from keras.utils.vis_utils import plot_model


if __name__ == '__main__':

    img_width, img_height = 107, 223  # dimensions of video

    train_data_dir = r'D:\Efim\thesis\roi\train'
    validation_data_dir = r'D:\Efim\thesis\roi\validation'
    nb_train_samples = 2000
    nb_validation_samples = 800
    epochs = 600
    batch_size = 16

    if backend.image_data_format() == 'channels_first':
        input_shape = (3, img_width, img_height)
    else:
        input_shape = (img_width, img_height, 3)

    model = Sequential()
    model.add(Conv2D(64, (3, 3), input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(128, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    sgd = optimizers.SGD(lr=0.001)

    model.compile(loss='binary_crossentropy',
                  optimizer=sgd,
                  metrics=['accuracy'])
    plot_model(model, to_file=r'C:\Users\EfimIakubovich\Desktop\thesis report\model_plot.png', show_shapes=True,
               show_layer_names=True)
    print('saved')

    # this is the augmentation configuration we will use for training
    train_datagen = ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

    # use rescaling for augmentation
    test_datagen = ImageDataGenerator(rescale=1. / 255)

    train_generator = train_datagen.flow_from_directory(
        train_data_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='binary')

    validation_generator = test_datagen.flow_from_directory(
        validation_data_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='binary')

    model.fit_generator(
        train_generator,
        steps_per_epoch=nb_train_samples // batch_size,
        epochs=epochs,
        validation_data=validation_generator,
        validation_steps=nb_validation_samples // batch_size)

    # model.save_weights(r'D:\Efim\thesis\audio_weights.h5')
    model.save_weights(r'D:\Efim\thesis\video_weights_3.h5')
    # model.save(r'D:\Efim\thesis\audio_model.h5')
    model.save(r'D:\Efim\thesis\video_model_3.h5')
