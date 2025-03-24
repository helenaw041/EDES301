#!/bin/bash
# --------------------------------------------------------------------------
# <Project Name> Pin Configuration
# --------------------------------------------------------------------------
# Copyright 2025 Helena Wang
#
# ... License ...
#
# --------------------------------------------------------------------------
# Configure pins for <Project Name>

# We add these pins to a configure pins shell script, so they run automatically. 

# I2C1
config-pin P2_09 i2c
config-pin P2_11 i2c

# Button
config-pin P2_02 gpio