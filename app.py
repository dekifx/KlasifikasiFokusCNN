from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

# Load the trained model
model_path = "models/mental_state_classifier_cnn.h5"
trained_model = load_model(model_path)

# Define the image size
img_size = (128, 128)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the uploaded image file
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            # Save the file to a temporary location
            image_path = "temp_image.png"
            uploaded_file.save(image_path)

            # Load and preprocess the image
            img = image.load_img(image_path, target_size=img_size)
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array /= 255.0

            # Make predictions
            predictions = trained_model.predict(img_array)

            # Get the predicted class
            predicted_class = int(np.argmax(predictions[0]))

            # Return the predicted class as JSON
            return jsonify({'prediction': predicted_class})

    except Exception as e:
        return jsonify({'error': str(e)})

    return jsonify({'error': 'No file uploaded'})

if __name__ == '__main__':
    app.run(debug=True)
