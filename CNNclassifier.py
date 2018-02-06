#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 19:25:48 2018

@author: bhargav
"""

import keras
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

##The Architecture
classifier=Sequential()
classifier.add(Convolution2D(filters=32,kernel_size=(3,3),activation='relu',data_format='channels_last',input_shape=(128,128,3)))
classifier.add(MaxPooling2D(pool_size=(2,2)))
classifier.add(Convolution2D(filters=32,kernel_size=(3,3),activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))
classifier.add(Flatten())
classifier.add(Dense(units=128,activation='relu'))
classifier.add(Dense(units=1,activation='sigmoid'))
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

#Image Preprocessing
from keras.preprocessing.image import ImageDataGenerator
train_datagen=ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True,vertical_flip=True)
test_datagen=ImageDataGenerator(rescale=1./255)

trainingset=train_datagen.flow_from_directory('Datasets/train',target_size=(128,128),batch_size=32,class_mode='binary')
testset=test_datagen.flow_from_directory('Datasets/test',target_size=(128,128),class_mode='binary')

classifier.fit_generator(trainingset,steps_per_epoch=75,epochs=10,validation_data=testset,validation_steps=1666)