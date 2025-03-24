#!/bin/bash
# --------------------------------------------------------------------------
# People Counter - Run Script
# --------------------------------------------------------------------------
# License:   
# Copyright 2025 Helena Wang
# 
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, this 
# list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice, 
# this list of conditions and the following disclaimer in the documentation 
# and/or other materials provided with the distribution.
# 
# 3. Neither the name of the copyright holder nor the names of its contributors 
# may be used to endorse or promote products derived from this software without 
# specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# --------------------------------------------------------------------------
# 
# Run People Counter
# 
# --------------------------------------------------------------------------

# Shell scripts eliminate the need to type a lot. 
# Changes our directory to where we want to run it: typically the main Python class 
cd /var/lib/cloud9/EDES301/python/people_counter

./configure_pins.sh

# List of directories of all non-system installed imports. 
# Separated by a colon
# Get through command "pwd": print working directory

# Better to use absolute / (start from the root of the file system) 
# rather than current ./ slash (start from the current file system)
dirs=(
    "/var/lib/cloud9/EDES301/python/ht16k33:"
    "/var/lib/cloud9/EDES301/python/button:"
)

# Shell Scripts allow us to run all this at once in the terminal shell, which is faster 
# if not in default directory, shell will not find it ./ means 

# Concatenating the "dirs" list into a string for python to run 
PYTHONPATH=$(IFS=; echo "${dirs[*]}") python3 people_counter.py