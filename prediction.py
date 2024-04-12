import joblib as jb
# import tensorflow as tf
import pickle
def predict(data):
    # preprocess = load_model("preprocessor.sav")
    filename = 'preprocessor.sav'
    preprocess = pickle.load(open(filename, 'rb'))
    tensor_data = preprocess(data)
    # reg = jb.load("tensor_model.sav")
    # return reg.predict(tensor_data)
    return tensor_data;
