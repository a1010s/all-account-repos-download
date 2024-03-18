# pip install PyGitHub

from github import Github
import os

# Replace 'username' and 'password' with your GitHub credentials
# or you can use a personal access token instead of a password
github_username = 'username'
github_password = '<token-or-password>'

# Initialize GitHub instance
g = Github(github_username, github_password)

# Replace 'your-organization' with the GitHub account or organization name
org_or_user = 'account-to-be-cloned'

# Directory where you want to clone the repositories
clone_dir = 'repos'

# Create directory if it doesn't exist
if not os.path.exists(clone_dir):
    os.makedirs(clone_dir)

# Get all repositories for the given user or organization
repos = g.get_user(org_or_user).get_repos()

# Clone each repository
for repo in repos:
    repo_url = repo.clone_url
    repo_name = repo.name
    clone_path = os.path.join(clone_dir, repo_name)
    
    # Clone the repository
    os.system(f'git clone {repo_url} {clone_path}')

print("All repositories cloned successfully.")
