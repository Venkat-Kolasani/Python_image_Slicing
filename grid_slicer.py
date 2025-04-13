import os
import argparse
from PIL import Image

def slice_image(input_path, output_dir, slice_width, slice_height, overlap=0, prefix="slice"):
    """
    Slice an image into a 4x4 grid.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    with Image.open(input_path) as img:
        # Get original image dimensions
        img_width, img_height = img.size
        
        # Calculate dimensions for 4x4 grid
        slice_width = img_width // 4
        slice_height = img_height // 4
        
        base_filename = os.path.splitext(os.path.basename(input_path))[0]
        slice_count = 0
        
        # Create 4x4 grid slices
        for y in range(4):
            for x in range(4):
                # Calculate slice boundaries
                left = x * slice_width
                upper = y * slice_height
                right = left + slice_width
                lower = upper + slice_height
                
                # Create slice
                slice_img = img.crop((left, upper, right, lower))
                
                # Generate organized filename
                output_filename = f"{prefix}_{base_filename}_part_{x+1}x{y+1}.png"
                output_path = os.path.join(output_dir, output_filename)
                
                # Save slice
                slice_img.save(output_path)
                slice_count += 1
                print(f"Created slice: {output_filename}")
        
        return slice_count

def process_folder(input_dir, output_dir, slice_width, slice_height, overlap=0, prefix="slice", extensions=(".jpg", ".jpeg", ".png")):
    """
    Process all images in a folder and its subfolders.
    
    Args:
        input_dir (str): Input directory containing images
        output_dir (str): Output directory for sliced images
        slice_width (int): Width of each slice
        slice_height (int): Height of each slice
        overlap (int, optional): Overlap between slices. Defaults to 0.
        prefix (str, optional): Prefix for output filenames. Defaults to "slice".
        extensions (tuple, optional): File extensions to process. Defaults to (".jpg", ".jpeg", ".png").
    
    Returns:
        tuple: (number of images processed, total number of slices created)
    """
    total_images = 0
    total_slices = 0
    
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(extensions):
                # Construct relative path for organized output
                rel_path = os.path.relpath(root, input_dir)
                if rel_path == ".":
                    rel_path = ""
                    
                # Construct input and output paths
                input_path = os.path.join(root, file)
                current_output_dir = os.path.join(output_dir, rel_path)
                
                try:
                    # Process the image
                    num_slices = slice_image(
                        input_path, 
                        current_output_dir, 
                        slice_width, 
                        slice_height, 
                        overlap, 
                        prefix
                    )
                    
                    total_images += 1
                    total_slices += num_slices
                    
                except Exception as e:
                    print(f"Error processing {input_path}: {str(e)}")
    
    return total_images, total_slices

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Slice images into smaller pieces with organized naming.')
    parser.add_argument('input', help='Input image file or directory')
    parser.add_argument('output', help='Output directory for sliced images')
    parser.add_argument('--width', type=int, default=256, help='Width of each slice (default: 256)')
    parser.add_argument('--height', type=int, default=256, help='Height of each slice (default: 256)')
    parser.add_argument('--overlap', type=int, default=0, help='Overlap between slices in pixels (default: 0)')
    parser.add_argument('--prefix', default='slice', help='Prefix for output filenames (default: "slice")')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Check if input is a file or directory
    if os.path.isfile(args.input):
        # Process single file
        slice_image(
            args.input, 
            args.output, 
            args.width, 
            args.height, 
            args.overlap, 
            args.prefix
        )
    elif os.path.isdir(args.input):
        # Process directory
        total_images, total_slices = process_folder(
            args.input, 
            args.output, 
            args.width, 
            args.height, 
            args.overlap, 
            args.prefix
        )
        print(f"Processed {total_images} images, created {total_slices} slices in total.")
    else:
        print(f"Error: Input path '{args.input}' does not exist.")

if __name__ == "__main__":
    main()