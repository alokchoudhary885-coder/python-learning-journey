"""
Python Learning Journey - Universal Terminal Code Runner
=========================================================
Easily run any practice script, chapter topic, or run a complete test across
all chapters without worrying about directory paths or quotes.

Usage:
    python run.py                 # Interactive menu to select and run any file
    python run.py --all           # Test and run all 48 Python scripts
    python run.py <keyword>       # Search and run matching file (e.g. 'pattern', 'numpy', 'dsa')
    python run.py <chapter_num>   # List/run files in a specific chapter (e.g. '4', '8')
"""

import os
import sys
import subprocess

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))


def get_all_python_files():
    """Discover all Python scripts across all chapters."""
    py_files = []
    for root, dirs, files in os.walk(REPO_ROOT):
        # Exclude git, venv, and the runner itself
        if ".git" in root or ".venv" in root or "__pycache__" in root:
            continue
        for file in files:
            if file.endswith(".py") and file != "run.py":
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, REPO_ROOT)
                py_files.append((rel_path, full_path))
    py_files.sort(key=lambda x: x[0].lower())
    return py_files


def run_single_file(file_path, interactive=True):
    """Executes a Python file with appropriate cwd and environment."""
    file_dir = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    rel_path = os.path.relpath(file_path, REPO_ROOT)

    print("\n" + "=" * 65)
    print(f"  RUNNING: {rel_path}")
    print("=" * 65)

    env = os.environ.copy()
    existing_pythonpath = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = (
        f"{file_dir};{REPO_ROOT};{existing_pythonpath}"
        if sys.platform == "win32"
        else f"{file_dir}:{REPO_ROOT}:{existing_pythonpath}"
    )

    try:
        # Run with cwd set to file directory so relative imports work seamlessly
        proc = subprocess.run([sys.executable, file_name], cwd=file_dir, env=env)
        print("=" * 65)
        if proc.returncode == 0:
            print(f"[SUCCESS] {file_name} finished cleanly (code 0).\n")
        else:
            print(f"[EXIT CODE {proc.returncode}] {file_name} returned non-zero code.\n")
        return proc.returncode == 0
    except Exception as e:
        print(f"[ERROR] Failed to run {file_name}: {e}\n")
        return False


def run_all_files(files):
    """Runs all discovered files and prints a consolidated health check."""
    print("\n" + "=" * 70)
    print(f"  RUNNING ALL {len(files)} PYTHON FILES IN REPOSITORY")
    print("=" * 70)

    passed = 0
    failed = []

    for rel_path, full_path in files:
        file_dir = os.path.dirname(full_path)
        file_name = os.path.basename(full_path)
        env = os.environ.copy()
        existing_pp = env.get("PYTHONPATH", "")
        env["PYTHONPATH"] = (
            f"{file_dir};{REPO_ROOT};{existing_pp}"
            if sys.platform == "win32"
            else f"{file_dir}:{REPO_ROOT}:{existing_pp}"
        )

        res = subprocess.run(
            [sys.executable, file_name],
            cwd=file_dir,
            env=env,
            capture_output=True,
            text=True,
        )

        if res.returncode == 0:
            print(f"  [PASS] {rel_path}")
            passed += 1
        else:
            print(f"  [FAIL] {rel_path} -> {res.stderr.strip().splitlines()[-1] if res.stderr else 'Error'}")
            failed.append(rel_path)

    print("\n" + "=" * 70)
    print(f"  SUMMARY: {passed}/{len(files)} PASSED | {len(failed)} FAILED")
    print("=" * 70 + "\n")
    return len(failed) == 0


def group_files_by_chapter(files):
    """Groups files by their parent folder/chapter."""
    groups = {}
    for rel_path, full_path in files:
        parts = rel_path.split(os.sep)
        chapter = parts[0] if len(parts) > 1 else "Root"
        if chapter not in groups:
            groups[chapter] = []
        groups[chapter].append((rel_path, full_path))
    return groups


