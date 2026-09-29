#!/usr/bin/env python3

# File: blink_USR3.py
# Author: Zeyi Lyu
# Date: September 28, 2026
# Description: Blink the PocketBeagle USR3 LED at 5 Hz.
# Copyright (c) 2026 Zeyi Lyu
# SPDX-License-Identifier: MIT

import time
import Adafruit_BBIO.GPIO as GPIO

LED = "USR3"
HALF_PERIOD = 0.1

GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(HALF_PERIOD)

        GPIO.output(LED, GPIO.LOW)
        time.sleep(HALF_PERIOD)

except KeyboardInterrupt:
    pass

finally:
    GPIO.output(LED, GPIO.LOW)
    GPIO.cleanup()