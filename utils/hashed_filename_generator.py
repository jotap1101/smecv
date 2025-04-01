from django.utils.timezone import now
from hashlib import sha256
import os

def generate_hashed_filename(instance, folder, filename):
    ext = os.path.splitext(filename)[1]
    hashed_filename = sha256(f'{filename}{now().timestamp()}'.encode('utf-8')).hexdigest()

    return os.path.join(folder, f'{hashed_filename}{ext}')