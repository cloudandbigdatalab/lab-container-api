import os
from draft import create, delete, run

create(os.environ['DO_KEY'])
run('docker/whalesay')
delete()
