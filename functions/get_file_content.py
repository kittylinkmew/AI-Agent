import os

from config import MAX_FILE_CHARS


def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory, file_path)
    abs_full_path = os.path.abspath(full_path)

    if not abs_full_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_full_path, "r") as f:
            content = f.read(MAX_FILE_CHARS + 1)

            if len(content) > MAX_FILE_CHARS:
                shortened_content = content[:MAX_FILE_CHARS]
                message = (
                    shortened_content
                    + f'\n[...File "{file_path}" truncated at {MAX_FILE_CHARS} characters]'
                )
                return message

            else:
                return content
    except Exception as e:
        return f"Error: {e}"
