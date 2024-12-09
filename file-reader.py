def read_and_modify_file():
    try:
        # Prompt the user for the input file name
        input_file = input("Enter the name of the file to read: ")
        
        # Attempt to open the file for reading
        with open(input_file, "r") as file:
            content = file.readlines()
        
        # Modify the content: Example - Add line numbers
        modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]
        
        # Ask for the output file name
        output_file = input("Enter the name of the new file to write to: ")
        
        # Write the modified content to the new file
        with open(output_file, "w") as file:
            file.writelines(modified_content)
        
        print(f"Modified content has been written to {output_file}.")
    
    except FileNotFoundError:
        print("Error: The file you specified does not exist. Please try again.")
    except IOError:
        print("Error: The file could not be read or written. Please check permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
