# GitHub Repository Cloner

This Python script allows you to clone all repositories from a GitHub account or organization with ease. It uses the GitHub API provided by the PyGitHub library to fetch repository information and clone each repository locally.

## Prerequisites

- Python 3.x installed on your system
- PyGitHub library installed (`pip install PyGitHub`)

## Usage

1. Clone or download this repository to your local machine.

```bash
   git clone https://github.com/your-username/github-repo-cloner.git
```
2. Navigate to the cloned repository directory.
```bash
    cd github-repo-cloner
```
3. Update the clone-git-account.py script with your GitHub credentials and the GitHub account or organization name you want to clone repositories from.
```bash
github_username = 'your-github-username'
github_password = 'your-github-password'
org_or_user = 'github-account-or-organization-name'
```
4. Run the script.
```bash
python3 clone-git-account.py
```
This will clone all repositories from the specified GitHub account or organization into a directory named repos in the current directory.


## Notes
Make sure to replace 'your-github-username', 'your-github-password', and 'github-account-or-organization-name' with your actual GitHub credentials and the account or organization name you want to clone repositories from.

If you have 2-factor authentication enabled on your GitHub account, use a personal access token instead of a password. You can generate a personal access token in your GitHub account settings.
Ensure that you have the necessary permissions to access the repositories you want to clone.
