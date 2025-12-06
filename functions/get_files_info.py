import os


def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    abs_full_path = os.path.abspath(full_path)
    abs_working_dir = os.path.abspath(working_directory)

    if not abs_full_path.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(abs_full_path):
        return f'Error: "{directory}" is not a directory'

    dir_list = os.listdir(abs_full_path)

    try:
        file_names = []

        for item in dir_list:
            filepath = os.path.join(abs_full_path, item)
            file_size = os.path.getsize(filepath)
            is_dir = os.path.isdir(filepath)
            item_info = f"- {item}: file_size={file_size} bytes, is_dir={is_dir}"
            file_names.append(item_info)

        result = "\n".join(file_names)

        return result

    except Exception as e:
        return f"Error: {e}"
