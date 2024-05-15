# !/usr/bin/python
#
# A python script to analyse the log files from the remote desktop gateway server
# (c) Graham Blackwell / GDMA Technology
# May 2024
#
# This Python script reads a text file created by the Powershell scripts running on the remote desktop gateway server (Windows Server 2016)
# and extracts the 302 and 303 events, writing their values to a csv file for manipulation with Excel or MySQL/PHP/CanvasJS
#
# The powershell script below reads the TerminalServices-Gateway/Operational log file and writes the contents to a text file defined as $filename
# This needs to run on the Windows remote desktop gateway server, every 24 hours, to produce the text file which is then processed by this python script
# <start>
# $timestamp = get-date -Format "yyyy-MM-dd_HH-mm-ss"
# $filename = "C:\Logs\Log_today_$timestamp.txt"
# New-Item -Path $filename -ItemType "file" -force
# get-winevent  @{LogName='Microsoft-Windows-TerminalServices-Gateway/Operational'; StartTime=[datetime]::Today} |  Out-File -width 500 $filename  -Encoding ASCII
# <end>
# The powershell script is scheduled to run every night at 23:59, and writes Todays events to a text file whose name is derived from Todays date
# 
# After the powershell script has run, run the python script, reads the text file created above, and extracts the 302 and 303
# events and writes to '.csv' file with the same filename, in the same folder as the text file

import os

def open_files():
    global ip, op, fname
    fname = "logs\Log_last28days_2024-05-15_08-44-01"
    ip = open(fname+".txt", "r") #open the text file for read
    print("Opened the Log input file for reading")
    op = open(fname+".csv", "w") #open the results.csv file for write
    print("Opened the result.csv output file for writing")
    op.write(fname+".txt"+chr(13)) #write the filename being read, to the fist line in the csv file
    op.write(chr(13)) # write a blank line to the csv file
    op.write("Date,Time,Id,User,ServerIP,Server,Transferred,Received,Session(secs)\n") # write the column names to the csv file

def close_files():
    ip.close() # close the input file
    print("Closed the input log file")
    op.close() # close the csv file
    print("Closed the result.csv file")

def split_string(status):
    words = line.split() #split on spaces
    if status == 303 :
        opstr = words[0]+","+words[1]+","+words[2]+","+words[6][1:-2]+","+words[10][1:-2]+","+words[17][1:-2]+","+words[25]+","+words[29]+","+words[36]+chr(13)
    if status == 302 :
        opstr = words[0]+","+words[1]+","+words[2]+","+words[6][1:-2]+","+words[10][1:-2]+","+words[14][1:-2]+chr(13)
    op.write(opstr) # write the opstr to the csv file

def process_files():
    global count, line
    count = 0
    print("Processing the input log file")
    while True:
        count += 1
        line = ip.readline().lower() #read a line from the input file
        if not line:
            break #eof so exit this loop
        if line.find("303 information") > 0 : # found a 303 information event
            split_string(303)
        if line.find("302 information") > 0 : # found a 302 information event
            split_string(302)

#main code
open_files()
process_files()
close_files()
print("Finished processing ",count,"lines")

      
