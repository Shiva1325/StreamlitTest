import joblib as jb
# import tensorflow as tf
from keras.models import load_model
def predict(data):
    preprocess = load_model("preprocessor.sav")
    tensor_data = preprocess(data)
    # reg = jb.load("tensor_model.sav")
    # return reg.predict(tensor_data)
    return tensor_data;
