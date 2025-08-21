import os
from datetime import datetime
from diff_detector import get_diff
from summarise_diff import generate_summary

def update_changelog(old_file, new_file, file_type):
    diff = get_diff(old_file, new_file)
    summary = generate_summary(diff)

    header = f"## {file_type.upper()} Update: {os.path.basename(old_file)} → {os.path.basename(new_file)}\n"
    timestamp = f"**Timestamp:** {datetime.now().isoformat()}\n"
    entry = f"{header}{timestamp}\n{summary}\n\n"

    with open("CHANGELOG.md", "a", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Auto-update changelog from IaC/Helm diffs")
    parser.add_argument("--old", required=True, help="Path to old file")
    parser.add_argument("--new", required=True, help="Path to new file")
    parser.add_argument("--type", required=True, choices=["helm", "iac"], help="Type of file")

    args = parser.parse_args()
    update_changelog(args.old, args.new, args.type)