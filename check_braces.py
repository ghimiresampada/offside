import os
import re

def check_latex_braces():
    found_issue = False
    # Scans all .tex files in the current directory and subdirectories
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".tex"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    for i, line in enumerate(f, 1):
                        # Ignore comments
                        clean_line = re.sub(r'%.*', '', line)
                        open_b = clean_line.count('{')
                        close_b = clean_line.count('}')
                        
                        if close_b > open_b:
                            print(f"❌ Issue in {filepath} at Line {i}:")
                            print(f"   {line.strip()}")
                            print(f"   (Found {open_b} '{{' and {close_b} '}}')\n")
                            found_issue = True
    
    if not found_issue:
        print("✅ No simple mismatched braces found in .tex files.")

if __name__ == "__main__":
    check_latex_braces()