# chromb

A simple command-line tool to convert Google Drive file links into direct download links.

## Installation

1.  **Make the script executable:**

    ```bash
    chmod +x chromb.py
    ```

2.  **Create a symbolic link to a directory in your PATH:**

    ```bash
    ln -s /path/to/chromb.py /usr/local/bin/chromb
    ```

    *Replace `/path/to/` with the actual path to the `chromb.py` script, and `/usr/local/bin/` with a directory in your system's PATH.*

## Usage

```bash
chromb <drive_download_link_url>
```

### Example

```bash
chromb https://drive.google.com/file/d/1LDRlyZaZTF-bxHjBDEiL2obMxYHtf3YT/view?usp=sharing
```

**Output:**

```
https://drive.google.com/uc?export=download&id=1LDRlyZaZTF-bxHjBDEiL2obMxYHtf3YT
```
