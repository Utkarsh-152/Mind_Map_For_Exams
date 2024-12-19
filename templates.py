import os

def create_file_structure():
    # Define the project structure
    structure = {
        "app": [
            "app.py",
            ".env",
            "__init__.py",
            "utils.py"
        ],
        "main": {
            "main.py": None,
            "templates": ["index.html", "result.html"],
            "static": ["styles.css", "script.js"]
        },
        "requirements.txt": None,
        "README.md": None
    }

    def create_dir(base_path, substructure):
        if isinstance(substructure, dict):
            for folder, contents in substructure.items():
                folder_path = os.path.join(base_path, folder)
                os.makedirs(folder_path, exist_ok=True)
                if contents:
                    create_dir(folder_path, contents)
        elif isinstance(substructure, list):
            for file in substructure:
                file_path = os.path.join(base_path, file)
                if file_path.endswith("/"):
                    os.makedirs(file_path, exist_ok=True)
                else:
                    with open(file_path, 'w') as f:
                        pass
        elif isinstance(substructure, str):
            with open(os.path.join(base_path, substructure), 'w') as f:
                pass

    # Create the root directory structure
    for root, content in structure.items():
        if isinstance(content, list) or isinstance(content, str):
            if root.endswith("/"):
                os.makedirs(root, exist_ok=True)
            elif isinstance(content, list):
                os.makedirs(root, exist_ok=True)
                create_dir(root, content)
            else:
                with open(root, 'w') as f:
                    pass
        elif isinstance(content, dict):
            os.makedirs(root, exist_ok=True)
            create_dir(root, content)

create_file_structure()
