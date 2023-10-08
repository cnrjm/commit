import os
from github import Github
from decouple import config

# Load environment variables from .env
GITHUB_USERNAME = config('USER')
GITHUB_REPO = config('REPO')
GITHUB_TOKEN = config('TOKEN')

# Create a GitHub instance
g = Github(GITHUB_TOKEN)

# Get the repository
repo = g.get_user(GITHUB_USERNAME).get_repo(GITHUB_REPO)

# Define the commit message
commit_message = f"Auto commit"

# Path to the file you want to commit
file_path = "commit.py"

# Read the content of the file
with open(file_path, "r") as file:
    file_content = file.read()

existing_functions = [line for line in file_content.splitlines() if line.strip().startswith("def new_function")]
next_function_number = len(existing_functions) + 1
new_function_name = f"new_function{next_function_number}"

new_function = f"""
def {new_function_name}():
    print("1");
"""

# Append the new function to the file content
file_content += new_function

# Commit changes
repo.update_file(file_path, commit_message, file_content, repo.get_contents(file_path).sha, branch="main")