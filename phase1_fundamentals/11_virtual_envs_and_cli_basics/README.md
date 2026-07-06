# Virtual Environments & CLI Basics  (Day 17)

## Overview

Isolating project dependencies with virtual environments, managing packages with pip, and writing scripts that accept command-line arguments.

## Key Concepts

- Why virtual environments: dependency isolation per project
- venv: creation, activation/deactivation, deleting an environment
- pip: install, uninstall, list, freeze; requirements.txt workflow
- Version pinning (==, >=) and why it matters for reproducibility
- sys.argv basics vs argparse for structured CLI argument parsing
- argparse: positional args, optional flags, --help generation, subcommands

## Gotchas

- Forgetting to activate the venv before installing packages (global pollution)
- Committing the venv folder to git instead of just requirements.txt
- Not pinning versions — 'works on my machine' problems later

## Search Keywords

Use these to look things up when you need more depth:

- `python venv tutorial`
- `pip freeze requirements.txt`
- `python argparse tutorial`
- `python virtual environment best practices`
- `python dependency management`

## References

**Official Docs**
- [venv](https://docs.python.org/3/library/venv.html)
- [argparse](https://docs.python.org/3/library/argparse.html)
- [Installing Packages (pip)](https://packaging.python.org/en/latest/tutorials/installing-packages/)

**YouTube (search these titles)**
- "python venv tutorial"
- "python argparse tutorial"
- "pip and requirements.txt explained"

**Books**
- Automate the Boring Stuff (appendix on installing third-party modules)
- Python Crash Course — Eric Matthes (setup appendix)

## My Notes

(Write concepts in your own words here as you learn — future-you is the audience.)
