class SessionState:
    def __init__(self, **kwargs):
        self.username = kwargs.get('username', "")
        self.user_logged_in = kwargs.get('user_logged_in', False)