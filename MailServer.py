import smtplib


class MailServer:
    """
    Usage Example:

    my_mail_server = MailServer(
        server_name='mxhfa.esl.corp.elbit.co.il'
        server_port=587,
        email_username='tc34549',
        email_password='Elbit-2',
        email_address='michael.palarya@elbitsystems.com',
    )
    my_mail_server.send(my_mail)
    """

    def __init__(self, server_name, server_port, email_username, email_password, email_address):
        self.__mail_server = smtplib.SMTP(
            host=server_name,
            port=server_port,
        )
        self.__email_username = email_username
        self.__email_password = email_password
        self.__email_address = email_address
        self.__server_name = server_name
        self.__server_port = server_port

    def __connect(self):
        print 'connecting to mail server...'
        # identify ourselves to smtp gmail client
        self.__mail_server.ehlo()
        # secure our email with tls encryption
        self.__mail_server.starttls()
        # re-identify ourselves as an encrypted connection
        self.__mail_server.ehlo()

    def __login(self):
        print 'logging in...'
        self.__mail_server.login(
            user=self.__email_username,
            password=self.__email_password,
        )

    def send(self, email):
        print '-'
        self.__connect()
        self.__login()

        print 'sending email...'
        self.__mail_server.sendmail(
            from_addr=self.__email_address,
            to_addrs=email.get_recipients(),
            msg=email.get_msg(),
            )
        print 'mail sent!'
        print '-'
        self.__mail_server.quit()

