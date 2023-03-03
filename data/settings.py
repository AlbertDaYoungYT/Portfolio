import logging



LOG_ROTATION_SIZE  = "10 MB"
LOG_RETENTION_TIME = "1 week"
FLASK_LOG_LEVEL = logging.INFO
DISABLE_FLASK_LOG = False
try:
    SECRET = open(".flask", "r").read()
    STRIPE = open(".stripe", "r").read()
except Exception:
    import uuid
    open(".flask", "w").write(str(uuid.uuid1()))
    open(".stripe", "x")
finally:
    SECRET = open(".flask", "r").read()
    STRIPE = open(".stripe", "r").read()


PROJECT_NAME = "NAME"
COMPANY_NAME = "Company Inc" 