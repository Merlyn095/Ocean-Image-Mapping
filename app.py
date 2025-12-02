import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# Set the title of the app
st.title("🌊 Ocean Plastic Mapping")

# Load the trained model
@st.cache_resource
def load_trained_model():
    model = load_model("plastic_classifier_model.keras")
    return model

model = load_trained_model()

# Define class names
class_names = ['no-plastic', 'plastic']

# File uploader for image upload
uploaded_file = st.file_uploader("Upload an image to classify", type=["jpg", "jpeg", "png"])

# Classify button
if st.button("Classify"):
    if uploaded_file is not None:
        # Load and preprocess the image
        img = Image.open(uploaded_file).convert('RGB')
        img = img.resize((128, 128))  # Ensure this matches your model's expected input size
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        img_array /= 255.0  # Normalize the image

        # Make prediction
        prediction = model.predict(img_array)[0][0]
        predicted_class = class_names[int(prediction > 0.5)]
        confidence = prediction if prediction > 0.5 else 1 - prediction

        # Display the image and prediction
        st.image(img, caption="Uploaded Image", width=200)
        # st.image(img, caption="Uploaded Image", use_container_width=True)
        st.markdown(f"### Prediction: **{predicted_class}**")
        st.markdown(f"**Confidence:** {confidence:.2f}")
    else:
        st.warning("Please upload an image before clicking 'Classify'.")
