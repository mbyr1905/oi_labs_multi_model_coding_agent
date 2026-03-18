import os
from typing import List, Dict


def write_files(base_dir: str, files: List[Dict]):

    created_files = []

    for file in files:
        file_path = os.path.join(base_dir, file["path"])
        content = file["content"]

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        created_files.append(file_path)

    return created_files