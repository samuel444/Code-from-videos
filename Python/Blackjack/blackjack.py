import random
import numpy as np
import statistics
import pygame
from matplotlib import pyplot as plt


deck = ['AH','AS','AD','AC','2H','2S','2D','2C','3H','3S','3D','3C','4H','4S','4D','4C','5H','5S','5D','5C','6H','6S','6D','6C','7H','7S','7D','7C','8H','8S','8D','8C','9H','9S','9D','9C','10H','10S','10D','10C','JH','JS','JD','JC','QH','QS','QD','QC','KH','KS','KD','KC']
blackjack_strategy = {
    # Hard Totals
    (11, '2'): 'hit', (11, '3'): 'hit', (11, '4'): 'hit', (11, '5'): 'hit', (11, '6'): 'hit',
    (11, '7'): 'hit', (11, '8'): 'hit', (11, '9'): 'hit', (11, '10'): 'hit', (11, 'J'): 'hit', (11, 'Q'): 'hit', (11, 'K'): 'hit', (11, 'A'): 'hit',

    (12, '2'): 'hit', (12, '3'): 'hit', (12, '4'): 'stand', (12, '5'): 'stand', (12, '6'): 'stand',
    (12, '7'): 'hit', (12, '8'): 'hit', (12, '9'): 'hit', (12, '10'): 'hit', (12, 'J'): 'hit', (12, 'Q'): 'hit', (12, 'K'): 'hit', (12, 'A'): 'hit',

    (13, '2'): 'stand', (13, '3'): 'stand', (13, '4'): 'stand', (13, '5'): 'stand', (13, '6'): 'stand',
    (13, '7'): 'hit', (13, '8'): 'hit', (13, '9'): 'hit', (13, '10'): 'hit', (13, 'J'): 'hit', (13, 'Q'): 'hit', (13, 'K'): 'hit', (13, 'A'): 'hit',

    (14, '2'): 'stand', (14, '3'): 'stand', (14, '4'): 'stand', (14, '5'): 'stand', (14, '6'): 'stand',
    (14, '7'): 'hit', (14, '8'): 'hit', (14, '9'): 'hit', (14, '10'): 'hit', (14, 'J'): 'hit', (14, 'Q'): 'hit', (14, 'K'): 'hit', (14, 'A'): 'hit',

    (15, '2'): 'stand', (15, '3'): 'stand', (15, '4'): 'stand', (15, '5'): 'stand', (15, '6'): 'stand',
    (15, '7'): 'hit', (15, '8'): 'hit', (15, '9'): 'hit', (15, '10'): 'hit', (15, 'J'): 'hit', (15, 'Q'): 'hit', (15, 'K'): 'hit', (15, 'A'): 'hit',

    (16, '2'): 'stand', (16, '3'): 'stand', (16, '4'): 'stand', (16, '5'): 'stand', (16, '6'): 'stand',
    (16, '7'): 'hit', (16, '8'): 'hit', (16, '9'): 'hit', (16, '10'): 'hit', (16, 'J'): 'hit', (16, 'Q'): 'hit', (16, 'K'): 'hit', (16, 'A'): 'hit',

    (17, '2'): 'stand', (17, '3'): 'stand', (17, '4'): 'stand', (17, '5'): 'stand', (17, '6'): 'stand',
    (17, '7'): 'stand', (17, '8'): 'stand', (17, '9'): 'stand', (17, '10'): 'stand', (17, 'J'): 'stand', (17, 'Q'): 'stand', (17, 'K'): 'stand', (17, 'A'): 'stand',

    (18, '2'): 'stand', (18, '3'): 'stand', (18, '4'): 'stand', (18, '5'): 'stand', (18, '6'): 'stand',
    (18, '7'): 'stand', (18, '8'): 'stand', (18, '9'): 'stand', (18, '10'): 'stand', (18, 'J'): 'stand', (18, 'Q'): 'stand', (18, 'K'): 'stand', (18, 'A'): 'stand',

    (19, '2'): 'stand', (19, '3'): 'stand', (19, '4'): 'stand', (19, '5'): 'stand', (19, '6'): 'stand',
    (19, '7'): 'stand', (19, '8'): 'stand', (19, '9'): 'stand', (19, '10'): 'stand', (19, 'J'): 'stand', (19, 'Q'): 'stand', (19, 'K'): 'stand', (19, 'A'): 'stand',

    (20, '2'): 'stand', (20, '3'): 'stand', (20, '4'): 'stand', (20, '5'): 'stand', (20, '6'): 'stand',
    (20, '7'): 'stand', (20, '8'): 'stand', (20, '9'): 'stand', (20, '10'): 'stand', (20, 'J'): 'stand', (20, 'Q'): 'stand', (20, 'K'): 'stand', (20, 'A'): 'stand',

    (21, '2'): 'stand', (21, '3'): 'stand', (21, '4'): 'stand', (21, '5'): 'stand', (21, '6'): 'stand',
    (21, '7'): 'stand', (21, '8'): 'stand', (21, '9'): 'stand', (21, '10'): 'stand', (21, 'J'): 'stand', (21, 'Q'): 'stand', (21, 'K'): 'stand', (21, 'A'): 'stand',

}

