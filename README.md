# CherryTree CTD to Markdown Converter

## Overview

This script converts CherryTree XML files to Markdown format. It traverses through a specified input directory, searches for `.ctd` files, and generates corresponding Markdown files in an output directory. The output file names are based on the second directory name or the `name` attribute in the `<node>` tag.

## Usage

### Requirements

- Python 3.x

### Running the Script

1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.

   ```bash
   cd path/to/cherrytree-to-markdown


python script.py input_folder output_directory

python script.py input_folder output_directory heading_level
