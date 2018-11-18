import pygame
from game_sprite import *


class PlaneGame(object):

    def __init__(self):
        print("--Init Game--")
        # create game window
        self.__create_game()

    def __create_game(self):
        """create game"""
        # create game window
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # create game clock
        self.clock = pygame.time.Clock()

    def __event_listen(self):
        """event listen"""
        for e in pygame.event.get():
            # click exit
            if e.type == pygame.QUIT:
                PlaneGame.over_game()


    def __create_sprite(self):
        """create sprite"""
        backgroung_image = BackGround(BACKGROUND_IMAGE)
        self.back_group = pygame.sprite.Group(backgroung_image)

    def __check_hint(self):
        """check hint"""
        pass

    def __update_sprite(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

    @staticmethod
    def over_game():
        pygame.quit()
        exit()


    def start_game(self):
        print("--Start Game--")
        # start game
        while True:
            # set refresh picture frame rate
            self.clock.tick(FRAME_RATE)
            # event listen
            self.__event_listen()
            # hint listen
            self.__check_hint()
            # refresh sprite
            self.__create_sprite()
            # update sprite
            self.__update_sprite()
            # update show
            pygame.display.update()
            pass


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