soft_strategy = {
    (18, '2'): 'stand', (18, '3'): 'stand', (18, '4'): 'stand', (18, '5'): 'stand', (18, '6'): 'stand',
    (18, '7'): 'stand', (18, '8'): 'hit', (18, '9'): 'hit', (18, '10'): 'hit', (18, 'J'): 'hit', (18, 'Q'): 'hit', (18, 'K'): 'hit', (18, 'A'): 'hit',

    (19, '2'): 'stand', (19, '3'): 'stand', (19, '4'): 'stand', (19, '5'): 'stand', (19, '6'): 'stand',
    (19, '7'): 'stand', (19, '8'): 'stand', (19, '9'): 'stand', (19, '10'): 'stand', (19, 'J'): 'stand', (19, 'Q'): 'stand', (19, 'K'): 'stand', (19, 'A'): 'stand',

    (20, '2'): 'stand', (20, '3'): 'stand', (20, '4'): 'stand', (20, '5'): 'stand', (20, '6'): 'stand',
    (20, '7'): 'stand', (20, '8'): 'stand', (20, '9'): 'stand', (20, '10'): 'stand', (20, 'J'): 'stand', (20, 'Q'): 'stand', (20, 'K'): 'stand', (20, 'A'): 'stand',

    (21, '2'): 'stand', (20, '3'): 'stand', (20, '4'): 'stand', (20, '5'): 'stand', (20, '6'): 'stand',
    (21, '7'): 'stand', (20, '8'): 'stand', (20, '9'): 'stand', (20, '10'): 'stand', (20, 'J'): 'stand', (20, 'Q'): 'stand', (20, 'K'): 'stand', (20, 'A'): 'stand',

}

