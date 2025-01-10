import os

def merge_files(file_list, output_file):
    merged_lines = set()
    try:
        for file_name in file_list:
            if not os.path.isfile(file_name):
                print(f"Warning: File {file_name} does not exist.")
                continue
            try:
                with open(file_name, 'r') as file:
                    for line in file:
                        merged_lines.add(line)
            except Exception as e:
                print(f"Error reading {file_name}: {e}")
        
        with open(output_file, 'w') as outfile:
            outfile.writelines(sorted(merged_lines))
        print(f"Files have been successfully merged into {output_file}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

file_list = ['file1.txt', 'file2.txt', 'file3.txt']
output_file = 'mergedFile.txt'
merge_files(file_list, output_file)
