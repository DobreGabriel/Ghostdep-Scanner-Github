import os
import requests

def comment(repo, pr, message):
    token = os.getenv("GITHUB_TOKEN")

    url = f"https://api.github.com/repos/{repo}/issues/{pr}/comments"

    requests.post(
        url,
        headers={"Authorization": f"token {token}"},
        json={"body": message}
    )

if __name__ == "__main__":
    # esempio statico
    comment("owner/repo", 1, "⚠️ Security scan completed")