true_hard_strategy = {
    # Hard Totals
    
(2, '2','N'): 'hit', (2, '3','N'): 'hit', (2, '4','N'): 'hit', (2, '5','N'): 'hit', (2, '6','N'): 'hit',
    (2, '7','N'): 'hit', (2, '8','N'): 'hit', (2, '9','N'): 'hit', (2, '10','N'): 'hit', (2, 'J','N'): 'hit', (2, 'Q','N'): 'hit', (2, 'K','N'): 'hit', (2, 'A','N'): 'hit',

    (3, '2','N'): 'hit', (3, '3','N'): 'hit', (3, '4','N'): 'hit', (3, '5','N'): 'hit', (3, '6','N'): 'hit',
    (3, '7','N'): 'hit', (3, '8','N'): 'hit', (3, '9','N'): 'hit', (3, '10','N'): 'hit', (3, 'J','N'): 'hit', (3, 'Q','N'): 'hit', (3, 'K','N'): 'hit', (3, 'A','N'): 'hit',

    (4, '2','N'): 'hit', (4, '3','N'): 'hit', (4, '4','N'): 'hit', (4, '5','N'): 'hit', (4, '6','N'): 'hit',
    (4, '7','N'): 'hit', (4, '8','N'): 'hit', (4, '9','N'): 'hit', (4, '10','N'): 'hit', (4, 'J','N'): 'hit', (4, 'Q','N'): 'hit', (4, 'K','N'): 'hit', (4, 'A','N'): 'hit',

    (5, '2','N'): 'hit', (5, '3','N'): 'hit', (5, '4','N'): 'hit', (5, '5','N'): 'hit', (5, '6','N'): 'hit',
    (5, '7','N'): 'hit', (5, '8','N'): 'hit', (5, '9','N'): 'hit', (5, '10','N'): 'hit', (5, 'J','N'): 'hit', (5, 'Q','N'): 'hit', (5, 'K','N'): 'hit', (5, 'A','N'): 'hit',

    (6, '2','N'): 'hit', (6, '3','N'): 'hit', (6, '4','N'): 'hit', (6, '5','N'): 'hit', (6, '6','N'): 'hit',
    (6, '7','N'): 'hit', (6, '8','N'): 'hit', (6, '9','N'): 'hit', (6, '10','N'): 'hit', (6, 'J','N'): 'hit', (6, 'Q','N'): 'hit', (6, 'K','N'): 'hit', (6, 'A','N'): 'hit',

    (7, '2','N'): 'hit', (7, '3','N'): 'hit', (7, '4','N'): 'hit', (7, '5','N'): 'hit', (7, '6','N'): 'hit',
    (7, '7','N'): 'hit', (7, '8','N'): 'hit', (7, '9','N'): 'hit', (7, '10','N'): 'hit', (7, 'J','N'): 'hit', (7, 'Q','N'): 'hit', (7, 'K','N'): 'hit', (7, 'A','N'): 'hit',
(8, '2','N'): 'double', (8, '3','N'): 'double', (8, '4','N'): 'double', (8, '5','N'): 'double', (8, '6','N'): 'double',
    (8, '7','N'): 'hit', (8, '8','N'): 'hit', (8, '9','N'): 'hit', (8, '10','N'): 'hit', (8, 'J','N'): 'hit', (8, 'Q','N'): 'hit', (8, 'K','N'): 'hit', (8, 'A','N'): 'hit', 
(9, '2','N'): 'double', (9, '3','N'): 'double', (9, '4','N'): 'double', (9, '5','N'): 'double', (9, '6','N'): 'double',
    (9, '7','N'): 'double', (9, '8','N'): 'hit', (9, '9','N'): 'hit', (9, '10','N'): 'hit', (9, 'J','N'): 'hit', (9, 'Q','N'): 'hit', (9, 'K','N'): 'hit', (9, 'A','N'): 'hit',
    (10, '2','N'): 'double', (10, '3','N'): 'double', (10, '4','N'): 'double', (10, '5','N'): 'double', (10, '6','N'): 'double',
    (10, '7','N'): 'double', (10, '8','N'): 'double', (10, '9','N'): 'double', (10, '10','N'): 'hit', (10, 'J','N'): 'hit', (10, 'Q','N'): 'hit', (10, 'K','N'): 'hit', (10, 'A','N'): 'hit', (11, '2','N'): 'double', (11, '3','N'): 'double', (11, '4','N'): 'double', (11, '5','N'): 'double', (11, '6','N'): 'double',
    (11, '7','N'): 'double', (11, '8','N'): 'double', (11, '9','N'): 'double', (11, '10','N'): 'double', (11, 'J','N'): 'double', (11, 'Q','N'): 'double', (11, 'K','N'): 'double', (11, 'A','N'): 'hit',
    (12, '2','N'): 'stand', (12, '3','N'): 'stand', (12, '4','N'): 'stand', (12, '5','N'): 'stand', (12, '6','N'): 'stand',
    (12, '7','N'): 'hit', (12, '8','N'): 'hit', (12, '9','N'): 'hit', (12, '10','N'): 'stand', (12, 'J','N'): 'stand', (12, 'Q','N'): 'stand', (12, 'K','N'): 'stand', (12, 'A','N'): 'hit',

    (13, '2','N'): 'stand', (13, '3','N'): 'stand', (13, '4','N'): 'stand', (13, '5','N'): 'stand', (13, '6','N'): 'stand',
    (13, '7','N'): 'hit', (13, '8','N'): 'hit', (13, '9','N'): 'hit', (13, '10','N'): 'stand', (13, 'J','N'): 'stand', (13, 'Q','N'): 'stand', (13, 'K','N'): 'stand', (13, 'A','N'): 'hit',

    (14, '2','N'): 'stand', (14, '3','N'): 'stand', (14, '4','N'): 'stand', (14, '5','N'): 'stand', (14, '6','N'): 'stand',
    (14, '7','N'): 'stand', (14, '8','N'): 'stand', (14, '9','N'): 'stand', (14, '10','N'): 'stand', (14, 'J','N'): 'stand', (14, 'Q','N'): 'stand', (14, 'K','N'): 'stand', (14, 'A','N'): 'stand',

    (15, '2','N'): 'stand', (15, '3','N'): 'stand', (15, '4','N'): 'stand', (15, '5','N'): 'stand', (15, '6','N'): 'stand',
    (15, '7','N'): 'stand', (15, '8','N'): 'stand', (15, '9','N'): 'stand', (15, '10','N'): 'stand', (15, 'J','N'): 'stand', (15, 'Q','N'): 'stand', (15, 'K','N'): 'stand', (15, 'A','N'): 'stand',

    (16, '2','N'): 'stand', (16, '3','N'): 'stand', (16, '4','N'): 'stand', (16, '5','N'): 'stand', (16, '6','N'): 'stand',
    (16, '7','N'): 'stand', (16, '8','N'): 'stand', (16, '9','N'): 'stand', (16, '10','N'): 'stand', (16, 'J','N'): 'stand', (16, 'Q','N'): 'stand', (16, 'K','N'): 'stand', (16, 'A','N'): 'stand',

    (17, '2','N'): 'stand', (17, '3','N'): 'stand', (17, '4','N'): 'stand', (17, '5','N'): 'stand', (17, '6','N'): 'stand',
    (17, '7','N'): 'stand', (17, '8','N'): 'stand', (17, '9','N'): 'stand', (17, '10','N'): 'stand', (17, 'J','N'): 'stand', (17, 'Q','N'): 'stand', (17, 'K','N'): 'stand', (17, 'A','N'): 'stand',

    (18, '2','N'): 'stand', (18, '3','N'): 'stand', (18, '4','N'): 'stand', (18, '5','N'): 'stand', (18, '6','N'): 'stand',
    (18, '7','N'): 'stand', (18, '8','N'): 'stand', (18, '9','N'): 'stand', (18, '10','N'): 'stand', (18, 'J','N'): 'stand', (18, 'Q','N'): 'stand', (18, 'K','N'): 'stand', (18, 'A','N'): 'stand',

    (19, '2','N'): 'stand', (19, '3','N'): 'stand', (19, '4','N'): 'stand', (19, '5','N'): 'stand', (19, '6','N'): 'stand',
    (19, '7','N'): 'stand', (19, '8','N'): 'stand', (19, '9','N'): 'stand', (19, '10','N'): 'stand', (19, 'J','N'): 'stand', (19, 'Q','N'): 'stand', (19, 'K','N'): 'stand', (19, 'A','N'): 'stand',

    (20, '2','N'): 'stand', (20, '3','N'): 'stand', (20, '4','N'): 'stand', (20, '5','N'): 'stand', (20, '6','N'): 'stand',
    (20, '7','N'): 'stand', (20, '8','N'): 'stand', (20, '9','N'): 'stand', (20, '10','N'): 'stand', (20, 'J','N'): 'stand', (20, 'Q','N'): 'stand', (20, 'K','N'): 'stand', (20, 'A','N'): 'stand',

    (21, '2','N'): 'stand', (21, '3','N'): 'stand', (21, '4','N'): 'stand', (21, '5','N'): 'stand', (21, '6','N'): 'stand',
    (21, '7','N'): 'stand', (21, '8','N'): 'stand', (21, '9','N'): 'stand', (21, '10','N'): 'stand', (21, 'J','N'): 'stand', (21, 'Q','N'): 'stand', (21, 'K','N'): 'stand', (21, 'A','N'): 'stand',

}

