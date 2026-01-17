import os
import logging
import redis
from flask import Flask


def create_app():
    app = Flask(__name__)

    # -----------------------
    # Basic logging
    # -----------------------
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Musical Volunteer app")

    # -----------------------
    # Env-based Redis config
    # -----------------------
    app.config["REDIS_HOST"] = os.getenv("REDIS_HOST", "localhost")
    app.config["REDIS_PORT"] = int(os.getenv("REDIS_PORT", "6379"))

    logging.info(
        f"Redis config host={app.config['REDIS_HOST']} "
        f"port={app.config['REDIS_PORT']}"
    )

    # -----------------------
    # Redis client (attached to app)
    # -----------------------
    app.redis_client = redis.Redis(
        host=app.config["REDIS_HOST"],
        port=app.config["REDIS_PORT"],
        decode_responses=True
    )

    try:
        app.redis_client.ping()
        logging.info("Redis connection successful")
    except Exception:
        logging.warning("Redis not reachable (app still starts)", exc_info=True)

    # -----------------------
    # Register blueprints
    # -----------------------
    from .routes import main
    app.register_blueprint(main)

    return app

