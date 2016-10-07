import os
import mimetypes
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email:
    """
    Usage Example:

    my_mail = Email()
    my_mail.sender = 'God'
    my_mail.to = ['Adam', 'Eve']
    my_mail.bcc = ['Snake']
    my_mail.subject = 'The Tree of Knowledge'
    my_mail.write('Of the tree of the knowledge of good and evil, thou shalt not eat of it:')
    my_mail.write('<b>for in the day that thou eatest thereof thou shalt surely die.</b>')
    my_mail.attach(r'C:\Bible\Genesis\')
    my_mail.attach(r'C:\Bible\disclaimer.txt')

    # pass to a mail-server for sending
    """

    def __init__(self):
        self.sender = ''
        self.to = []
        self.cc = []
        self.bcc = []
        self.subject = ''
        self.__content = []
        self.__attachments = []
        self.__body = MIMEMultipart()

    def __build(self):
        self.__body = MIMEMultipart()  # default as 'mixed'
        self.__body['From'] = self.sender
        self.__body['To'] = ", ".join(self.to)
        self.__body['Cc'] = ", ".join(self.cc)
        self.__body['Subject'] = self.subject

        for file_path in self.__attachments:
            # Guess the content type based on the file's extension.
            # Encoding will be ignored, although we should check for simple things like gzip'd or compressed files.
            ctype, encoding = mimetypes.guess_type(file_path)
            if ctype is None or encoding is not None:
                # No guess could be made, or the file is encoded (compressed)- use a generic bag-of-bits type.
                ctype = 'application/octet-stream'

            maintype, subtype = ctype.split('/', 1)

            if maintype == 'text':
                fp = open(file_path)
                # Note: we should handle calculating the charset
                attachment = MIMEText(fp.read(), _subtype=subtype)
                fp.close()
            elif maintype == 'image':
                fp = open(file_path, 'rb')
                attachment = MIMEImage(fp.read(), _subtype=subtype)
                fp.close()
            elif maintype == 'audio':
                fp = open(file_path, 'rb')
                attachment = MIMEAudio(fp.read(), _subtype=subtype)
                fp.close()
            else:
                fp = open(file_path, 'rb')
                attachment = MIMEBase(maintype, subtype)
                attachment.set_payload(fp.read())
                # Encode the payload using Base64
                encoders.encode_base64(attachment)
                fp.close()

            # Set the filename parameter
            attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path))
            self.__body.attach(attachment)

        self.__body.attach(MIMEText(self.__html_msg_wrapper(), 'html'))

    def attach(self, path):
        path = os.path.abspath(path)

        # file:
        if os.path.isfile(path):
            if path not in self.__attachments:
                self.__attachments.append(path)
                print 'successfully added attachment:\t %s' % path

        # directory:
        elif os.path.isdir(path):
            for directory, subdirectories, files in os.walk(path):
                for filename in files:
                    file_path = os.path.join(directory, filename)

                    # recursive call to attach file:
                    self.attach(file_path)

        # path does not exist:
        else:
            print 'FAILED adding attachment:\t\t %s \t (INVALID PATH)' % path

    def write(self, msg):
        self.__content.append(msg)

    def __html_msg_wrapper(self):
        html = """\
                <html>
                  <head></head>
                  <body>
               """

        for paragraph in self.__content:
            html = html + paragraph + '<br><br>'

        html += """\
                    </body>
                </html>
               """

        return html

    def get_recipients(self):
        return self.to + self.cc + self.bcc

    def get_msg(self):
        self.__build()
        return self.__body.as_string()

