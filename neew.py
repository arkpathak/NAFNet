import streamlit as st
from PIL import Image, ImageOps, ImageEnhance

# Function to process the image
def process_image(image, options):
    processed_image = image.copy()
    
    # Apply selected processing options
    if options['Resize']:
        size = (options['Width'], options['Height'])
        processed_image = processed_image.resize(size)
    if options['Rotate']:
        angle = options['Angle']
        processed_image = processed_image.rotate(angle)
    if options['Grayscale']:
        processed_image = ImageOps.grayscale(processed_image)
    if options['Brightness']:
        enhancer = ImageEnhance.Brightness(processed_image)
        processed_image = enhancer.enhance(options['Brightness_Level'])
    if options['Contrast']:
        enhancer = ImageEnhance.Contrast(processed_image)
        processed_image = enhancer.enhance(options['Contrast_Level'])
    if options['Saturation']:
        enhancer = ImageEnhance.Color(processed_image)
        processed_image = enhancer.enhance(options['Saturation_Level'])
    
    return processed_image

# Main function to create the UI
def main():
    st.title("Image Processing App")
    
    # Upload image
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Display uploaded image
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        
        # Sidebar with processing options
        st.sidebar.title("Processing Options")
        options = {}
        options['Resize'] = st.sidebar.checkbox("Resize")
        if options['Resize']:
            options['Width'] = st.sidebar.slider("Width", 10, 1000, 300)
            options['Height'] = st.sidebar.slider("Height", 10, 1000, 300)
        options['Rotate'] = st.sidebar.checkbox("Rotate")
        if options['Rotate']:
            options['Angle'] = st.sidebar.slider("Angle", -180, 180, 0)
        options['Grayscale'] = st.sidebar.checkbox("Convert to Grayscale")
        options['Brightness'] = st.sidebar.checkbox("Adjust Brightness")
        if options['Brightness']:
            options['Brightness_Level'] = st.sidebar.slider("Brightness Level", 0.1, 2.0, 1.0)
        options['Contrast'] = st.sidebar.checkbox("Adjust Contrast")
        if options['Contrast']:
            options['Contrast_Level'] = st.sidebar.slider("Contrast Level", 0.1, 2.0, 1.0)
        options['Saturation'] = st.sidebar.checkbox("Adjust Saturation")
        if options['Saturation']:
            options['Saturation_Level'] = st.sidebar.slider("Saturation Level", 0.1, 2.0, 1.0)
        
        # Process image on button click
        if st.button("Process"):
            # Convert uploaded image to PIL Image
            pil_image = Image.open(uploaded_image)
            
            # Process the image
            processed_image = process_image(pil_image, options)
            
            # Display processed image
            st.image(processed_image, caption="Processed Image", use_column_width=True)

        # Process image on backend button click
        if st.button("Process on Backend"):
            # Placeholder for backend processing logic
            st.write("Processing on backend...")
            
            # You can add backend processing logic here

if __name__ == "__main__":
    main()
