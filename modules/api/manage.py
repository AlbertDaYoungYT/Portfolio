import modules.core.auth as Auth

def __init__(self, data):
    self.data = data
    self.urls = {
        "/auth": ["Authenticate", Auth.URL]
    }