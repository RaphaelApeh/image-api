import cloudinary

from decouple import config

CLOUDINARY_SECRET_KEY=config('CLOUDINARY_SECRET_KEY', cast=str)
CLOUDINARY_API_KEY=config('CLOUDINARY_API_KEY', cast=str)
CLOUDINARY_NAME=config('CLOUDINARY_NAME')


def cloudinary_init():
    cloudinary.config( 
        cloud_name = CLOUDINARY_NAME, 
        api_key = CLOUDINARY_API_KEY, 
        api_secret = CLOUDINARY_SECRET_KEY, # Click 'View API Keys' above to copy your API secret
        secure=True
    )

def convert_from_bytes(byte: float):
    kilobytes = byte / 1024
    return kilobytes