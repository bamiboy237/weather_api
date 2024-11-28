import os
import secrets

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex(16)
    API_KEY = 'RVD4YVGCKQTA7DFNYM4FMSPD7'
    GEMINI_API_KEY = 'AIzaSyDcXQ_rr9kOlHOC91yJH_8OWEjLWgOXRV0'