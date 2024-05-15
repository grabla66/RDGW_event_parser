Do you want to analyse the event logs on your remote desktop gateway server?

This pair of scripts will allow you to search for Event ID 302 and 303 from the Microsoft-Windows-TerminalServices-Gateway/Operational
event log on your Gateway server, export only those events to a text file, and then use the Python script to analyse the text file and
produce a CSV file which contains the Date,Time,Id,User,ServerIP,Server,Transferred,Received,Session(secs) for the 302/303 events.

The ps1 Powershell script needs to be either run manually, or scheduled to run on a daily basis, on the remote desktop gateway server.
The file that is created by the Powershell script, has a unique filename that is automatically generated by using the date and time
when the script was run.

Edit the python script to point to the filename that was generated, and then run it. It will open the texxt file, process it, and 
create a csv file with the same filename.

The csv file can then be opened in Excel for sorting etc, or imported to mySQL for manipulation with PHP

