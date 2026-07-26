"""
Duplicate File Finder
---------------------
A simple tool that scans a folder (and all its sub-folders) and finds
files that are exact duplicates of each other, based on their content
(not just their name).

How it works:
1. Walk through every file in the given folder.
2. Group files that have the same size (files with different sizes
   can never be duplicates, so this step saves time).
3. For files that share the same size, calculate an MD5 hash of the
   content and compare the hashes.
4. Files with the same hash are duplicates.

Author: Rinas
"""

import os
import hashlib


def get_file_hash(filepath, block_size=65536):
    """Calculate the MD5 hash of a file by reading it in small chunks
    (so we don't load huge files fully into memory)."""
    hasher = hashlib.md5()
    try:
        with open(filepath, "rb") as f:
            buf = f.read(block_size)
            while buf:
                hasher.update(buf)
                buf = f.read(block_size)
    except (PermissionError, FileNotFoundError):
        # Some files might be locked or removed while scanning, just skip them
        return None
    return hasher.hexdigest()


def find_duplicates(folder_path):
    """Scan folder_path and return a dictionary of duplicate files.

    Returns:
        A dict where each key is a hash and the value is a list of
        file paths that share that hash (only groups with more than
        one file are included, since a single file has no duplicate).
    """

    # Step 1: group files by size first
    files_by_size = {}

    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                file_size = os.path.getsize(filepath)
            except OSError:
                continue

            files_by_size.setdefault(file_size, []).append(filepath)

    # Step 2: within each size group, compare hashes
    files_by_hash = {}

    for size, file_list in files_by_size.items():
        # No point hashing a file if it's the only one with that size
        if len(file_list) < 2:
            continue

        for filepath in file_list:
            file_hash = get_file_hash(filepath)
            if file_hash is None:
                continue
            files_by_hash.setdefault(file_hash, []).append(filepath)

    # Step 3: only keep hash groups with more than 1 file (actual duplicates)
    duplicates = {h: paths for h, paths in files_by_hash.items() if len(paths) > 1}

    return duplicates


def print_report(duplicates):
    """Print out the duplicate groups in a readable way."""
    if not duplicates:
        print("No duplicate files found.")
        return

    total_wasted_space = 0
    group_number = 1

    for file_hash, paths in duplicates.items():
        print(f"\nDuplicate Group {group_number}: ({len(paths)} files)")
        for p in paths:
            print(f"  {p}")

        # All files in the group are the same size, so use the first one
        file_size = os.path.getsize(paths[0])
        # Wasted space = size * (number of copies - 1), since we'd keep 1 copy
        wasted = file_size * (len(paths) - 1)
        total_wasted_space += wasted

        group_number += 1

    print(f"\nTotal duplicate groups found: {len(duplicates)}")
    print(f"Total wasted space: {total_wasted_space / (1024 * 1024):.2f} MB")


def delete_duplicates(duplicates):
    """Ask the user which files to keep and delete the rest, group by group."""
    for file_hash, paths in duplicates.items():
        print("\nDuplicate group:")
        for i, p in enumerate(paths, start=1):
            print(f"  [{i}] {p}")

        choice = input(
            f"Enter the number of the file to KEEP (1-{len(paths)}), "
            f"or press Enter to skip this group: "
        )

        if choice.strip() == "":
            print("Skipped.")
            continue

        try:
            keep_index = int(choice) - 1
            if keep_index < 0 or keep_index >= len(paths):
                print("Invalid number, skipping this group.")
                continue
        except ValueError:
            print("Invalid input, skipping this group.")
            continue

        for i, p in enumerate(paths):
            if i != keep_index:
                try:
                    os.remove(p)
                    print(f"Deleted: {p}")
                except OSError as e:
                    print(f"Could not delete {p}: {e}")


def main():
    folder_path = input("Enter the folder path to scan: ").strip()

    if not os.path.isdir(folder_path):
        print("That folder path does not exist. Please check and try again.")
        return

    print(f"\nScanning '{folder_path}' for duplicate files...")
    duplicates = find_duplicates(folder_path)
    print_report(duplicates)

    if duplicates:
        answer = input("\nDo you want to review and delete duplicates now? (y/n): ")
        if answer.strip().lower() == "y":
            delete_duplicates(duplicates)
        else:
            print("No files were deleted.")


if __name__ == "__main__":
    main()
