import subprocess

output = str(subprocess.Popen(['ps -a | grep mjpg'], stdout=subprocess.PIPE, shell=True).communicate()[0],
             encoding='utf8')
print(output == '')
