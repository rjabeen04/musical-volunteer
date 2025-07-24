import redis
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Setup Redis client and attach to app
    app.redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

    # Import and register blueprint(s)
    from .routes import main
    app.register_blueprint(main)

    return app
