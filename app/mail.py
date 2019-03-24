import getpass as gp
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os

def sendMail(email,ImgFileName):
    smtp_server = "smtp.gmail.com"
    port = 587 
    #Enter sender and reviever emails below
    sender = "codecell.engg@somaiya.edu"
    #Sender mail should have less secure apps enabled 
    reciever = email
    # recievers=["aditya.prajapati@somaiya.edu","karan.sheth@somaiya.edu","dhruvi.vadalia@somaiya.edu","rushang.g@somaiya.edu","akshay.padte@somaiya.edu"]
    # recievers=["hetal.kuvadia@somaiya.edu"]

    txt = MIMEMultipart("alternative")

    #Specify subject of mail, sender and reciever 
    txt["Subject"] = "Workshop registration ACK"
    txt["From"] = sender


    
    
    #Content of the mail to be sent
    str1 = '''<html>
            <body>
            
                <p>
                Hola! I see you've signed up for our workshop😃. The details for the workshop are as follows : 
                </p>
                <p>
                Hope you have filled the right details as the same will be used for the <b>certificates</b>.
                </p>
                <br>
                <b>Venue: </b> B-215, KJ Somaiya College Of Engineering, Vidyavihar.
                <br>
                <b>Timing: </b> 10:00 - 5:00
                <br>
                Here is your pass for the event <img src="cid:image1">
                <br>
                <b>You are supposed to deposit INR 50 </b>(refundable at the venue on the day of the event) either by Paytm (to 7045185177) or in cash to any of the council members in room B-111 by Friday, 22nd March, 2019,<b without which your registration will be deemed null and void.</b>
                <br>
            </body>
            </html>'''
    str1 = MIMEText(str1, "html")
    txt.attach(str1)
    
    # This example assumes the image is in the current directory
    fp = open(ImgFileName, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    txt.attach(msgImage)

    
    #Input password from user 
    password = 'kauxtcfedhruytxl'
    con = ssl.create_default_context()
    server = smtplib.SMTP(smtp_server, port)
    FROMADDR = "%s <%s>" % ('KJSCE CodeCell', sender)
    server.starttls()
    server.login(sender, password)
    # Spam people :P
    # for reciever in recievers:
    server.sendmail(FROMADDR, reciever, txt.as_string())

    print("Succesfully sent the mails!")

#sendMail('karan.sheth@somaiya.edu','passes/r.jpeg')