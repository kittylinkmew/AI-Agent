import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    abs_working_directory = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory, file_path)
    abs_full_path = os.path.abspath(full_path)

    if not abs_full_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_full_path):
        return f'Error: "{file_path}" does not exist or is not a regular file'

    if not abs_full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'

    try:
        command = ["python", abs_full_path]

        if args:
            command.extend(args) 

        result = subprocess.run(
            command,
            cwd=abs_working_directory,
            capture_output=True,
            text=True,
            timeout=30,
        )
        parts = []

        if result.returncode != 0:
            parts.append(f"Process exited with code {result.returncode}")

        stdout = (result.stdout or "").strip()
        stderr = (result.stderr or "").strip()

        if not stdout and not stderr:
            parts.append("No output produced")
        else:
            if stdout:
                parts.append(f"STDOUT: {stdout}")
            if stderr:
                parts.append(f"STDERR: {stderr}")

        output = "\n".join(parts)

        return output

    except Exception as e:
        return f"Error: executing Python file: {e}"
