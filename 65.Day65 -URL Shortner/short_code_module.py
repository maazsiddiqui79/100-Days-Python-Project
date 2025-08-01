import random

class SHORT_CODE():

    @staticmethod
    def password_gen():
        characters = [
            # Letters
            'A','B','C','D','E','F','G','H','I','J','K','L','M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
            'a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z',

            # Digits
            '0','1','2','3','4','5','6','7','8','9',

            # Symbols and punctuation
        ]

        weights = [5 if i.isalpha() else (3 if i.isnumeric() else 1) for i in characters]
        password_list = random.choices(characters, k=8, weights=weights)
        actual_password = "".join(password_list)
        return actual_password

# Usage
a = SHORT_CODE()
print(a.password_gen())
