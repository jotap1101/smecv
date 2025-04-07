from django.contrib.auth.tokens import PasswordResetTokenGenerator

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    """
    Custom token generator for password reset and account activation.
    """
    def _make_hash_value(self, user, timestamp):
        return f'{user.pk}{timestamp}{user.is_active}'
    
account_activation_token = AccountActivationTokenGenerator()