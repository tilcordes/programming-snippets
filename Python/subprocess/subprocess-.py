import subprocess

processs = subprocess.Popen('ipconfig', stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
stdout, stderr = processs.communicate()
print(stdout.decode())