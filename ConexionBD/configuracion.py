from decouple import config

class Config:
    POSTGRES_HOST = config('POSTGRES_HOST')
    POSTGRES_USER = config('POSTGRES_USER')
    POSTGRES_DB = config('POSTGRES_DB')
    POSTGRES_PORT = config('POSTGRES_PORT')
    POSTGRES_PASSWORD = config('POSTGRES_PASSWORD')
    SECRET_KEY = config('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG = True

config = {'development': DevelopmentConfig}
