"""Main entry point for the Stock-Quant-Risk module.

This script initializes the risk analysis service,
sets up logging, and starts consuming messages from the configured
message queue.
"""

import os
import sys

# Add 'src/' to Python's module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.logger import setup_logger
from app.queue_handler import consume_messages

# Initialize logger
logger = setup_logger(__name__)


def main() -> None:
    """Starts the Quantitative Risk Analysis Service.

    This service listens to messages from a queue (RabbitMQ or SQS),
    applies risk scoring or risk assessment algorithms,
    and publishes the results.
    """
    logger.info("Starting Quantitative Risk Analysis Service...")
    consume_messages()


if __name__ == "__main__":
    main()
