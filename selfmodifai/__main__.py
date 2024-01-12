import logging
from selfmodifai.agents.fine_tunable_agents.team_agent.team_agent import team_agent


def main():
    # Set up logging configuration here
    logging.basicConfig(
        filename="autoautoml.log", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    team_agent()


if __name__ == "__main__":
    main()
