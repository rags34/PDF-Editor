import fitz
import os
import sys

def file_merge(file1, file2, out_folder):
    # Open the first and second PDF files
    doc_a = fitz.open(file1)
    doc_b = fitz.open(file2)

    # Merge the documents
    doc_a.insert_pdf(doc_b)
    
    # Get the unique output file path
    outfile = close_file(out_folder, "merged.pdf")
    
    # Save the merged document
    doc_a.save(outfile)

def add_watermark(file1, file2, out_folder):
    # Open the PDF file
    doc = fitz.open(file1)

    # Add an image watermark to each page
    for page_index in range(len(doc)):
        page = doc[page_index]
        page.insert_image(page.rect, filename=file2, overlay=False)

    # Get the unique output file path
    outfile = close_file(out_folder, "watermarked.pdf")
    
    # Save the document with the watermark
    doc.save(outfile)

def rotate_file(file, out_folder):
    # Open the PDF file
    doc = fitz.open(file)

    # Prompt user for rotation angle
    a = int(input("Enter the angle of rotation: "))

    # Rotate the pages
    for page_index in range(len(doc)):
        page = doc[page_index]
        page.set_rotation(a)

    # Get the unique output file path
    outfile = close_file(out_folder, "rotated.pdf")
    
    # Save the document with the rotated page
    doc.save(outfile)

def rearrange_file(file, out_folder):
    # Open the PDF file
    doc = fitz.open(file)

    # Prompt user for page numbers to rearrange
    print("Enter the page numbers you want to rearrange:")
    a = int(input('Page 1: '))
    b = int(input('Page 2: '))

    # Rearrange the specified pages
    doc.move_page(a, b)

    # Get the unique output file path
    outfile = close_file(out_folder, "rearranged.pdf")
    
    # Save the document with rearranged pages
    doc.save(outfile)

def close_file(out_folder, default_name):
    # Prompt user for the output file name
    file = input("Enter the name of the output file (without extension): ")
    
    # Construct the output file path with a ".pdf" extension
    file_path = os.path.join(out_folder, f"{file}.pdf" if file else default_name)

    # Ensure the output file path is unique
    count = 1
    while os.path.exists(file_path):
        file_path = f'{file_path}_{count}'
        count += 1

    return file_path

def open_file(in_folder):
    # Prompt user for the input file name
    file = input("Enter the name of the file you want to edit: ")
    
    # Construct the input file path
    file_path = os.path.join(in_folder, file)
    
    # Check if the file exists; exit if not
    if os.path.isfile(file_path):
        return file_path
    else:
        print(f"{file} does not exist")
        sys.exit(1)

if __name__ == '__main__':
    # User interface
    print("(When prompted, type the serial no. corresponding to the actions shown here)\nACTIONS-->\n1. MERGE\n2. ADD WATERMARK\n3. ROTATE ANY ONE PAGE\n4. REARRANGE ANY TWO PAGES")
    
    # Prompt user for the desired action
    action = input("Please enter the action you want to perform: ")

    in_folder = "./input_folder/"
    out_folder = "./output_folder/"

    if action == '1':
        # Merge action
        print("First file:")
        file1 = open_file(in_folder)
        print("Second file:")
        file2 = open_file(in_folder)
        file_merge(file1, file2, out_folder)

    elif action == '2':
        # Add watermark action
        print("First file:")
        file1 = open_file(in_folder)
        print("Watermark file:")
        file2 = open_file(in_folder)
        add_watermark(file1, file2, out_folder)

    elif action == '3':
        # Rotate action
        print("File to rotate:")
        file = open_file(in_folder)
        rotate_file(file, out_folder)

    elif action == '4':
        # Rearrange action
        print("File to rearrange:")
        file = open_file(in_folder)
        rearrange_file(file, out_folder)

    else:
        # Invalid action
        print("Please enter a valid action")
