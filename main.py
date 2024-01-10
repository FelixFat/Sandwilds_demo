import sys

from code.game import Game


def main():
    game = Game()
    game.start()
    game.run()
    game.close()

    sys.exit(0)


if __name__ == '__main__':
    main()
