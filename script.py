import threading
from bugg_cm4_firmware import gcs_server_sync

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

sync_interval= 10000
upload_dir= "./upload"
die= threading.Event()
config_path="./config.json" 
led_driver=None 
data_led_update_int= None

gcs_server_sync(sync_interval, upload_dir, die, config_path, led_driver, data_led_update_int)