true_soft_strategy = {
    (17, '2',1): 'double', (17, '3','N'): 'double', (17, '4','N'): 'double', (17, '5','N'): 'double', (17, '6','N'): 'double',
    (17, '7','N'): 'hit', (17, '8','N'): 'hit', (17, '9','N'): 'hit', (17, '10','N'): 'hit', (17, 'J','N'): 'hit', (17, 'Q','N'): 'hit', (17, 'K','N'): 'hit', (17, 'A','N'): 'hit',

    (16, '2','N'): 'hit', (16, '3','N'): 'hit', (16, '4','N'): 'double', (16, '5','N'): 'double', (16, '6','N'): 'double',
    (16, '7','N'): 'hit', (16, '8','N'): 'hit', (16, '9','N'): 'hit', (16, '10','N'): 'hit', (16, 'J','N'): 'hit', (16, 'Q','N'): 'hit', (16, 'K','N'): 'hit', (16, 'A','N'): 'hit',

    (15, '2','N'): 'hit', (15, '3','N'): 'hit', (15, '4','N'): 'double', (15, '5','N'): 'double', (15, '6','N'): 'double',
    (15, '7','N'): 'hit', (15, '8','N'): 'hit', (15, '9','N'): 'hit', (15, '10','N'): 'hit', (15, 'J','N'): 'hit', (15, 'Q','N'): 'hit', (15, 'K','N'): 'hit', (15, 'A','N'): 'hit',

    (14, '2','N'): 'hit', (14, '3','N'): 'hit', (14, '4','N'): 'hit', (14, '5','N'): 'double', (14, '6','N'): 'double',
    (14, '7','N'): 'hit', (14, '8','N'): 'hit', (14, '9','N'): 'hit', (14, '10','N'): 'hit', (14, 'J','N'): 'hit', (14, 'Q','N'): 'hit', (14, 'K','N'): 'hit', (14, 'A','N'): 'hit',

    (13, '2','N'): 'hit', (13, '3','N'): 'hit', (13, '4','N'): 'hit', (13, '5','N'): 'double', (13, '6','N'): 'double',
    (13, '7','N'): 'hit', (13, '8','N'): 'hit', (13, '9','N'): 'hit', (13, '10','N'): 'hit', (13, 'J','N'): 'hit', (13, 'Q','N'): 'hit', (13, 'K','N'): 'hit', (13, 'A','N'): 'hit',

    (18, '2','N'): 'double', (18, '3','N'): 'double', (18, '4','N'): 'double', (18, '5','N'): 'double', (18, '6','N'): 'double',
    (18, '7','N'): 'stand', (18, '8','N'): 'stand', (18, '9','N'): 'hit', (18, '10','N'): 'hit', (18, 'J','N'): 'hit', (18, 'Q','N'): 'hit', (18, 'K','N'): 'hit', (18, 'A','N'): 'hit',

    (19, '2','N'): 'stand', (19, '3','N'): 'stand', (19, '4',3): 'hit', (19, '5',1): 'hit', (19, '6', 0): 'double',
    (19, '7','N'): 'stand', (19, '8','N'): 'stand', (19, '9','N'): 'stand', (19, '10','N'): 'stand', (19, 'J','N'): 'stand', (19, 'Q','N'): 'stand', (19, 'K','N'): 'stand', (19, 'A','N'): 'stand',

    (20, '2','N'): 'stand', (20, '3','N'): 'stand', (20, '4','N'): 'stand', (20, '5','N'): 'stand', (20, '6','N'): 'stand',
    (20, '7','N'): 'stand', (20, '8','N'): 'stand', (20, '9','N'): 'stand', (20, '10','N'): 'stand', (20, 'J','N'): 'stand', (20, 'Q','N'): 'stand', (20, 'K','N'): 'stand', (20, 'A','N'): 'stand',

    (21, '2','N'): 'stand', (20, '3','N'): 'stand', (20, '4','N'): 'stand', (20, '5','N'): 'stand', (20, '6','N'): 'stand',
    (21, '7','N'): 'stand', (20, '8','N'): 'stand', (20, '9','N'): 'stand', (20, '10','N'): 'stand', (20, 'J','N'): 'stand', (20, 'Q','N'): 'stand', (20, 'K','N'): 'stand', (20, 'A','N'): 'stand',

}

