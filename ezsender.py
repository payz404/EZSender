from main import *


mailist = "" # Set Mailist File

subject = "" # Set Subject

from_name = "" # Set From Name Sender

from_email = "" # Set From Email Sender

letter = "" # Set HTML Letter File

random_link = ["http://short.link/1","http://short.link/2","http://short.link/3"] # Set Random Link (if you want use)

setDelay = 0 # Set Delay/Send

ezsettings = {

 "smtpHost":"", # your server/host smtp
 "smtpPort":, # your port smtp (ex:587)
 "smtpUser":"", # your smtp Username
 "smtpPass":"", # your smtp Password

}


app = EZSender(mailist, subject, from_email, from_name, letter, random_link, ezsettings, setDelay)
app.EZSend()


