import random, string

def generate_random_token(string_length):
    # Generate a token
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(string_length))