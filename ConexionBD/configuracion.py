import decouple

class Config:
    POSTGRES_HOST = decouple.config('POSTGRES_HOST')
    POSTGRES_USER = decouple.config('POSTGRES_USER')
    POSTGRES_DB = decouple.config('POSTGRES_DB')
    POSTGRES_PORT = decouple.config('POSTGRES_PORT')
    POSTGRES_PASSWORD = decouple.config('POSTGRES_PASSWORD')
    SECRET_KEY = decouple.config('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG = True

config = {'development': DevelopmentConfig}
