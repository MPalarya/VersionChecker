from Email import Email
from MailServer import MailServer

const_server_name = 'mxhfa.esl.corp.elbit.co.il'
const_server_port = 587
const_email_username = 'tc34549'
const_email_password = 'Elbit-2'
const_email_address = 'michael.palarya@elbitsystems.com'

my_mail = Email()
my_mail.sender = 'God'
my_mail.to = ['michael.palarya@elbitsystems.com']
my_mail.subject = 'The Tree of Knowledge'
my_mail.write('Of the tree of the knowledge of good and evil, thou shalt not eat of it:')
my_mail.write('<b>for in the day that thou eatest thereof thou shalt surely die.</b><br>\
       Here is the <a href="http://www.python.org">link</a> you wanted.')
my_mail.attach(r'Attachments')
my_mail.attach(r'C:\Bible\disclaimer.txt')

my_mail_server = MailServer(
    server_name=const_server_name,
    server_port=const_server_port,
    email_username=const_email_username,
    email_password=const_email_password,
    email_address=const_email_address,
)
my_mail_server.send(my_mail)
