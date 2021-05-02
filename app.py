
import tensorflow as tf
import numpy as np
import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import pyngrok

st.set_option('deprecation.showfileUploaderEncoding', False)
st.title('                                  Covid_19 Detector')
html_temp = '''
<div style='background-color:tomato;padding:10px'>
<h2 style= 'color:white;text-align:center;'>Covid_19 MRI Classifier<h/2>
</div>
'''
st.markdown(html_temp,unsafe_allow_html=True)

st.text('''
        The coronavirus disease (COVID-19) is caused by a new strain of coronavirus (SARS-CoV-2)
        that has not been previously identified in humans. It was first reported to WHO on the 
        31st of December, 2019 in Wuhan, China.
        ''')
st.text('Provide URL of MRI Image for image classification')

@st.cache(allow_output_mutation=True)

def load_model():
    model = tf.keras.models.load_model('covid_model')
    return model

with st.spinner('Loading Model Into Memory....'):
    model = load_model()

classes = ['Covid19','Normal','Pneumoinia']

def scale(image):
    image = tf.cast(image, tf.float32)
    image /= 255.0

    return tf.image.resize(image,[150,150])

def decode_img(image):
    img = tf.image.decode_jpeg(image, channels=3)
    img = scale(img)
    return np.expand_dims(img, axis= 0)

path = st.text_input('Enter Image URL to Classify...', 'https://prod-images-static.radiopaedia.org/images/52197348/df1053d3e8896b53ef140773e10e26_big_gallery.jpeg')

if path is not None:
    content = requests.get(path).content

    st.write('Predicted Class :')
    with st.spinner('classifying...'):
        label = np.argmax(model.predict(decode_img(content)), axis=1)
        st.write(classes[label[0]])
    st.write('')
    image = Image.open(BytesIO(content))
    st.image(image, caption='Classified MRI Image', use_column_width=True)