true_split_strategy = {
    # Split Totals

    ('A', '2','N'): 'yes', ('A', '3','N'): 'yes', ('A', '4','N'): 'yes', ('A', '5','N'): 'yes', ('A', '6','N'): 'yes',
    ('A', '7','N'): 'yes', ('A', '8','N'): 'yes', ('A', '9','N'): 'yes', ('A', '10','N'): 'yes', ('A', 'J','N'): 'yes', ('A', 'Q','N'): 'yes', ('A', 'K','N'): 'yes', ('A', 'A','N'): 'yes',

    ('K', '2','N'): 'no', ('K', '3','N'): 'no', ('K', '4',6):'yes/no', ('K', '5',5):'yes/no', ('K', '6',4):'yes/no',
    ('K', '7','N'): 'no', ('K', '8','N'): 'no', ('K', '9','N'): 'no', ('K', '10','N'): 'no', ('K', 'J','N'): 'no', ('K', 'Q','N'): 'no', ('K', 'K','N'): 'no', ('K', 'A','N'): 'no',

    ('J', '2','N'): 'no', ('J', '3','N'): 'no', ('J', '4',6):'yes/no', ('J', '5',5):'yes/no', ('J', '6',4):'yes/no',
    ('J', '7','N'): 'no', ('J', '8','N'): 'no', ('J', '9','N'): 'no', ('J', '10','N'): 'no', ('J', 'J','N'): 'no', ('J', 'Q','N'): 'no', ('J', 'K','N'): 'no', ('J', 'A','N'): 'no',

    ('Q', '2','N'): 'no', ('Q', '3','N'): 'no', ('Q', '4',6):'yes/no', ('Q', '5',5):'yes/no', ('Q', '6',4):'yes/no',
    ('Q', '7','N'): 'no', ('Q', '8','N'): 'no', ('Q', '9','N'): 'no', ('Q', '10','N'): 'no', ('Q', 'J','N'): 'no', ('Q', 'Q','N'): 'no', ('Q', 'K','N'): 'no', ('Q', 'A','N'): 'no',

    ('1', '2','N'): 'no', ('1', '3','N'): 'no', ('1', '4',6):'yes/no', ('1', '5',5):'yes/no', ('1', '6',4):'yes/no',
    ('1', '7','N'): 'no', ('1', '8','N'): 'no', ('1', '9','N'): 'no', ('1', '10','N'): 'no', ('1', 'J','N'): 'no', ('1', 'Q','N'): 'no', ('1', 'K','N'): 'no', ('1', 'A','N'): 'no',

    ('2', '2','N'): 'no', ('2', '3','N'): 'no', ('2', '4','N'): 'yes', ('2', '5','N'): 'yes', ('2', '6','N'): 'yes',
    ('2', '7','N'): 'yes', ('2', '8','N'): 'no', ('2', '9','N'): 'no', ('2', '10','N'): 'no', ('2', 'J','N'): 'no', ('2', 'Q','N'): 'no', ('2', 'K','N'): 'no', ('2', 'A','N'): 'no',

    ('3', '2','N'): 'no', ('3', '3','N'): 'no', ('3', '4','N'): 'yes', ('3', '5','N'): 'yes', ('3', '6','N'): 'yes',
    ('3', '7','N'): 'yes', ('3', '8','N'): 'no', ('3', '9','N'): 'no', ('3', '10','N'): 'no', ('3', 'J','N'): 'no', ('3', 'Q','N'): 'no', ('3', 'K','N'): 'no', ('3', 'A','N'): 'no',

    ('4', '2','N'): 'no', ('4', '3','N'): 'no', ('4', '4','N'): 'no', ('4', '5','N'): 'no', ('4', '6','N'): 'yes',
    ('4', '7','N'): 'no', ('4', '8','N'): 'no', ('4', '9','N'): 'no', ('4', '10','N'): 'no', ('4', 'J','N'): 'no', ('4', 'Q','N'): 'no', ('4', 'K','N'): 'no', ('4', 'A','N'): 'no',

    ('5', '2','N'): 'no', ('5', '3','N'): 'no', ('5', '4','N'): 'no', ('5', '5','N'): 'no', ('5', '6','N'): 'yes',
    ('5', '7','N'): 'no', ('5', '8','N'): 'no', ('5', '9','N'): 'no', ('5', '10','N'): 'no', ('5', 'J','N'): 'no', ('5', 'Q','N'): 'no', ('5', 'K','N'): 'no', ('5', 'A','N'): 'no',

    ('6', '2','N'): 'yes', ('6', '3','N'): 'yes', ('6', '4','N'): 'yes', ('6', '5','N'): 'yes', ('6', '6','N'): 'yes',
    ('6', '7','N'): 'no', ('6', '8','N'): 'no', ('6', '9','N'): 'no', ('6', '10','N'): 'no', ('6', 'J','N'): 'no', ('6', 'Q','N'): 'no', ('6', 'K','N'): 'no', ('6', 'A','N'): 'no',

    ('7', '2','N'): 'yes', ('7', '3','N'): 'yes', ('7', '4','N'): 'yes', ('7', '5','N'): 'yes', ('7', '6','N'): 'yes',
    ('7', '7','N'): 'yes', ('7', '8','N'): 'no', ('7', '9','N'): 'no', ('7', '10','N'): 'no', ('7', 'J','N'): 'no', ('7', 'Q','N'): 'no', ('7', 'K','N'): 'no', ('7', 'A','N'): 'no',

    ('8', '2','N'): 'yes', ('8', '3','N'): 'yes', ('8', '4','N'): 'yes', ('8', '5','N'): 'yes', ('8', '6','N'): 'yes',
    ('8', '7','N'): 'yes', ('8', '8','N'): 'yes', ('8', '9','N'): 'yes', ('8', '10','N'): 'yes', ('8', 'J','N'): 'yes', ('8', 'Q','N'): 'yes', ('8', 'K','N'): 'yes', ('8', 'A','N'): 'yes',

    ('9', '2','N'): 'yes', ('9', '3','N'): 'yes', ('9', '4','N'): 'yes', ('9', '5','N'): 'yes', ('9', '6','N'): 'yes',
    ('9', '7','N'): 'no', ('9', '8','N'): 'yes', ('9', '9','N'): 'yes', ('9', '10','N'): 'no', ('9', 'J','N'): 'no', ('9', 'Q','N'): 'no', ('9', 'K','N'): 'yes', ('9', 'A','N'): 'no',
}

