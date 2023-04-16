#!/usr/bin/env python3
import os

change_path = r'C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2302.7-0'
os.chdir(change_path)

os.system('MpCmdRun -Scan -ScanType 0') # 0 or 1 for short scan, 2 for long scan
