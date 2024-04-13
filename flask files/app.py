from flask import Flask, request, render_template
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
import io

app = Flask(__name__)

model = tf.keras.models.load_model(
    "C:/Users/CHARVI UPRETI/Documents/GitHub/Unveiling-India-s-Heritage/flask files/model_with_mobilenetv2_94.72.h5"
)
with open(
    "C:/Users/CHARVI UPRETI/Documents/GitHub/Unveiling-India-s-Heritage/flask files/label_mapping.pkl",
    "rb",
) as f:
    label_mapping = pickle.load(f)


@app.route("/")
def index():
    return render_template("index.html", predicted_class=None)


@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["file"]
    if file.filename == "":
        return render_template("index.html", predicted_class="No file selected")

    if file:
        img = image.load_img(io.BytesIO(file.read()), target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = preprocess_input(img_array)
        img_array = np.expand_dims(img_array, axis=0)
        predicted_label = model.predict(img_array)
        predicted_class = label_mapping[np.argmax(predicted_label)]
        return render_template("index.html", predicted_class=predicted_class)


if __name__ == "__main__":
    app.run(debug=True)
