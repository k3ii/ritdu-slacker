from fly_cli import FlyCLI
from ritdu_slacker.api import SlackClient


def main():
    fly = FlyCLI()
    fly(SlackClient())


if __name__ == "__main__":
    main()
