from invoke.base import ServiceInvoke


class EmailInvoke(ServiceInvoke):
    _prefix = "F_EMAIL_"

    def get_index(self):
        return self.send_request('GET', "/")

    def get_hello(self):
        return self.send_request('GET', '/get')
