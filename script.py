import xml.etree.ElementTree as ET
import os
import sys

def convert_to_markdown(node):
    md_content = ""

    if 'name' in node.attrib:
        heading_level = node.attrib.get('heading_level', '1')
        md_content += f"{'#' * int(heading_level)} {node.attrib['name']}\n"

    for child in node:
        if child.tag == 'rich_text':
            md_content += convert_rich_text(child)
        elif child.tag == 'node':
            md_content += convert_to_markdown(child)
        elif child.tag == 'cherrytree':
            # Handle CherryTree specific content (if needed)
            pass
        elif child.tag == 'codebox':
            # Handle codebox content
            md_content += f"```\n{child.text}\n```\n"
        elif child.tag == 'encoded_png':
            # Handle encoded_png content (if needed)
            pass
        elif child.tag == 'bookmarks':
            # Handle bookmarks content (if needed)
            pass

    return md_content

def convert_rich_text(rich_text):
    md_content = ""
    for child in rich_text:
        if child.tag == 'bold':
            md_content += '**' + convert_rich_text(child) + '**'
        elif child.tag == 'italic':
            md_content += '*' + convert_rich_text(child) + '*'
        elif child.tag == 'list':
            md_content += convert_list(child)
        else:
            md_content += child.text or ''
            md_content += convert_rich_text(child)

    return md_content

def convert_list(list_element):
    md_content = "\n"
    for item in list_element.findall('listitem'):
        md_content += "- " + convert_rich_text(item) + "\n"
    return md_content

def convert_ctd_file(input_ctd_file, output_directory):
    # Extract the second directory name as the output name
    folder_names = os.path.dirname(input_ctd_file).split(os.path.sep)
    output_name = " - ".join(folder_names[1:])

    # Use the determined output name for the output file
    output_md_file = os.path.join(output_directory, f"{output_name}.md")

    md_content = convert_to_markdown(ET.parse(input_ctd_file).getroot())

    with open(output_md_file, 'w', encoding='utf-8') as md_file:
        md_file.write(md_content)

    print(f"Conversion successful: {input_ctd_file} -> {output_md_file}")





def convert_all_ctd_files(input_folder, output_directory):
    for folder_path, _, files in os.walk(input_folder):
        for file_name in files:
            if file_name.endswith(".ctd"):
                input_ctd_file = os.path.join(folder_path, file_name)
                convert_ctd_file(input_ctd_file, output_directory)

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py input_folder output_directory heading_level")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_directory = sys.argv[2]

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    heading_level = sys.argv[3]

    convert_all_ctd_files(input_folder, output_directory)

    print("Conversion completed.")

if __name__ == "__main__":
    main()

