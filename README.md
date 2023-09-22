# BUGG firmware custom

This repository contains a copy of the [open source BUGG firmware](https://github.com/bugg-resources/bugg-cm4-firmware) that we modified so that we can test how to send data from a BUGG device to our own Google Cloud bucket.

## Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade google-cloud-storage
```

## Add an `__init__.py` to `bugg_cm4_firmware`

Add an `__init__.py` to `bugg_cm4_firmware` so that the folder is understood as a module by python.

In the `__init__.py` file write:

```
from .python_record import gcs_server_sync
```

So that the function is available when the user import the module.

## Change the `config.json` file

- Create the service account
- Create key from the service account
- From the service account copy / paste line 1 to 12 in the config file

## Slightly modify the `gcs_server_sync`

We used the function `gcs_server_sync` from `python_record.py`

- Comment (so it's not taken into account) the libraries `sensors`, `pcf8574`, `utils`, `httplib`. Some of these libraries handles real raspi hardware, such as leds and scripts using them can't run on computers.
- In the function `gcs_server_sync` some modifications also need to be done:
    - L.243 set `GLOB_is_connected = True`
    - L. 245, L.257, L.304  comment `disable_modem()` / `enable_modem()`
    - L. 249, L.263, L.309 comment `time.sleep(wait_t)`, `update_time()`, `time.sleep(max(0, sync_wait))`
    - L. 268, L.297 comment `set_led(led_driver, DATA_LED_CHS, DATA_LED_UPLOADING)`, `set_led(led_driver, DATA_LED_CHS, DATA_LED_CONN)`
    - L.252, set `while True:` 

## Run the `script.py`

We wrote a small wrapper around `gcs_server_sync`. To run it follow the steps described below:

- We first create a folder `./upload` containing the data to be sent on the Google Cloud bucket
- We move the `config.json` file in the same directory as `script.py`
- Run the script:

```
python script.py
```

If everything runs correctly the files contained in the `./upload` folder should disappear as they are sent to the Google Cloud bucket described in the `config.json` file