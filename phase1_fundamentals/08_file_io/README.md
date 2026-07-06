# File I/O  (Day 12-13)

## Overview

Reading and writing files safely with context managers, working with text/CSV/JSON formats, and basic filesystem operations with pathlib/os.

## Key Concepts

- open() modes: r, w, a, r+, b (binary) variants
- Context managers: `with open(...) as f:` for automatic file closing
- Reading: .read(), .readline(), .readlines(), iterating a file object
- Writing/appending text files
- csv module: reading/writing CSV files (csv.reader, csv.DictWriter)
- json module: json.load/loads, json.dump/dumps for serialization
- pathlib.Path for modern, cross-platform path handling (vs os.path)

## Gotchas

- Forgetting to close files without `with` — resource leaks
- Opening in 'w' mode truncates/overwrites existing file content
- Encoding issues — always specify encoding='utf-8' explicitly

## Search Keywords

Use these to look things up when you need more depth:

- `python with statement context manager`
- `python read write csv files`
- `python json module tutorial`
- `python pathlib vs os.path`
- `python file encoding utf-8`

## References

**Official Docs**
- [Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [pathlib](https://docs.python.org/3/library/pathlib.html)
- [json](https://docs.python.org/3/library/json.html)

**YouTube (search these titles)**
- "python file handling tutorial"
- "python pathlib tutorial"
- "python json module tutorial"

**Books**
- Automate the Boring Stuff (ch. 8-9, 14-16)
- Python Crash Course — Eric Matthes (ch. 10)

## My Notes

(Write concepts in your own words here as you learn — future-you is the audience.)
