import streamlit as st
import cv2
import numpy as np
import img_color

def colorize_image(image):
    # Convert image to grayscale
    colour_img=img_color.colorizer(image)
    
    return colour_img

def main():
    st.title("Image Colorization App")
    
    # Upload input image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Read uploaded image
        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
        
        # Colorize image
        colorized_image = colorize_image(image)
        
        # Display colorized image
        st.image(colorized_image, channels="BGR")
    
if __name__ == "__main__":
    main()