import tempfile
import subprocess

def clone_repo(url):
    tmp = tempfile.mkdtemp()

    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", url, tmp],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return tmp
    except:
        return None
