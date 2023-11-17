import json

def resolve_conflict_in_notebook(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    resolved_lines = []
    keep_line = True

    for line in lines:
        if line.startswith('<<<<<<< HEAD'):
            keep_line = True
            continue
        elif line.startswith('======='):
            keep_line = False
            continue
        elif line.startswith('>>>>>>>'):
            keep_line = True
            continue

        if keep_line:
            resolved_lines.append(line)

    resolved_content = ''.join(resolved_lines)

    # Check if the resolved content is valid JSON
    try:
        json.loads(resolved_content)
    except json.JSONDecodeError:
        raise ValueError("Resolved file is not valid JSON. Manual intervention required.")

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(resolved_content)

# Replace 'path_to_your_notebook.ipynb' with the path to your notebook file
resolve_conflict_in_notebook('main_copy.ipynb')
