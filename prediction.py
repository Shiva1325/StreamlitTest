import joblib as jb
import tensorflow as tf
def predict(data):
    preprocess = tf.keras.models.load_model("preprocessor.keras")
    tensor_data = preprocess(data)
    # reg = jb.load("tensor_model.sav")
    # return reg.predict(tensor_data)
    return tensor_data;
