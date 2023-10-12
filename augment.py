from PIL import Image, ImageDraw
import cv2  # Importing the OpenCV library (currently unused in the script, could be removed if not needed later).
import numpy as np  # Importing the numpy library for numerical operations (currently unused, could be removed if not needed later).
import os  # Importing the os library for interacting with the operating system.
import argparse  # Importing the argparse library for parsing command line arguments.

def augment(annotation_file, image_file, save_dir, filename):
    """
    Function to augment images by flipping them and adjust their corresponding annotations.

    :param annotation_file: Path to the file containing annotations for the image.
    :param image_file: Path to the image file to be augmented.
    :param save_dir: Directory where the augmented images and their annotations will be saved.
    :param filename: Base filename of the image and annotation, without extension.
    """

    # Load the image
    image = Image.open(image_file)

    # Load the annotation file
    with open(annotation_file, 'r') as file:
        lines = file.readlines()

    print(filename)
    # Generate flipped images and corresponding annotations
    for flip_type in ["original", "horizontal", "vertical", "both"]:
        
        flipped_image = image.copy()

        if flip_type == "horizontal":
            flipped_image = flipped_image.transpose(Image.FLIP_LEFT_RIGHT)
        elif flip_type == "vertical":
            flipped_image = flipped_image.transpose(Image.FLIP_TOP_BOTTOM)
        elif flip_type == "both":
            flipped_image = flipped_image.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.FLIP_TOP_BOTTOM)

        # Save the flipped image
        flipped_image.save(f"{save_dir}/{filename}_{flip_type}.png")
        print(f"{save_dir}/{filename}_{flip_type}.png")

        # Adjust annotations and save
        with open(f"{save_dir}/{filename}_{flip_type}.txt", 'w') as file:
            for line in lines:
                values = line.strip().split()
                class_index = values[0]
                coordinates = [float(x) for x in values[1:]]
                
                if flip_type == "horizontal" or flip_type == "both":
                    # Flip the even-indexed coordinates (x)
                    for i in range(0, len(coordinates), 2):
                        coordinates[i] = 1.0 - coordinates[i]

                if flip_type == "vertical" or flip_type == "both":
                    # Flip the odd-indexed coordinates (y)
                    for i in range(1, len(coordinates), 2):
                        coordinates[i] = 1.0 - coordinates[i]

                # Write the annotation to text
                annotation = " ".join([class_index] + [str(coord) for coord in coordinates])
                file.write(annotation + "\n")


def main(input_dir, output_dir):
    """
    Main function to process all images in a specified directory.

    :param input_dir: Directory containing the images to be processed.
    :param output_dir: Directory where processed images and annotations will be saved.
    """
    png_files = [f.split(".png")[0] for f in os.listdir(input_dir) if f.endswith('.png')]
    for filename in png_files:
        image_path = f"{input_dir}/{filename}.png"
        data_path = f"{input_dir}/{filename}.txt"
        save_dir = output_dir

        augment(data_path, image_path, save_dir, filename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script to augment images by flipping and adjusting annotations.')
    parser.add_argument('--inputDir', required=True, help='Directory containing images to be processed.')
    parser.add_argument('--outputDir', required=True, help='Directory where processed images will be saved.')
    
    args = parser.parse_args()

    main(args.inputDir, args.outputDir)
