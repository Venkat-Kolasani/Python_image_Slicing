# Python Image Grid Slicer

A Python tool to slice images into a 4x4 grid with organized naming conventions. Useful for processing character images and creating training datasets.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Venkat-Kolasani/Python_image_Slicing.git
cd Python_image_Slicing
```

2. Install required dependencies:
```bash
pip install Pillow
```

## Usage

### Basic Command Structure
```bash
python grid_slicer.py <input_path> <output_path> --prefix <prefix_name>
```

### Examples

1. Process a single image:
```bash
python grid_slicer.py "path/to/image.png" "path/to/output" --prefix "char"
```

2. Process all images in a directory:
```bash
python grid_slicer.py "path/to/input/folder" "path/to/output/folder" --prefix "char"
```

### Options
- `--width`: Width of each slice (default: 256)
- `--height`: Height of each slice (default: 256)
- `--overlap`: Overlap between slices in pixels (default: 0)
- `--prefix`: Prefix for output filenames (default: "slice")

## Output Format
- Each image is split into a 4x4 grid (16 parts)
- Output files are named as: `<prefix>_<original_filename>_part_<x>x<y>.png`
- Example: `char_image1_part_1x1.png`, `char_image1_part_1x2.png`, etc.

## Supported Image Formats
- PNG
- JPEG/JPG

