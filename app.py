import streamlit as st
import helper
import io

st.set_page_config(page_title="Color Extractor", page_icon="🎨", layout="wide")


def main():
    header = st.container()
    upload_image = st.container()
    tune = st.container()
    extract_color_palette = st.container()

    with header:
        st.markdown("<h1 style = 'text-align : center'> Color Extractor </h1>",
                    unsafe_allow_html=True)

    with upload_image:
        image = st.file_uploader("Choose An Image File to Extract Color Palette From:", type=[
            "jpg", "png", "svg", "JPG", "jpeg", "JPEG", "PNG", "SVG"])

    with tune:
        if image is not None:
            num_colors = st.slider(
                "Number of colors to extract from the image", 2, 20, 10)

    with extract_color_palette:
        if image is not None:
            left_col, right_col = st.columns(2)
            with left_col:
                IMAGE_WINDOW = st.image([])
            with right_col:
                COLOR_PALETTE_WINDOW = st.image([])

            image = helper.load_image(image)
            IMAGE_WINDOW.image(image)

            img_buf = io.BytesIO()
            color_palette = helper.get_color_palette(
                image, img_buf, num_colors)
            COLOR_PALETTE_WINDOW.image(color_palette)
            img_buf.close()


if __name__ == "__main__":
    main()
