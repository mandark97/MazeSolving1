import sys
import pygame
from pygame.locals import *

DAY9YELLOW = (255, 167, 26)

GOAL = (245, 163, 183)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLUE = (50, 50, 255)
FILL = (255, 77, 77)

class Wall(pygame.sprite.Sprite):
    """ Wall the robot can run into. """

    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the robot can run into. """
        super().__init__()

        # Make a black wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Space(pygame.sprite.Sprite):
    """ Wall the robot can run into. """

    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the robot can run into. """
        super().__init__()

        # Make a transparent wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Goal(pygame.sprite.Sprite):
    """ Wall the robot can run into. """

    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the robot can run into. """
        # Call the parent's constructor
        super().__init__()

        # Make the goal, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(GOAL)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class VisitedLocation(pygame.sprite.Sprite):
    """ Visited location """

    def __init__(self, x, y, width, height):
        super().__init__()

        # Make the goal, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(FILL)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