# Draws a card from the deck and updates Hi-Lo count
def takeCard(cardsLeft, hand, count):
    hand.append(cardsLeft[0])

    # Hi-Lo card counting system
    if cardsLeft[0][:-1] in ['A','10','J','Q','K']:
        count -= 1
    elif cardsLeft[0][:-1] in ['2','3','4','5','6']:
        count += 1

    del cardsLeft[0]
    return cardsLeft, hand, count


# Calculates true count (normalized by decks remaining)
def trueCount(cardsLeft, count):
    try:
        true_count = count / (len(cardsLeft) / 52)
        true_count = int(true_count)
    except ZeroDivisionError:
        true_count = count
    return true_count

def ruin_probability(m, x, p):
    if p <= 0:
        return 1.0
    N = m / x
    ratio = (1 - p) / (1 + p)
    return ratio ** N

# Reshuffles a new shoe of n decks
def reshuffle(n):
    cardsLeft = []
    for i in range(n):
        cardsLeft.extend(deck)
    random.shuffle(cardsLeft)
    return cardsLeft, 0


# Initializes a new hand for players and dealer
def newhand(cardsLeft, money, count):
    global money_graph, total, ready, wins, prepared, move
    blackjack = False
    dealer_blackjack = False
    p = 0  # Number of NPC players

    cards = []
    players = [[]]
    dealer = []
    money_initial = money

    for i in range(p):
        cards.append([])

     # Determine bet size based on true count
    true_count = trueCount(cardsLeft, count)
    
    if true_count > 1:
        bet = 10#((true_count-1)**1) * 11#(statistics.median(money_graph)//900)
        #if bet < 11:
            #bet = 10
    else:
        bet = 10
    if bet > 1000:
            bet = 1000
    ready = False
    ##if true_count > 1:
        #money_initial = money
        #ready = True
        #total += 1

    # Deal initial cards
    for i in range(2):
        cardsLeft, players[0], count = takeCard(cardsLeft, players[0], count)
        for j in range(p):
            cardsLeft, cards[j], count = takeCard(cardsLeft, cards[j], count)
        cardsLeft, dealer, count = takeCard(cardsLeft, dealer, count)

    
    

    # Offer insurance if dealer shows Ace
    takeInsurance = False
    if dealer[0][0] == 'A':
        if true_count >= 0:
            takeInsurance = True

    dealerInitialVal, soft = value(dealer)
    if dealerInitialVal == 21:
        dealer_blackjack = True

    # Check for player's blackjack
    initialVal, soft = value(players[0])
    if initialVal == 21 and len(players[0]) == 2:
        blackjack = True
        if not dealer_blackjack:
            money += (bet * 1.5)
        doubled_down = False
    if not blackjack and dealer_blackjack:
        money -= bet
    if not dealer_blackjack and not blackjack:
        # Handle splitting
        splitting = True
        while splitting:
            check = 0
            for i in range(len(players)):
                if value([players[i][0]]) == value([players[i][1]]):
                    for ranges in ['N', 4, 5, 6]:
                        key = (players[i][0][0], dealer[0][:-1], ranges)
                        try:
                            split = true_split_strategy[key]
                            if ranges != 'N':
                                if ranges <= true_count:
                                    split = 'yes'
                                else:
                                    split = 'no'
                            break
                        except KeyError:
                            next
                    if split == 'yes':
                        players.append([players[i][1]])
                        players[i] = [players[i][0]]
                        cardsLeft, players[i], count = takeCard(cardsLeft, players[i], count)
                        cardsLeft, players[-1], count = takeCard(cardsLeft, players[-1], count)
                    else:
                        check += 1
                else:
                    check += 1
                if check == len(players):
                    splitting = False

            # Process each hand
            hands = len(players)
            bets = [bet for _ in range(hands)]
            amount = [0 for _ in range(hands)]
            doubled_down = [False for _ in range(hands)]

            for i in range(len(players)):
                amount[i], cardsLeft, count, doubled_down[i] = player(cardsLeft, players[i], dealer[0], count)
                if doubled_down[i]:
                    bets[i] *= 2

    if not dealer_blackjack:
        # Play NPC hands
        for i in range(p):
            cardsLeft, count, fill = npc(cardsLeft, cards[i], dealer[0], count)

        # Dealer's turn
        done = False
        while not done:
            valuation, soft = value(dealer)
            if valuation < 17:
                cardsLeft, dealer, count = takeCard(cardsLeft, dealer, count)
            else:
                done = True

        # Resolve outcomes
        if not blackjack:
            for i in range(len(players)):
                if (amount[i] > valuation or valuation > 21) and amount[i] <= 21:
                    money += bets[i]
                elif amount[i] == valuation and amount[i] <= 21:
                    pass  # push
                else:
                    money -= bets[i]
    if takeInsurance:
        if dealer[1][:-1] in ['10', 'J', 'K', 'Q']:
            money += bet
        else:
            money -= bet/2
    for i in range(len(prepared)):
        if prepared[i]:
            if move[i] == 'stand':
                wins[i][0] += (money-money_initial)
                wins[i][3] += 1
            elif move[i] == 'hit':
                wins[i][1] += (money-money_initial)
                wins[i][4] += 1
            elif move[i] == 'double':
                wins[i][2] += (money-money_initial)
                wins[i][5] += 1
            
        #vals[len(cardsLeft)].append(money-money_initial)
    prepared = [False for i in range(len(true_hard_strategy))]
    move = ['stand' for i in range(len(true_hard_strategy))]
    money_graph.append(money)
    return cardsLeft, money, count


