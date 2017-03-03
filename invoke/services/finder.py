from invoke.base import ServiceInvoke


class FinderInvoke(ServiceInvoke):
    _prefix = "F_FINDER_"

    def ls(self):
        return self.send_request('GET', '/ls')

    def check(self):
        return self.send_request('GET', 'check')

    def register(self, **data):
        return self.send_request('POST', '/register', json=data)

    def get(self, field):
        return self.send_request('GET', '/get/{}'.format(field))

    def remove(self, field):
        return self.send_request('DELETE', '/remove/{}'.format(field))
