# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 09:12:29 2021

@author: quinj
"""

from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.applications.inception_resnet_v2 import InceptionResNetV2
from tensorflow.keras.applications.inception_resnet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
# import if need to check graphs *Use spyder IDE
# from livelossplot.inputs.keras import PlotLossesCallback
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from Common.DatasetGenerator import DatasetGenerator
import numpy as np
from glob import glob
from PIL import Image
from tensorflow.keras.models import load_model
import os
import cv2
import sys
np.set_printoptions(threshold=sys.maxsize)


class MachineLearningModel:
    def __init__(self, method):
        print("Machine Learning Model Initialized")
        self.method = method
        os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
    
    def Train(self):
        
        ds = DatasetGenerator(self.method, "")
        ds.SplitData()
        
        BATCH_SIZE = 2
        IMAGE_SIZE = [320, 240]
        
        train_path = "Datasets/{}/Splits/train".format(self.method)
        valid_path = "Datasets/{}/Splits/val".format(self.method)
        
        num_classes = glob(train_path + "/*")
        
        train_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)
        val_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)
        
        training_set = train_datagen.flow_from_directory(train_path, target_size = (320, 240), batch_size = BATCH_SIZE, class_mode = 'categorical', seed=42)
        val_set = val_datagen.flow_from_directory(valid_path, target_size = (320, 240), batch_size = BATCH_SIZE, class_mode = 'categorical', seed=42)
        
        conv_base = InceptionResNetV2(input_shape=IMAGE_SIZE + [3], weights='imagenet', include_top=False)

        for layer in conv_base.layers:
            layer.trainable = False
        
        # our layers - you can add more if you want
        x = Flatten()(conv_base.output)
        # x = Dense(1000, activation='relu')(x)
        prediction = Dense(len(num_classes), activation='softmax')(x)
        
        # create a model object
        model = Model(inputs=conv_base.input, outputs=prediction)
        
        
        # tell the model what cost and optimization method to use
        model.compile(
          loss='categorical_crossentropy',
          optimizer=Adam(learning_rate=0.001),
          metrics=['accuracy']
        )
        
        n_steps = training_set.samples // BATCH_SIZE
        n_val_steps = val_set.samples // BATCH_SIZE
        n_epochs = 10
        
        # Run in spyder and add in model.fit callbacks to generate graph
        # lossesCallback = PlotLossesCallback()

        # ModelCheckpoint callback - save best weights
        os.makedirs("Model/{}".format(self.method), exist_ok=True) 
        tl_checkpoint_1 = ModelCheckpoint(filepath="Model/{}/tl_model_v1.weights.best.hdf5".format(self.method),
                                          save_best_only=True,
                                          verbose=1)
        
        # EarlyStopping
        early_stop = EarlyStopping(monitor='val_loss',
                                    patience=10,
                                    restore_best_weights=True,
                                    mode='min')
        
        history = model.fit(training_set,
                            batch_size=BATCH_SIZE,
                            epochs=n_epochs,
                            validation_data=val_set,
                            steps_per_epoch=n_steps,
                            validation_steps=n_val_steps,
                            callbacks=[tl_checkpoint_1, early_stop],
                            verbose=1)
        
    def ValidateImage(self, image, username):
        self.LoadClasses()
        model = self.LoadModel()
        image = np.uint8(image)
        try:
            print("Converting to RGB")
            image = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
        except:
            print("Image already RGB")
        print(image.shape)
        print("Resizing Image to 320 x 240")
        image = cv2.resize(image, (240, 320))
        im = Image.fromarray(image, 'RGB')
        print(im)
        #Resizing into 128x128 because we trained the model with this image size.
        img_array = np.array(im)
        #Our keras model used a 4D tensor, (images x height x width x channel)
        #So changing dimension 128x128x3 into 1x128x128x3 
        img_array = np.expand_dims(img_array, axis=0)
        x = preprocess_input(img_array)
        pred = model.predict(x)
        predicted_label_index = np.argmax(pred)
        print(pred)
        predicted_class = self.classList[predicted_label_index]
        print(predicted_class)
        if(username == predicted_class):
            return True
        else:
            return False
    
    def LoadModel(self):
        return load_model("Model/{}/tl_model_v1.weights.best.hdf5".format(self.method))
    
    def LoadClasses(self):
        BATCH_SIZE = 32
        train_path = "Datasets/{}/Splits/train".format(self.method)
        train_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)
        training_set = train_datagen.flow_from_directory(train_path, target_size = (320, 240), batch_size = BATCH_SIZE, class_mode = 'categorical', seed=42)
        classDictionary = training_set.class_indices
        self.classList = list(classDictionary)
        
        
        
