#  Ocean Plastic Mapping

This project is a web-based application for detecting plastic in ocean images using a Convolutional Neural Network (CNN). It allows users to upload an image and receive a prediction on whether plastic is present or not.

## Features

- Upload `.jpg`, `.jpeg`, or `.png` images
- Classifies image as **plastic** or **no-plastic**
- Displays the prediction result with confidence score
- Interactive UI built with **Streamlit**

## Model

The model used in this application is a binary image classifier trained to detect plastic in ocean scenes. It accepts 128x128 RGB images and outputs a probability indicating the presence of plastic.

Model file: `plastic_classifier_model.keras`

## 🛠️ Requirements

- Python 3.7+
- TensorFlow
- Streamlit
- Pillow
- NumPy

You can install dependencies with:

```bash
pip install -r requirements.txt
```

### `requirements.txt` (sample)
```
streamlit
tensorflow
pillow
numpy
```

## 🚀 Usage

1. Clone this repository or download the files.

2. Place your trained model (`plastic_classifier_model.keras`) in the same directory as `app.py`.

3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. Open the web browser (usually at `http://localhost:8501`) and upload an image to classify.

## 📂 File Structure

```
.
├── app.py                         # Main Streamlit application
├── plastic_classifier_model.keras # Trained Keras model (not included)
├── Ocean_Plastic_Mapping_Model.ipynb  # Training notebook (optional)
└── README.md                     # This file
```

## Example Output

- **Prediction:** `plastic`
- **Confidence:** `0.87`

## License

This project is for educational and research purposes only.

---

> Developed as part of a sustainability-focused AI initiative.
