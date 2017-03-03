from invoke.base import ServiceInvoke


class PhoneInvoke(ServiceInvoke):
    _prefix = 'F_PHONE_'

    def get_index(self):
        return self.send_request("GET", '/')
