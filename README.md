# Color-Identification-in-Images

## <b> Overview </b>

The goal of this project is to create a tool that will extract input number of colors from an image.

## <b> Install requirements </b>

```
(base) kaungkhantkoko@Kaungs-MacBook-Air ~ % pip3 install requirements.txt
```

## <b> Run app </b>

```
(base) kaungkhantkoko@Kaungs-MacBook-Air ~ % streamlit run app.py
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



When a user uploads an image, the color palette of that input image is displayed.

## <b> References </b>
* The `sample_image.jpg` was taken from reference article and the other 9 images from `images` folder were taken from [Unsplash](https://unsplash.com/).
* [Reference Article](https://towardsdatascience.com/color-identification-in-images-machine-learning-application-b26e770c4c71)