import os
import subprocess
import signal
import time
import sys

proc = subprocess.Popen(['ping','192.168.1.100'], close_fds=True, preexec_fn=os.setsid,)

print 'PARENT      : Pausing before sending signal to child %s...' % proc.pid
sys.stdout.flush()
time.sleep(1)
print 'PARENT      : Signaling process group %s' % proc.pid
sys.stdout.flush()
os.killpg(proc.pid, signal.SIGUSR1)
time.sleep(3)