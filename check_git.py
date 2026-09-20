import subprocess
try:
    result = subprocess.run(['git', 'status'], cwd='/var/home/glenn/Projects/newman-server/newman-pack', capture_output=True, text=True)
    with open('/var/home/glenn/Projects/newman-server/newman-pack/git_status.txt', 'w') as f:
        f.write(result.stdout + "\n" + result.stderr)
except Exception as e:
    with open('/var/home/glenn/Projects/newman-server/newman-pack/git_status.txt', 'w') as f:
        f.write(str(e))
