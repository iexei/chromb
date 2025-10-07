#!/usr/bin/env python3

import argparse
import re

def extract_file_id(url):
    """Extracts the file ID from a Google Drive URL."""
    match = re.search(r"/d/([^/]+)", url)
    if match:
        return match.group(1)
    return None

def main():
    """Main function for the chromb tool."""
    parser = argparse.ArgumentParser(description="Create a direct download link for a Google Drive file.")
    parser.add_argument("url", help="The Google Drive URL of the file.")
    args = parser.parse_args()

    file_id = extract_file_id(args.url)

    if file_id:
        download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
        print(download_url)
    else:
        print("Could not find file ID in the URL.")

if __name__ == "__main__":
    main()