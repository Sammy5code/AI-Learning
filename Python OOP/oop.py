# Abstraction


class EmailService:

    def _connect(self):
        print("Connecting to email server")

    def _authenticate(self, username, password):
        print("Aunthenticating")

    def send_email(self):
        self._connect()
        self._authenticate()
        print("Sending Email....")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from email server...")

email = EmailService()
email.send_email()