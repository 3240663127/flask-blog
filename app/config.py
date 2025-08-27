class Config:
    SECRET_KEY = ""
class DevelopmentConfig(Config):#开发环境配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:197303@localhost:3306/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
class ProductionConfig(Config):#生产环境配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:197303@localhost:3306/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}



