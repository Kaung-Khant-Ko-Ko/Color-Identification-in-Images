# Color-Identification-in-Images

## <b> Overview </b>

The goal of this project is to create a tool that will extract input numbers of the most significant colors from the user-inputted image.

## <b> Install requirements </b>

```
pip3 install requirements.txt
```

## <b> Run app </b>

```
streamlit run app.py
```

## <b> Libraries Used </b>
<ul>
  <li> <b> Streamlit </b> for Front-end </li>
  <li> <b> OpenCV </b> for Image Processing </li>
  <li> <b> KMeans </b> for Color Clustering </li>
  <li> <b> Matplotlib </b> for Conversion between RGB to HEX </li>
  <li> <b> Numpy </b> for Mathematical Operations for Array </li>
  <li> <b> OS </b> </li>
  <li> <b> Zipfile </b> for creating zip file </li>
</ul>

## <b> Image Upload and Color Palette </b>

<img width="1440" alt="Screen Shot 2022-09-15 at 7 32 25 PM" src="https://user-images.githubusercontent.com/59255928/190410992-4fc5d362-31e6-4148-a57e-c271162bbdd2.png">

When a user uploads an image, the color palette of that input image is displayed.

## <b> References </b>
* The `sample_image.jpg` was taken from the reference article and the other 9 images from the `images` folder were taken from [Unsplash](https://unsplash.com/).
* [Reference Article](https://towardsdatascience.com/color-identification-in-images-machine-learning-application-b26e770c4c71)
