import os
import zipfile

from keras.layers import Convolution2D, Flatten, Activation
from keras.models import Model

from race_model import VGGFace


def loadModel():
    model = VGGFace.baseModel()
    classes = 6
    base_model_output = Convolution2D(classes, (1, 1), name='predictions')(model.layers[-4].output)
    base_model_output = Flatten()(base_model_output)
    base_model_output = Activation('softmax')(base_model_output)
    race_model = Model(inputs=model.input, outputs=base_model_output)

    with zipfile.ZipFile(os.path.join('race_model', 'models', 'race_model_single_batch.zip'), 'r') as zip_ref:
        zip_ref.extractall(os.path.join('race_model', 'models', 'race_model_single_batch.h5'))

    race_model.load_weights(
        os.path.join('race_model', 'models', 'race_model_single_batch.h5', 'race_model_single_batch.h5'))
    return race_model
