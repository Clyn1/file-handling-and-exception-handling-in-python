# Step 1: Open the original file and read
with open("original.txt", "r") as source_file:
    content = source_file.read()

# Step 2: Modify the content (example: uppercase it)
modified_content = content.upper()

# Step 3: Write to a new file
with open("modified.txt", "w") as new_file:
    new_file.write(modified_content)

print("File has been modified and saved as 'modified.txt'.")
