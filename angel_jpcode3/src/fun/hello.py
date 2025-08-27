import logging

logger = logging.getLogger()

def say_hello(name: str) -> str:
    """Return greeting and log it."""
    message = f"Hello, {name}!"
    logger.info(f"Generated greeting for {name}")
    return message