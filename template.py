import os



# Function to parse the file and create directories and files
def parse_and_create_structure(template_file):
    try:
        with open(template_file, 'r') as file:
            lines = file.readlines()

        for line in lines:
            # Clean the line (strip whitespace and newlines)
            line = line.strip()

            # Check if it's a file or directory
            if '->' in line:
                # It's a file
                file_path = line.replace('->', '').strip()  # Remove '->'
                dir_path = os.path.dirname(file_path)
                
                # Create directory if it doesn't exist
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)
                    print(f"Directory created: {dir_path}")

                # Create the file
                with open(file_path, 'w') as f:
                    pass  # Create an empty file
                print(f"File created: {file_path}")

            else:
                # It's a directory
                if not os.path.exists(line):
                    os.makedirs(line)
                    print(f"Directory created: {line}")

    except Exception as e:
        print(f"Error: {e}")

# Write the template file
template_file = 'directory_structure_template.txt'
write_template_file(template_file)

# Parse and create directories and files
parse_and_create_structure(template_file)
