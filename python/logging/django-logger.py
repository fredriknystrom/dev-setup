# NOTE: Place this code in the settings file. 
# Define the path to LOGS_DIR above in the file

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
             'format': '[%(asctime)s] %(levelname)s [%(name)s:%(filename)s:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler', # Rotating log files to not overflow memory on server
            'filename': LOGS_DIR / 'acidapp.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB per log file
            'backupCount': 5, # Number of backups saved before rotating out old logs 
            'formatter': 'standard',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': { #  The default Django logger.
            'handlers': ['file', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'myapp': {  # myapp logger
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}