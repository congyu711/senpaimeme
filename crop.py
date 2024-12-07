from PIL import Image
import os

def crop_to_square(image_path, output_path, target_size=(270, 270)):
    """
    Crops an image to a square, keeping only the center part.

    Parameters:
        image_path (str): Path to the input image.
        output_path (str): Path to save the cropped image.
        target_size (tuple): Size of the square (default is 270x270).
    """
    with Image.open(image_path) as img:
        width, height = img.size
        
        # Calculate the cropping box to center the square
        left = (width - target_size[0]) // 2
        top = (height - target_size[1]) // 2
        right = left + target_size[0]
        bottom = top + target_size[1]
        
        # Crop and save the result
        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.save(output_path)
        print(f"Cropped and saved: {output_path}")

def process_images_in_folder(input_folder, output_folder, target_size=(270, 270)):
    """
    Processes all PNG images in a folder by cropping them to squares.
    
    Parameters:
        input_folder (str): Path to the input folder containing images.
        output_folder (str): Path to the output folder to save cropped images.
        target_size (tuple): Size of the square to crop (default 270x270).
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):
            image_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            crop_to_square(image_path, output_path, target_size)

# Example usage
if __name__ == "__main__":
    input_folder = "cancel_img"  # Replace with your input folder
    output_folder = "cancel_img_sq"  # Replace with your desired output folder
    process_images_in_folder(input_folder, output_folder)
