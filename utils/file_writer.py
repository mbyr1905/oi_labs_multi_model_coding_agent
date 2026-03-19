import os


def write_files(base_dir: str, files: list, mode: str = "overwrite"):
    created_files = []
    updated_files = []

    for file in files:
        file_path = os.path.normpath(os.path.join(base_dir, file["path"]))
        content = file["content"]

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # 🔍 Check if file exists
        if os.path.exists(file_path):

            if mode == "skip":
                continue

            elif mode == "append":
                with open(file_path, "a", encoding="utf-8") as f:
                    f.write("\n" + content)
                updated_files.append(file_path)

            elif mode == "overwrite":
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                updated_files.append(file_path)

        else:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            created_files.append(file_path)

    return {
        "created": created_files,
        "updated": updated_files
    }