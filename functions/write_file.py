import os


def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory, file_path)
    abs_full_path = os.path.abspath(full_path)

    if not abs_full_path.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        if os.path.exists(abs_full_path):
            with open(abs_full_path, "w") as f:
                f.write(content)
                return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

        else:
            directory_name = os.path.dirname(abs_full_path)
            os.makedirs(directory_name, exist_ok=True)
            with open(abs_full_path, "w") as f:
                f.write(content)
                return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"