# Handles player's turn based on strategy
def player(cardsLeft, hand, dealer, count):
    global total, ready, dcard, pval, money_initial, prepared, move, wins

    while True:
        valuation, soft = value(hand)

        if valuation > 21:
            return valuation, cardsLeft, count, False

        true_count = trueCount(cardsLeft, count)
        if true_count == truth and not(soft):
            location = list(true_hard_strategy).index((valuation, dealer[:-1], 'N'))
            action = random.choice(['stand','hit','double'])
            if action == 'double' and len(hand) > 2:
                action = 'hit'
            move[location] = action
            prepared[location] = True
        else:
            '''if valuation == pval and dcard == dealer[:-1] and true_count == truth:
                ready = True
                total += 1
                money_initial = money'''

            action = ''
            for ranges in ['N',-2, -1, 0, 1, 2, 3, 4, 5, 6]:
                key = (valuation, dealer[:-1], ranges)
                if not soft:
                    try:
                        action = true_hard_strategy[key]
                        break
                    except KeyError:
                        next
                else:
                    try:
                        action = true_soft_strategy[key]
                        break
                    except KeyError:
                        next

            if key[2] != 'N' and action != '':
                if key[2] > true_count:
                    action = 'hit'
        
            

        if (action == 'double' and len(hand) > 2) or action == '':
            action = 'hit'

        

        if action == 'hit':
            cardsLeft, hand, count = takeCard(cardsLeft, hand, count)
        elif action == 'stand':
            return valuation, cardsLeft, count, False
        elif action == 'double':
            cardsLeft, hand, count = takeCard(cardsLeft, hand, count)
            valuation, soft = value(hand)
            return valuation, cardsLeft, count, True


# Simulates NPC strategy
def npc(cardsLeft, hand, dealer, count):
    while True:
        valuation, soft = value(hand)

        if valuation > 21:
            return cardsLeft, count, hand

        key = (valuation, dealer[:-1])
        if not soft:
            try:
                action = blackjack_strategy[key]
            except KeyError:
                action = 'hit'
        else:
            try:
                action = soft_strategy[key]
            except KeyError:
                action = 'hit'

        if action == 'hit':
            cardsLeft, hand, count = takeCard(cardsLeft, hand, count)
        elif action == 'stand':
            return cardsLeft, count, hand



# Returns the total value and whether it's a soft hand
def value(hand):
    totals = 0
    aces = 0

    for card in hand:
        rank = card[:-1]
        if rank == 'A':
            totals += 11
            aces += 1
        elif rank in ['K', 'Q', 'J']:
            totals += 10
        else:
            totals += int(rank)

    while totals > 21 and aces > 0:
        totals -= 10
        aces -= 1

    soft = len(hand) == 2 and (aces == 1)
    return totals, soft


# Starts a new simulation
def start():
    m = 100000  # Starting money
    n = 6      # Number of decks
    return n, m

wins = [[0,0,0,0,0,0] for i in range(len(true_hard_strategy))]
prepared = [False for i in range(len(true_hard_strategy))]
move = ['stand' for i in range(len(true_hard_strategy))]

file = open('BlackjackResults.txt', 'a')

