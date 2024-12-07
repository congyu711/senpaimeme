from PIL import Image
import os

def gif2imgs(gif_path, output_folder):
    """
    Splits a GIF into individual frames and saves them as separate image files.
    
    Parameters:
        gif_path (str): Path to the input GIF file.
        output_folder (str): Directory where the frames will be saved.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    try:
        with Image.open(gif_path) as gif:
            frame_index = 0
            while True:
                # Save each frame as an image
                frame_path = os.path.join(output_folder, f"frame_{frame_index:03d}.png")
                gif.save(frame_path, format="PNG")
                print(f"Saved: {frame_path}")
                
                frame_index += 1
                gif.seek(frame_index)  # Move to the next frame
    except EOFError:
        # Reached the end of the GIF
        print("Finished extracting frames.")

gifpath=r'input_gifs/senpai.gif'
imgfolder=os.path.splitext(os.path.basename(gifpath))[0]+'_img'

gif2imgs(gifpath,imgfolder)