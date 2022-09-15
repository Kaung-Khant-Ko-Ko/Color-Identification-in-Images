import matplotlib
import streamlit as st
from PIL import Image
import cv2
from sklearn.cluster import KMeans
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import io


def RGB2HEX(color: list) -> str:
    color = list(map(lambda value: value / 255.0, color))
    hex = matplotlib.colors.to_hex(color)
    return hex


def load_image(image: st.uploaded_file_manager.UploadedFile) -> np.ndarray:
    image = Image.open(image)
    image = np.array(image)
    return image


def get_color_palette(image: np.ndarray, img_buf: io.BytesIO, num_colors: int) -> np.ndarray:
    height, width, _ = image.shape
    image = cv2.resize(image, (width // 2, height // 2))

    pixel_values = image.reshape((-1, 3))

    km = KMeans(n_clusters=num_colors, random_state=0)
    labels = km.fit_predict(pixel_values)

    centers = km.cluster_centers_
    hex_values = [RGB2HEX(center) for center in centers]
    rgb_values = list(map(lambda value: value / 255.0, centers))

    explode_part = np.zeros(num_colors)
    values = list(Counter(labels).values())
    id = values.index(max(values))
    explode_part[id] = 0.1

    plt.figure(figsize=(num_colors + 2, num_colors + 2))
    plt.pie(values, labels=hex_values, colors=rgb_values, explode=explode_part)
    plt.legend(title="Colors", loc="best")
    plt.savefig(img_buf, format="png")
    color_palette = Image.open(img_buf)
    return color_palette
