import os

count = 1 

# Folder containing the .data files 
data_folder = 'data_files'

# Output header folder
header_folder = 'image_headers'

if not os.path.exists(header_folder):
  os.makedirs(header_folder)

for filename in os.listdir(data_folder):
  if filename.endswith('.data'):

    # Read image data
    with open(os.path.join(data_folder, filename), 'rb') as f:
      data = f.read()

    header_name = os.path.splitext(filename)[0] + '.h'
    header_path = os.path.join(header_folder, header_name)

    # Generate unique array name 
    array_name = f"{header_name[:-2]}_{count}"

    # Write header file
    with open(header_path, 'w') as f:
      
      f.write(f'const unsigned char {array_name}[] = {{')
      
      # Write image data bytes
      
      f.write('};\n')

      count += 1

print('Headers generated in folder: ', header_folder) 
