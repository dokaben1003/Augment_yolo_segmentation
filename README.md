# Image Augmentation Script

This script is designed for augmenting image datasets by creating flipped versions of the images and appropriately adjusting their corresponding annotations. This is particularly useful for increasing the size of your dataset and introducing more variability, which can help improve the robustness of machine learning models.

## Features

- Generates flipped versions of images: horizontally, vertically, and both.
- Adjusts the annotations corresponding to the flipped images.
- Saves the augmented images and their corresponding annotations in a specified directory.
- Can process a directory of images and annotations at once.

## Requirements

- Python 3.x
- PIL (Pillow)
- OpenCV (optional, if additional image processing features are needed)
- numpy (optional, if additional mathematical operations are needed)

## Usage

1. Install the required Python packages if you haven't already:

```
pip install Pillow opencv-python numpy
```


2. Clone this repository or download the script to your local machine.

3. Place your images and corresponding annotation files in a directory. Ensure that the annotation files have the same base filename as their corresponding images.

4. Run the script from the command line, specifying the input directory (containing the images and annotation files) and the output directory (where you want the augmented images and adjusted annotations to be saved):

```
python <script_name>.py --inputDir <path_to_input_directory> --outputDir <path_to_output_directory>
```


Replace `<script_name>.py` with the name of the script, `<path_to_input_directory>` with the path of your input directory, and `<path_to_output_directory>` with the path of your output directory.

## Example

```
python augment_images.py --inputDir ./original_images --outputDir ./augmented_images
```


This command will process all images in the `./original_images` directory and save the augmented images and adjusted annotations in the `./augmented_images` directory.

## Contributing

Contributions, issues, and feature requests are welcome!
