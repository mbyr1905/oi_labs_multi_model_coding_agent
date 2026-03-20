def validate_code_structure(code_data):
    issues = []

    if not code_data or "files" not in code_data:
        issues.append("Missing files key")

    for file in code_data.get("files", []):
        if "path" not in file or "content" not in file:
            issues.append(f"Invalid file structure: {file}")

        if not file["content"].strip():
            issues.append(f"Empty file: {file['path']}")

    return issues