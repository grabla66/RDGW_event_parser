# event log search for last 28 days RDP logins
# (c) Graham Blackwell / GDMA Technology
# May 2024
#
# Run this powershell script as a sheduled task, on the remote desktop gateway server,
# to extract the Operational events from the Microsoft-Windows-TerminalServices-Gateway/Operational event log
# and write them to a text file, using the time/date to generate the filename
# The text file can then be interrogated by the analysethelogs python script to export to CSV format.
#
# Hint: the TerminalServices-Gateway event log is set to 1MB by default, so increase the size to collect history over a longer period.

$timestamp = get-date -Format "yyyy-MM-dd_HH-mm-ss"
$filename = "C:\Logs\Log_last28days_$timestamp.txt"

#generate the output file
New-Item -Path $filename -ItemType "file"
#get yesterdays date
$startdate = (Get-Date).AddDays(-28).Date
$enddate   = (Get-Date).Date

#read the events from the event log and write to text file
get-winevent  @{LogName='Microsoft-Windows-TerminalServices-Gateway/Operational'; StartTime=$startdate; EndTime=$enddate;} |  Out-File -width 500 $filename  -Encoding ASCII



