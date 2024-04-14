from flask import Flask, request, render_template
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
import io
from Translate import translate_it
from Wiki import summarize, get_monument_name
import os

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "static", "model_with_mobilenetv2_94.41.h5")
label_mapping_path = os.path.join(current_dir, "static", "label_mapping.pkl")

app = Flask(__name__)

model = tf.keras.models.load_model(model_path)
with open(
    label_mapping_path,
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
        summary = summarize(predicted_class)
        lang = request.form.get("language")
        translated = translate_it(summary[:500], lang)
        return render_template(
            "index.html",
            predicted_class=get_monument_name(predicted_class),
            translated=translated,
        )


if __name__ == "__main__":
    app.run(debug=True)