for truth in [0,-1,1,-2,2,3,4,5]:
        wins = [[0,0,0,0,0,0] for i in range(len(true_hard_strategy))]
        file.write(('TRUE COUNT ' + str(truth) + ' \n'))
        print('True Count', truth)
        toTest = true_hard_strategy

        for m in [1]:
            ###pval = m[0]
            ##dcard = m[1]
            #results = []
            for b in ['stand']:
                #hold = true_hard_strategy[(pval,dcard,'N')]
                #true_hard_strategy[(pval,dcard,'N')] = b
                total = 0
                n,money = start()
                money_graph = [money]
                cardsLeft, count = reshuffle(n)
                cardsLeft, money, count = newhand(cardsLeft, money, count)
                i=0
                while i<10000000:
                    i+=1
                    if len(cardsLeft) > 65:#and count > -12:
                        cardsLeft, money, count = newhand(cardsLeft, money, count)
                    else:
                        cardsLeft, count = reshuffle(n)

                x_values = np.arange(len(money_graph)) / 120
                for i in range(len(wins)):
                    file.write("For the combination " + str((list(true_hard_strategy))[i]) + ' we get:\n')
                    if wins[i][3] != 0 and wins[i][4] != 0 and wins[i][5] != 0:
                        standResult = wins[i][0]/wins[i][3]
                        hitResult = wins[i][1]/wins[i][4]
                        doubleResult = wins[i][2]/wins[i][5]
                        if standResult > hitResult and standResult > doubleResult:
                            file.write('The best is to stand with £' + str(standResult) + ' being made from gathering ' + str(wins[i][3]) + " results!\n")
                        elif hitResult > doubleResult:
                            file.write('The best is to hit with £' + str(standResult) + ' being made from gathering ' + str(wins[i][4]) + " results!\n")
                        else:
                            file.write('The best is to double with £' + str(standResult) + ' being made from gathering ' + str(wins[i][5]) + " results!\n")
                    else:
                        file.write('Invalid since there was not enough results\n')
                    file.write('\n')
                file.close()
                file = open('BlackjackResults.txt', 'a')

                    

                #plt.plot(x_values, money_graph)
                    ##plt.plot(x_values, best_fit_line, color='red', linestyle='--', label='Best Fit Line')
                #plt.show() 


            '''if results[0] < results[2] and results[1] < results[2]:
                print ('The best choice is to double, with winning £' + str((results[2])) + ' per £10' )
                if results[0] > results[1]:
                    print ('If double is not avaliable then stand')
                else:
                    print ('If double is not avaliable then hit')
            elif results[0] > results[1]:
                print ('The best choice is to stand, with winning £' + str((results[0])) + ' per £10' )
            else:
                print ('The best choice is to hit, with winning £' + str((results[1])) + ' per £10' )
            true_hard_strategy[(pval,dcard,'N')] = hold'''

            
'''
vals = [[] for _ in range(312)]                  
fails = 0
chances = []
prob = []
for f in range(10):
    wins = 0
    total = 0
    numOfRounds = 0
    n,m = start()
    money = m
    money_graph = [money]
    cardsLeft, count = reshuffle(n)
    cardsLeft, money, count = newhand(cardsLeft, money, count)
    i=0
    while i<100000 and money > 0:
        i+=1
        if len(cardsLeft) > 60 and count > -3:
            cardsLeft, money, count = newhand(cardsLeft, money, count)
            numOfRounds += 1
        else:
            cardsLeft, count = reshuffle(n)
    if money <= 0:
        fails += 1
    chances.append(wins/total)
    prob.append(total/numOfRounds)
    x_values = np.arange(len(money_graph)) / 120
    plt.plot(x_values, money_graph)
    plt.show() 
print ('Median value is:', statistics.mean(chances))
print ('You lost money', fails, 'times in 10 games')
print ('Chance of being in this true count:', statistics.mean(prob))
'''
'''done = False
i = 0
reminds = vals
while not done:
    if i >= len(vals):
        i = 0
    if vals[i] == []:
        del vals[i]
    if not([] in vals):
        done = True
    
    i += 1
for i in range(len(vals)):
        
        vals[i] = statistics.mean(vals[i])

#vals = vals[210:]
x_values = list(range(1, len(vals)+1))
m, b = np.polyfit(x_values, vals, 1)

#Create the best fit line values
x_fit = np.linspace(min(x_values), max(x_values), 100)
y_fit = m * x_fit + b
print ("Crosses x-axis at", -b/m)
plt.scatter(x_values, vals)
plt.plot(x_fit, y_fit, color='red', label=f'Best fit: y = {m:.2f}x + {b:.2f}')
plt.show()
pass     
'''
    
    
    
    
    
    
    

    
''' Hi Low 
        if cardsLeft[0][:-1] in ['A','10','J','Q','K']:
            count -= 1
        elif cardsLeft[0][:-1] in ['2','3','4','5','6']:
            count += 1
        
        Halves
        if cardsLeft[0][:-1] in ['2', '7']:
            count += 0.5
        elif cardsLeft[0][:-1] in ['3','4','6']:
            count += 1
        elif cardsLeft[0][:-1] in ['5']:
            count += 1.5
        elif cardsLeft[0][:-1] in ['9']:
            count -= 0.5
        elif cardsLeft[0][:-1] in ['J', 'K', '10', 'Q', 'A']:
            count -= 1
        
'''
    