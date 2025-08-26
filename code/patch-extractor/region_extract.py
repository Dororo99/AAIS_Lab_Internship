import openslide
from PIL import Image

def extract_patch(slide_path, x, y, tile_size):
    """
    Open a slide file and extract a patch of given size at specified coordinates.
    
    Parameters:
    - slide_path: str, path to the slide file
    - x: int, x-coordinate of the top-left corner of the patch
    - y: int, y-coordinate of the top-left corner of the patch
    - tile_size: tuple, (width, height) of the patch to extract

    Returns:
    - patch: PIL.Image, extracted patch
    """
    # Open the slide
    slide = openslide.OpenSlide(slide_path)

    # Extract the region of the specified size at the (x, y) location
    patch = slide.read_region((x, y), 0, tile_size)
    
    # Convert the image from RGBA to RGB
    patch = patch.convert("RGB")
    
    # Close the slide after reading
    slide.close()
    
    return patch

# Example usage
slide_path = '/home/dororo99/data/TCGA-DQ-7591-01Z-00-DX1.8304B939-542C-4D30-8C77-F705DE1311FF.svs'  # replace with the actual path to your slide file
x = 20580  # x-coordinate
y = 10632  # y-coordinate
tile_size = (1024,1024)  # width and height of the patch

# Extract the patch
patch = extract_patch(slide_path, x, y, tile_size)

# Display or save the patch
# patch.show()  # To display
patch.save("output_patch.png")  # To save the patch as an image file