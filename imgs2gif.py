from PIL import Image
import os

def create_gif_from_frames(image_folder, output_gif, duration=150, loop=0):
    """
    Combines a series of images into an animated GIF.
    
    Parameters:
        image_folder (str): Path to the folder containing the images.
        output_gif (str): Path to save the generated GIF.
        duration (int): Duration of each frame in milliseconds. Default is 100ms.
        loop (int): Number of loops (0 = infinite loop). Default is 0.
    """
    # Get all image file paths in the folder, sorted by name
    images = sorted(
        [os.path.join(image_folder, img) 
         for img in os.listdir(image_folder) if img.endswith(('.png', '.jpg', '.jpeg'))]
    )
    
    # Open the images
    frames = [Image.open(img) for img in images]
    
    # Create and save the GIF
    if frames:
        frames[0].save(
            output_gif,
            save_all=True,
            append_images=frames[1:],
            duration=duration,
            loop=loop,
        )
        print(f"GIF created successfully: {output_gif}")
    else:
        print("No images found in the specified folder.")

# Example usage
if __name__ == "__main__":
    image_folder = "cancel_img_sq"  # Replace with your folder containing images
    output_gif = "cancel_sq.gif"    # Replace with your desired GIF file name
    create_gif_from_frames(image_folder, output_gif)
