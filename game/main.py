#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import curses
import os
from collections import Iterable
from random import shuffle

import game.deck
from . import deck
from . import cards
from . import colors


class Game:
    def __init__(self, id, players=None, shuffle_players=True):
        """
        WIP

        Args:
            id: unique integer of game name
            players:
            shuffle_players:
        """

        if isinstance(players, Iterable):
            pass
        elif isinstance(players, int):
            pass

        self.trader_deck = deck.TradeDeck()

        # todo: gold and silver coins for 0th and 1st element of scoring_area
        self.score_deck = game.deck.SCORE_DECK
        shuffle(self.score_deck)
        self.scoring_area = [self.score_deck.pop() for _ in range(5)]

    def loop(self):
        """
        Main loop
        """
        self.render()
        while True:
            i = self.get_input()
            self.render()

    def render(self):
        os.system('clear')
        print(self.scoring_area)
        print(self.trader_market)

    def get_input(self):
        return input('Enter your command: ')


class CursesGame(Game):
    WINDOW_HEIGHT = 51
    WINDOW_WIDTH = 251

    TRADER_MARKET_X = 1
    TRADER_MARKET_Y = 1
    SCORING_AREA_X = 1
    SCORING_AREA_Y = 1

    def __init__(self, id, players=None, shuffle_players=True):
        super().__init__(id, players, shuffle_players)
        # Instantiate players
        # Give players their starting hands (Acquire(YY), Convert(2))
        # Assign one to go first
        # Distribute starting resources
        # Instantiate action_deck and action_market
        # Instantiate scoring_area and coin piles

        # Initialize curses
        stdscr = curses.initscr()
        stdscr.keypad(1)
        self.win = curses.newwin(self.WINDOW_HEIGHT, self.WINDOW_WIDTH, 0, 0)

        # curses.noecho()
        curses.cbreak()
        curses.start_color()

        # Clear screen
        self.win.clear()

        # Initialize colors corresponding to spice colors
        for color, pair in colors.COLOR_PAIR_DICT.iteritems()
            curses.init_pair(pair, color, colors.BACKGROUND_COLOR)

    def __del__(self):
        self.win.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()

    def initialize_players(self):
        pass

    def get_input(self):
        self.win.move(self.WINDOW_HEIGHT - 1, 0)
        ret = self.win.getstr()
        self.win.deleteln()
        return ret

    def render_market(self):
        """Render the central "Marketplace" area (i.e. the draftable face-up cards)"""
        for i_trade, trade_card in enumerate(self.trader_market):
            self.win.addstr()

    def render(self):
        self.win.clear()
        self.win.border()
        self.win.addstr(1, 1, "\u25a3", curses.color_pair(1))
        self.win.addstr(1, 2, "\u25a3", curses.color_pair(2))
        self.win.addstr(1, 3, "\u25a3", curses.color_pair(3))
        self.win.addstr(1, 4, "\u25a3", curses.color_pair(4))
        self.win.refresh()


if __name__ == "__main__":
    game = CursesGame(0)
    game.loop()
