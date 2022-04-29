import os
import time 


# cmd = 'mgeneratejs tracking.json -n 5 | mongoimport --uri mongodb+srv://mycluster-ABCDE.azure.mongodb.net/ \
#    --username=MYUSERNAME \
#    --password=SECRETPASSWORD --collection=mycollectionname'
cmd = 'ls -l'

while True: 
    os.system(cmd)
    print("Telemetry data sent")
    time.sleep(1)


