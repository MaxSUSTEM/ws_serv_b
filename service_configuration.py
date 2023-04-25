#!/usr/bin/env python3

import time
import tqdm

configuration_number = "5015"
version = "1.1.0"

print("Service package 2: ver. {}".format(version))
time.sleep(0.5)
print("Service package 2: start configuration ")
time.sleep(0.5)
print("Service package 2: stage 1")
time.sleep(0.5)
for i in tqdm.tqdm(range(7500), ascii=True, desc="Finding dependencies"):
    time.sleep(0.01)
print("Service package 2: stage 1 finished")
time.sleep(0.5)
print("Service package 2: stage 2")
time.sleep(1.5)
print("Service package 2: configuration package 1 found")
for i in tqdm.tqdm(range(10000), ascii=True, desc="Setup in progress"):
    time.sleep(0.001)
print("Service package 2: stage 2 finished")
time.sleep(0.5)
print("Service package 2: successfully configured!")
time.sleep(0.5)
print("Service package 2: configuration checksum : {}".format(configuration_number))
print("Service package 2: please push Ctrl+C to finish")
