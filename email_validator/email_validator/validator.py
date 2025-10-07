import re

class EmailValidator:
    def is_valid(self, email: str) -> bool:
        if not isinstance(email, str) or not email:
            return False

        if " " in email:
            return False

        if len(email) < 5 or len(email) > 254:
            return False

        if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email):
            return False

        if email.startswith((".", "-", "_", "@")) or email.endswith((".", "-", "_", "@")):
            return False

        return True
