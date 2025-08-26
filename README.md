# SVS Image Patch Extractor and Analyzer

This project is designed for efficiently extracting and analyzing image patches from large SVS files. It provides functionalities for selective patch extraction based on tissue characteristics and offers various visualization tools for analyzing the extracted patches.

## 📜 Table of Contents

* [Key Features](#-key-features)
* [Getting Started](#-getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Code Structure](#-code-structure)
* [Usage](#-usage)
  * [patch_extractor](#1-patch_extractor)
  * [analyze_patch](#2-analyze_patch)
* [Methodology](#-methodology)

## ✨ Key Features

* **Efficient Patch Extraction**: Optimized for handling large SVS files.
* **Conditional Filtering**: Extract only the desired image patches based on user-defined conditions.
* **In-depth Analysis**:
  * Calculates the RGB channel covariance matrix.
  * Extracts features based on eigenvalues and eigenvectors.
  * Saves analysis results to a CSV file.
* **Advanced Visualization**:
  * 2D scatter plots based on eigenvector projection.
  * Interactive 3D scatter plots of RGB pixel values using Plotly.

## 🚀 Getting Started

### Prerequisites

* **Conda**: This project uses Conda for environment management. Make sure you have Anaconda or Miniconda installed.

### Installation

1. Navigate to the `env` directory.
2. Install the required packages using the `requirements.txt` file:

   ```bash
   conda create --name svs_patch_env python=3.8
   conda activate svs_patch_env
   pip install -r requirements.txt
   ```
## 📁 Code Structure

The project is organized into two main modules:

1. **`patch_extractor`**: Contains scripts for extracting patches from SVS files.
2. **`analyze_patch`**: Contains notebooks and scripts for analyzing the extracted image patches.

## 💻 Usage

### 1. `patch_extractor`

This module is used to extract image patches from `.svs` files.

* **`extract_patch.py`**:
* **Functionality**: Extracts image patches from an SVS file, distinguishing between tissue and background using eigenvalue analysis.
* **Libraries**: `openslide`, `numpy`, `PIL`, `os`
* **Usage**:
 ```
 # Set the target path to save patches
 target_path = r'/path/to/save/patches/'
 
 # Set the root directory of the SVS files
 svs_root = '/path/to/svs/files'
 ```

* **`region_extract.py`**:
* **Functionality**: Extracts a patch of a specific size from designated coordinates.
* **Libraries**: `openslide`, `PIL`
* **Usage**: Use the `extract_patch` function by setting `slide_path`, `x`, `y`, and `tile_size`.

* **`naming.py`**:
* **Functionality**: Renames the extracted patch image files sequentially.
* **Libraries**: `os`, `glob`
* **Usage**:
 ```
 rename_files_with_numbering(
     folder_path='/path/to/images',
     prefix='patch_',
     start_num=1,
     num_digits=3,
     extension_filter=['*.png', '*.jpg', '*.jpeg']
 )
 ```

### 2. `analyze_patch`

This module is used for analyzing and visualizing the extracted patches.

* **`plt.ipynb`**:
* **Functionality**: Performs image feature analysis and visualization. It calculates the RGB covariance matrix, analyzes eigenvalues/eigenvectors, and generates scatter plots.

* **`3d_scatter_plot.py`**:
* **Functionality**: Visualizes the RGB pixel values of an image in a 3D space using Plotly for an interactive experience.

* **`project.ipynb`**:
* **Functionality**: Projects RGB data points onto a plane defined by the top three eigenvectors for 2D visualization while retaining RGB color information.

## 🔬 Methodology

The core of this project lies in its ability to differentiate tissue from the background in whole slide images. This is achieved by:

1. Calculating the **RGB Covariance Matrix** for image patches.
2. Computing the **eigenvalues and eigenvectors** from this matrix.
3. Applying a set of **judgement conditions** based on the mean of RGB channels and the calculated eigenvalues to filter out background and markings, thereby isolating tissue-only patches.

This algorithm allows for the rapid and accurate extraction of relevant tissue regions from large datasets.