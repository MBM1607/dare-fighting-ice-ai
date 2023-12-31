import argparse
import logging

from pyftg.gateway import Gateway

from BAISIK import BAISIK
from Randman import Randman


def start_game(port: int):
    gateway = Gateway(port=port)
    character = "ZEN"
    game_num = 1
    agent1 = BAISIK()
    agent2 = Randman()
    gateway.register_ai("BAISIK", agent1)
    gateway.register_ai("Randman", agent2)
    gateway.run_game([character, character], ["BAISIK", "Randman"], game_num)
    gateway.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--log",
        default="INFO",
        type=str,
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    )
    parser.add_argument(
        "--port", default=50051, type=int, help="Port used by DareFightingICE"
    )
    args = parser.parse_args()
    logging.basicConfig(level=args.log)
    start_game(args.port)
