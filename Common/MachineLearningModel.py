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
from livelossplot.inputs.keras import PlotLossesCallback
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import numpy as np
from glob import glob
from pathlib import Path
from PIL import Image
from tensorflow.keras.models import load_model
import os


class MachineLearningModel:
    def __init__(self, method):
        print("Machine Learning Model Initialized")
        self.method = method
        os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
    
    def Train(self):
        BATCH_SIZE = 32
        IMAGE_SIZE = [299, 299]
        
        train_path = "Datasets/{}/Splits/train".format(self.method)
        valid_path = "Datasets/{}/Splits/val".format(self.method)
        
        num_classes = glob(train_path + "/*")
        
        train_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)
        val_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)
        
        training_set = train_datagen.flow_from_directory(train_path, target_size = (299, 299), batch_size = BATCH_SIZE, class_mode = 'categorical', seed=42)
        val_set = val_datagen.flow_from_directory(valid_path, target_size = (299, 299), batch_size = BATCH_SIZE, class_mode = 'categorical', seed=42)
        
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
        n_epochs = 50
        
        plot_loss_1 = PlotLossesCallback()
        
        # ModelCheckpoint callback - save best weights
        Path("Model/{}".format(self.method)).mkdir(parents=True, exist_ok=True)
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
                            callbacks=[tl_checkpoint_1, early_stop, plot_loss_1],
                            verbose=1)
        
    def ValidateImage(self, image):
        model = self.LoadModel()
        im = Image.fromarray(image, 'RGB')
        #Resizing into 128x128 because we trained the model with this image size.
        img_array = np.array(im)
        #Our keras model used a 4D tensor, (images x height x width x channel)
        #So changing dimension 128x128x3 into 1x128x128x3 
        img_array = np.expand_dims(img_array, axis=0)
        pred = model.predict(img_array)
        return pred
    
    def LoadModel(self):
        return load_model("Model/{}/tl_model_v1.weights.best.hdf5".format(self.method))