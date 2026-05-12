from config import ADMIN_EMAIL, ADMIN_PASSWORD

VALID_DATA = [
    {
        "email": ADMIN_EMAIL,
        "password": ADMIN_PASSWORD
    }
]

INVALID_DATA = [
    {
        "email": "randomemail@gmail.com",
        "password":"test123@"
    },
    {
        "email": "",
        "password":"test123@"
    },
    {
        "email": "randomemail@gmail.com",
        "password":""
    },
    {
        "email": "",
        "password":""
    }
]