def interactive_menu(files):
    """Displays an easy terminal menu for the user."""
    groups = group_files_by_chapter(files)
    chapter_list = list(groups.keys())

    while True:
        print("\n" + "=" * 55)
        print("   PYTHON LEARNING JOURNEY - TERMINAL RUNNER")
        print("=" * 55)
        for idx, ch in enumerate(chapter_list, 1):
            print(f"  [{idx}] {ch} ({len(groups[ch])} files)")
        print("-" * 55)
        print("  [A] Run All Files (Health Check)")
        print("  [S] Search by name (e.g. 'practice', 'numpy', 'pattern')")
        print("  [Q] Exit")
        print("=" * 55)

        choice = input("Enter option or number: ").strip().lower()

        if choice in ("q", "exit", "quit"):
            print("Exiting runner. Happy coding!")
            break

        if choice in ("a", "all"):
            run_all_files(files)
            continue

        if choice in ("s", "search"):
            query = input("Enter search term: ").strip().lower()
            matches = [f for f in files if query in f[0].lower()]
            if not matches:
                print(f"No files matching '{query}' found.")
                continue
            if len(matches) == 1:
                run_single_file(matches[0][1])
            else:
                print(f"\nFound {len(matches)} matching files:")
                for i, (rel, full) in enumerate(matches, 1):
                    print(f"  [{i}] {rel}")
                sel = input(f"Choose [1-{len(matches)}] to run (or Enter to cancel): ").strip()
                if sel.isdigit() and 1 <= int(sel) <= len(matches):
                    run_single_file(matches[int(sel) - 1][1])
            continue

        if choice.isdigit() and 1 <= int(choice) <= len(chapter_list):
            selected_chapter = chapter_list[int(choice) - 1]
            ch_files = groups[selected_chapter]

            print(f"\nFiles in {selected_chapter}:")
            for i, (rel, full) in enumerate(ch_files, 1):
                print(f"  [{i}] {os.path.basename(rel)}")
            print(f"  [A] Run all files in this chapter")
            print(f"  [B] Back to main menu")

            sub_choice = input(f"Choose file [1-{len(ch_files)}]: ").strip().lower()
            if sub_choice == "b":
                continue
            elif sub_choice == "a":
                for _, full in ch_files:
                    run_single_file(full)
            elif sub_choice.isdigit() and 1 <= int(sub_choice) <= len(ch_files):
                run_single_file(ch_files[int(sub_choice) - 1][1])
            continue

        # If user directly typed a search word like "pattern" or "dsa"
        matches = [f for f in files if choice in f[0].lower()]
        if matches:
            if len(matches) == 1:
                run_single_file(matches[0][1])
            else:
                print(f"\nFound {len(matches)} files matching '{choice}':")
                for i, (rel, full) in enumerate(matches, 1):
                    print(f"  [{i}] {rel}")
                sel = input(f"Choose [1-{len(matches)}] to run: ").strip()
                if sel.isdigit() and 1 <= int(sel) <= len(matches):
                    run_single_file(matches[int(sel) - 1][1])
        else:
            print("Invalid selection. Please choose a valid number or option.")


def main():
    files = get_all_python_files()

    if len(sys.argv) > 1:
        arg = sys.argv[1].strip().lower()

        if arg in ("--all", "-a", "all"):
            run_all_files(files)
            return

        # Chapter filter (e.g. '4', 'ch4', '8')
        digits = "".join(c for c in arg if c.isdigit())
        if digits:
            matches = [f for f in files if f"chapter {digits}" in f[0].lower()]
            if matches:
                if len(sys.argv) > 2:
                    sub = sys.argv[2].lower()
                    sub_matches = [f for f in matches if sub in f[0].lower()]
                    if sub_matches:
                        run_single_file(sub_matches[0][1])
                        return
                print(f"\nFiles in Chapter {digits}:")
                for i, (rel, full) in enumerate(matches, 1):
                    print(f"  [{i}] {os.path.basename(rel)}")
                if len(matches) == 1:
                    run_single_file(matches[0][1])
                return

        # Search keyword match
        matches = [f for f in files if arg in f[0].lower()]
        if len(matches) == 1:
            run_single_file(matches[0][1])
            return
        elif len(matches) > 1:
            print(f"\nMultiple files match '{arg}':")
            for i, (rel, _) in enumerate(matches, 1):
                print(f"  [{i}] {rel}")
            print("\nTip: Be more specific or run without arguments for interactive menu.")
            return
        else:
            print(f"No files found matching '{arg}'.")
            return

    # If no CLI arguments provided, launch interactive menu
    if sys.stdin.isatty():
        interactive_menu(files)
    else:
        # Fallback if run non-interactively without args
        run_all_files(files)


if __name__ == "__main__":
    main()
