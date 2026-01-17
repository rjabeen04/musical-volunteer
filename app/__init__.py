import os
import logging
import redis
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY", "dev-only-secret-key")

    # -----------------------
    # Basic logging (optional)
    # -----------------------
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Musical Volunteer app")

    # -----------------------
    # Env-based Redis config
    # -----------------------
    app.config["REDIS_HOST"] = os.getenv("REDIS_HOST", "localhost")
    app.config["REDIS_PORT"] = int(os.getenv("REDIS_PORT", "6379"))

    # -----------------------
    # Basic print logging (stdout)
    # -----------------------
    print("Starting Flask app...")
    print(f"Redis Host: {app.config['REDIS_HOST']}")
    print(f"Redis Port: {app.config['REDIS_PORT']}")

    # -----------------------
    # Redis client (attached to app)
    # -----------------------
    app.redis_client = redis.Redis(
        host=app.config["REDIS_HOST"],
        port=app.config["REDIS_PORT"],
        decode_responses=True
    )

    # Optional: Redis connectivity check
    try:
        app.redis_client.ping()
        print("Redis connection successful")
    except Exception:
        print("Redis not reachable (app still starts)")

    # -----------------------
    # Request-level logging
    # -----------------------
    @app.before_request
    def log_request():
        print("Incoming request")

    # -----------------------
    # Register blueprints
    # -----------------------
    from .routes import main
    app.register_blueprint(main)

    return app

