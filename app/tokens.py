from rest_framework_simplejwt.tokens import RefreshToken

class CustomAccessToken(RefreshToken):
    @property
    def role(self):
        return self.payload.get('role')