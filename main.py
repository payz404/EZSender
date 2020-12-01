################################
####                        ####
####    Author : Im.Payz    ####
####    Name   : EZSender   ####
####    Version: 1.0        ####
####                        ####
################################


from EZModule import *

class EZSender:


   def __init__(self, email, subject, from_email, from_name, letter, randlink, settings, delay):
      
      os.system("clear")
      
      
      print("""[yellow]

  ┈┈╱▔▔▔▔▔▔▔▔▔▔▔▏ 
  ┈╱╭▏╮╭┻┻╮╭┻┻╮╭▏ 
  ▕╮╰▏╯┃╭╮┃┃╭╮┃╰▏ 
  ▕╯┈▏┈┗┻┻┛┗┻┻┻╮▏ 
  ▕╭╮▏╮┈┈┈┈┏━━━╯▏
  ▕╰╯▏╯╰┳┳┳┳┳┳╯╭▏ 
  ▕┈╭▏╭╮┃┗┛┗┛┃┈╰▏ [/yellow][red]EZSender [/red]v.1.0[yellow]  
  ▕┈╰▏╰╯╰━━━━╯┈┈▏      

[/yellow]""")
      
      
      
      
      
      
      self.host = settings['smtpHost']
      self.port = settings['smtpPort']
      self.user = settings['smtpUser']
      self.pwd = settings['smtpPass']
           
      
      self.date = datetime.date.today()
      self.mailist = open("EZConfig/Mailist/"+email).readlines()
      self.subject = subject
      self.fromEmail = from_email
      self.fromName = from_name
      self.letter = letter
      self.randlink = randlink
      self.delay = delay
   
   
      
   
   def getMailist(self):
   
      for lists in self.mailist:        
         return lists
      
   
   
   def getUsername(self):
      
      username = self.getMailist().split("@")
      return username[0]

   
         
   
   def fiture(self,data):
   
      #setlength = length
      data = data.replace("{email}", self.getMailist())
      data = data.replace("{user}",self.getUsername())
      data = data.replace("{date}",self.date.strftime('%B %d, %Y'))
      data = data.replace("{date2}",self.date.strftime('%m/%d/%Y'))
      data = data.replace("{ip}", self.randIp())
      data = data.replace("{device}",self.device())
      data = data.replace("{browser}",self.browser())
      data = data.replace("{country}",self.negara())
      data = data.replace("{randstring}", self.randomString(8))
      data = data.replace("{randnumber}",str(self.randomNumber(8)))
      data = data.replace("{random}",self.randoms())
      data = data.replace("{random_link}", self.randomLink())
         
      return data
   


   def randIp(self):
      
      ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
      return ip
       
   
   
   def randomString(self,length):
      
      letters = string.ascii_lowercase
      result_str = ''.join(random.choice(letters) for i in range(length))      
      return result_str
      

   def randomNumber(self,num):
      range_start = 10**(num-1)
      range_end = (10**num)-1
      return randint(range_start, range_end)
      
      
   def randoms(self):
       
      N = 7       
      res = ''.join(random.choices(string.ascii_lowercase+string.digits, k = N))
      return str(res)
   
   
   def randomLink(self):
      
      link = self.randlink
        	
      return random.choice(link)
      
      
   def browser(self):
      
      browser = ['Mozilla Firefox' , 'Chrome' , 'Safari']
      return random.choice(browser)   
    
    
      
   def device(self):
      
      device = ['iPhone 6S Plus','iPhone 6S','iPhone SE','iPad Pro 9.7','iPhone 7 Plus', 'iPhone 7','IPad Pro','IPhone 8','IPhone 8+','IPhone 7+','Iphone X']	
      return random.choice(device)   
   
   
   def negara(self):
       
       negara = ["Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegowina", "Botswana", "Bouvet Island", "Brazil", "British Indian Ocean Territory", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros", "Congo", "Congo, the Democratic Republic of the", "Cook Islands", "Costa Rica", "Cote d'Ivoire", "Croatia (Hrvatska)", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands (Malvinas)", "Faroe Islands", "Fiji", "Finland", "France", "France Metropolitan", "French Guiana", "French Polynesia", "French Southern Territories", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Heard and Mc Donald Islands", "Holy See (Vatican City State)", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran (Islamic Republic of)", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, Democratic People's Republic of", "Korea, Republic of", "Kuwait", "Kyrgyzstan", "Lao, People's Democratic Republic", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libyan Arab Jamahiriya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia, The Former Yugoslav Republic of", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia, Federated States of", "Moldova, Republic of", "Monaco", "Mongolia", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "Netherlands Antilles", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", "Norfolk Island", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russian Federation", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Seychelles", "Sierra Leone", "Singapore", "Slovakia (Slovak Republic)", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Georgia and the South Sandwich Islands", "Spain", "Sri Lanka", "St. Helena", "St. Pierre and Miquelon", "Sudan", "Suriname", "Svalbard and Jan Mayen Islands", "Swaziland", "Sweden", "Switzerland", "Syrian Arab Republic", "Taiwan, Province of China", "Tajikistan", "Tanzania, United Republic of", "Thailand", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "United States Minor Outlying Islands", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Virgin Islands (British)", "Virgin Islands (U.S.)", "Wallis and Futuna Islands", "Western Sahara", "Yemen", "Yugoslavia", "Zambia", "Zimbabwe"]
       
       return random.choice(negara)
     

   
   
   
   def EZSend(self):
      
      
      console = Console()
      counts = len(self.mailist)
      i = 0
      for email in self.mailist:
         
        # email.replace("\n\n","")
         try:
            letters = codecs.open("EZConfig/Letter/"+self.letter).read()
         
            letter = self.fiture(letters)
            emails = self.fiture(email)
            subject = self.fiture(self.subject)
            fromEmail = self.fiture(self.fromEmail)
        
         
            msg = MIMEMultipart()
            msg.set_charset("UTF-8")
            msg['Subject'] = self.subject
            msg['From'] = formataddr((str(Header(self.fromName, 'utf-8')), ''+fromEmail))
            msg['To'] = emails

            msg.attach(MIMEText(letter, "html"))
         
         
            server = smtplib.SMTP(self.host, self.port)
            server.starttls()
            server.ehlo()
            server.login(self.user, self.pwd)
            toString = msg.as_string()
            server.sendmail(msg['From'], msg['to'], toString)
            server.quit()
            
            sub = self.subject.split(" ")
            
            subjct = "[ "+sub[0]+" "+sub[1]+"... ]"
            
            
            i += 1
            send = "[red][ {} ][ {}/{} ] [/red][cyan]{}[/cyan] [yellow]{}[/yellow][bold] => [/bold][green][ Sent ][/green]".format(self.date.today().strftime('%m:%d:%Y'), i, counts, subjct, email)
            console.print(send.replace("\n", ""))
            time.sleep(self.delay)
            
            
            
         
         except:
            send = "[red][ {} ][ {}/{} ] [/red][cyan]{}[/cyan] [yellow]{}[/yellow][bold] => [/bold][red][ Not Sent ][/red]".format(self.date.today().strftime('%m:%d:%Y'), i, counts, subjct, email)
            console.print(send.replace("\n", ""))
            time.sleep(self.delay)
      
   
      
      
   
   
   
      




 
      








