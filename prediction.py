import joblib as jb
import os
# import tensorflow as tf
from keras.models import load_model
def predict(data):
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    print(files)
    # preprocess = load_model("preprocessor.sav
    preprocess = load_model("./preprocessor.keras")
    tensor_data = preprocess(data)
    # reg = jb.load("tensor_model.h5")
    # return reg.predict(tensor_data)
    return reg;
