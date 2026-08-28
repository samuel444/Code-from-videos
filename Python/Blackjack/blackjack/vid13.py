import pygame
import random
pygame.init()

hard_strategy = {
    # Hard Totals
    (9, '2'): 'hit', (9, '3'): 'double', (9, '4'): 'double', (9, '5'): 'double', (9, '6'): 'double',
    (9, '7'): 'hit', (9, '8'): 'hit', (9, '9'): 'hit', (9, '10'): 'hit', (9, 'J'): 'hit', (9, 'Q'): 'hit', (9, 'K'): 'hit', (9, 'A'): 'hit',

    (10, '2'): 'double', (10, '3'): 'double', (10, '4'): 'double', (10, '5'): 'double', (10, '6'): 'double',
    (10, '7'): 'double', (10, '8'): 'double', (10, '9'): 'double', (10, '10'): 'hit', (10, 'J'): 'hit', (10, 'Q'): 'hit', (10, 'K'): 'hit', (10, 'A'): 'hit',

    (11, '2'): 'double', (11, '3'): 'double', (11, '4'): 'double', (11, '5'): 'double', (11, '6'): 'double',
    (11, '7'): 'double', (11, '8'): 'double', (11, '9'): 'double', (11, '10'): 'double', (11, 'J'): 'double', (11, 'Q'): 'double', (11, 'K'): 'double', (11, 'A'): 'double',

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
    (13, '2'): 'hit', (13, '3'): 'hit', (13, '4'): 'hit', (13, '5'): 'double', (13, '6'): 'double',
    (13, '7'): 'hit', (13, '8'): 'hit', (13, '9'): 'hit', (13, '10'): 'hit', (13, 'J'): 'hit', (13, 'Q'): 'hit', (13, 'K'): 'hit', (13, 'A'): 'hit',
    
    (14, '2'): 'hit', (14, '3'): 'hit', (14, '4'): 'hit', (14, '5'): 'double', (14, '6'): 'double',
    (14, '7'): 'hit', (14, '8'): 'hit', (14, '9'): 'hit', (14, '10'): 'hit', (14, 'J'): 'hit', (14, 'Q'): 'hit', (14, 'K'): 'hit', (14, 'A'): 'hit',

    (15, '2'): 'hit', (15, '3'): 'hit', (15, '4'): 'double', (15, '5'): 'double', (15, '6'): 'double',
    (15, '7'): 'hit', (15, '8'): 'hit', (15, '9'): 'hit', (15, '10'): 'hit', (15, 'J'): 'hit', (15, 'Q'): 'hit', (15, 'K'): 'hit', (15, 'A'): 'hit',

    (16, '2'): 'hit', (16, '3'): 'hit', (16, '4'): 'double', (16, '5'): 'double', (16, '6'): 'double',
    (16, '7'): 'hit', (16, '8'): 'hit', (16, '9'): 'hit', (16, '10'): 'hit', (16, 'J'): 'hit', (16, 'Q'): 'hit', (16, 'K'): 'hit', (16, 'A'): 'hit',

    (17, '2'): 'hit', (17, '3'): 'double', (17, '4'): 'double', (17, '5'): 'double', (17, '6'): 'double',
    (17, '7'): 'hit', (17, '8'): 'hit', (17, '9'): 'hit', (17, '10'): 'hit', (17, 'J'): 'hit', (17, 'Q'): 'hit', (17, 'K'): 'hit', (17, 'A'): 'hit',

    (18, '2'): 'stand', (18, '3'): 'stand', (18, '4'): 'stand', (18, '5'): 'stand', (18, '6'): 'stand',
    (18, '7'): 'stand', (18, '8'): 'stand', (18, '9'): 'hit', (18, '10'): 'hit', (18, 'J'): 'hit', (18, 'Q'): 'hit', (18, 'K'): 'hit', (18, 'A'): 'hit',

    (19, '2'): 'stand', (19, '3'): 'stand', (19, '4'): 'stand', (19, '5'): 'stand', (19, '6'): 'stand',
    (19, '7'): 'stand', (19, '8'): 'stand', (19, '9'): 'stand', (19, '10'): 'stand', (19, 'J'): 'stand', (19, 'Q'): 'stand', (19, 'K'): 'stand', (19, 'A'): 'stand',

    (20, '2'): 'stand', (20, '3'): 'stand', (20, '4'): 'stand', (20, '5'): 'stand', (20, '6'): 'stand',
    (20, '7'): 'stand', (20, '8'): 'stand', (20, '9'): 'stand', (20, '10'): 'stand', (20, 'J'): 'stand', (20, 'Q'): 'stand', (20, 'K'): 'stand', (20, 'A'): 'stand',

    (21, '2'): 'stand', (21, '3'): 'stand', (21, '4'): 'stand', (21, '5'): 'stand', (21, '6'): 'stand',
    (21, '7'): 'stand', (21, '8'): 'stand', (21, '9'): 'stand', (21, '10'): 'stand', (21, 'J'): 'stand', (21, 'Q'): 'stand', (21, 'K'): 'stand', (21, 'A'): 'stand',

}

split_strategy = {
    (2, '2'): 'no', (2, '3'): 'no', (2, '4'): 'yes', (2, '5'): 'yes', (2, '6'): 'yes',
    (2, '7'): 'yes', (2, '8'): 'no', (2, '9'): 'no', (2, '10'): 'no', (2, 'J'): 'no', (2, 'Q'): 'no', (2, 'K'): 'no', (2, 'A'): 'no',

    (3, '2'): 'no', (3, '3'): 'no', (3, '4'): 'yes', (3, '5'): 'yes', (3, '6'): 'yes',
    (3, '7'): 'yes', (3, '8'): 'no', (3, '9'): 'no', (3, '10'): 'no', (3, 'J'): 'no', (3, 'Q'): 'no', (3, 'K'): 'no', (3, 'A'): 'no',

    (4, '2'): 'no', (4, '3'): 'no', (4, '4'): 'no', (4, '5'): 'no', (4, '6'): 'yes',
    (4, '7'): 'no', (4, '8'): 'no', (4, '9'): 'no', (4, '10'): 'no', (4, 'J'): 'no', (4, 'Q'): 'no', (4, 'K'): 'no', (4, 'A'): 'no',

    (5, '2'): 'no', (5, '3'): 'no', (5, '4'): 'no', (5, '5'): 'no', (5, '6'): 'yes',
    (5, '7'): 'no', (5, '8'): 'no', (5, '9'): 'no', (5, '10'): 'no', (5, 'J'): 'no', (5, 'Q'): 'no', (5, 'K'): 'no', (5, 'A'): 'no',

    (6, '2'): 'yes', (6, '3'): 'yes', (6, '4'): 'yes', (6, '5'): 'yes', (6, '6'): 'yes',
    (6, '7'): 'no', (6, '8'): 'no', (6, '9'): 'no', (6, '10'): 'no', (6, 'J'): 'no', (6, 'Q'): 'no', (6, 'K'): 'no', (6, 'A'): 'no',

    (7, '2'): 'yes', (7, '3'): 'yes', (7, '4'): 'yes', (7, '5'): 'yes', (7, '6'): 'yes',
    (7, '7'): 'yes', (7, '8'): 'no', (7, '9'): 'no', (7, '10'): 'no', (7, 'J'): 'no', (7, 'Q'): 'no', (7, 'K'): 'no', (7, 'A'): 'no',

    (8, '2'): 'yes', (8, '3'): 'yes', (8, '4'): 'yes', (8, '5'): 'yes', (8, '6'): 'yes',
    (8, '7'): 'yes', (8, '8'): 'yes', (8, '9'): 'yes', (8, '10'): 'yes', (8, 'J'): 'yes', (8, 'Q'): 'yes', (8, 'K'): 'yes', (8, 'A'): 'yes',

    (9, '2'): 'yes', (9, '3'): 'yes', (9, '4'): 'yes', (9, '5'): 'yes', (9, '6'): 'yes',
    (9, '7'): 'no', (9, '8'): 'yes', (9, '9'): 'yes', (9, '10'): 'no', (9, 'J'): 'no', (9, 'Q'): 'no', (9, 'K'): 'no', (9, 'A'): 'no',

    (10, '2'): 'no', (10, '3'): 'no', (10, '4'): 'no', (10, '5'): 'no', (10, '6'): 'no',
    (10, '7'): 'no', (10, '8'): 'no', (10, '9'): 'no', (10, '10'): 'no', (10, 'J'): 'no', (10, 'Q'): 'no', (10, 'K'): 'no', (10, 'A'): 'no',

   (11, '2'): 'yes', (11, '3'): 'yes', (11, '4'): 'yes', (11, '5'): 'yes', (11, '6'): 'yes',
    (11, '7'): 'yes', (11, '8'): 'yes', (11, '9'): 'yes', (11, '10'): 'yes', (11, 'J'): 'yes', (11, 'Q'): 'yes', (11, 'K'): 'yes', (11, 'A'): 'yes'
}

true_hard_strategy = {
    # Hard Totals
    (4, '2','N'): 'hit', (4, '3','N'): 'hit', (4, '4','N'): 'hit', (4, '5','N'): 'hit', (4, '6','N'): 'hit',
    (4, '7','N'): 'hit', (4, '8','N'): 'hit', (4, '9','N'): 'hit', (4, '10','N'): 'hit', (4, 'J','N'): 'hit', (4, 'Q','N'): 'hit', (4, 'K','N'): 'hit', (4, 'A','N'): 'hit',

    (5, '2','N'): 'hit', (5, '3','N'): 'hit', (5, '4','N'): 'hit', (5, '5','N'): 'hit', (5, '6','N'): 'hit',
    (5, '7','N'): 'hit', (5, '8','N'): 'hit', (5, '9','N'): 'hit', (5, '10','N'): 'hit', (5, 'J','N'): 'hit', (5, 'Q','N'): 'hit', (5, 'K','N'): 'hit', (5, 'A','N'): 'hit',

    (6, '2','N'): 'hit', (6, '3','N'): 'hit', (6, '4','N'): 'hit', (6, '5','N'): 'hit', (6, '6','N'): 'hit',
    (6, '7','N'): 'hit', (6, '8','N'): 'hit', (6, '9','N'): 'hit', (6, '10','N'): 'hit', (6, 'J','N'): 'hit', (6, 'Q','N'): 'hit', (6, 'K','N'): 'hit', (6, 'A','N'): 'hit',

    (7, '2','N'): 'hit', (7, '3','N'): 'hit', (7, '4','N'): 'hit', (7, '5','N'): 'hit', (7, '6','N'): 'hit',
    (7, '7','N'): 'hit', (7, '8','N'): 'hit', (7, '9','N'): 'hit', (7, '10','N'): 'hit', (7, 'J','N'): 'hit', (7, 'Q','N'): 'hit', (7, 'K','N'): 'hit', (7, 'A','N'): 'hit',

    (8, '2','N'): 'hit', (8, '3','N'): 'hit', (8, '4','N'): 'hit', (8, '5','N'): 'hit', (8, '6',2): 'hit/double',
    (8, '7','N'): 'hit', (8, '8','N'): 'hit', (8, '9','N'): 'hit', (8, '10','N'): 'hit', (8, 'J','N'): 'hit', (8, 'Q','N'): 'hit', (8, 'K','N'): 'hit', (8, 'A','N'): 'hit',

    (9, '2',1): 'hit/double', (9, '3','N'): 'double', (9, '4','N'): 'double', (9, '5','N'): 'double', (9, '6','N'): 'double',
    (9, '7',3): 'hit/double', (9, '8','N'): 'hit', (9, '9','N'): 'hit', (9, '10','N'): 'hit', (9, 'J','N'): 'hit', (9, 'Q','N'): 'hit', (9, 'K','N'): 'hit', (9, 'A','N'): 'hit',

    (10, '2','N'): 'double', (10, '3','N'): 'double', (10, '4','N'): 'double', (10, '5','N'): 'double', (10, '6','N'): 'double',
    (10, '7','N'): 'double', (10, '8','N'): 'double', (10, '9','N'): 'double', (10, '10',4): 'hit/double', (10, 'J',4): 'hit/double', (10, 'Q',4): 'hit/double', (10, 'K',4): 'hit/double', (10, 'A',3): 'hit/double',

    (11, '2','N'): 'double', (11, '3','N'): 'double', (11, '4','N'): 'double', (11, '5','N'): 'double', (11, '6','N'): 'double',
    (11, '7','N'): 'double', (11, '8','N'): 'double', (11, '9','N'): 'double', (11, '10','N'): 'double', (11, 'J','N'): 'double', (11, 'Q','N'): 'double', (11, 'K','N'): 'double', (11, 'A','N'): 'double',

    (12, '2',3): 'hit/stand', (12, '3',2): 'hit/stand', (12, '4',0): 'hit/stand', (12, '5','N'): 'stand', (12, '6','N'): 'stand',
    (12, '7','N'): 'hit', (12, '8','N'): 'hit', (12, '9','N'): 'hit', (12, '10','N'): 'hit', (12, 'J','N'): 'hit', (12, 'Q','N'): 'hit', (12, 'K','N'): 'hit', (12, 'A','N'): 'hit',

    (13, '2',-1): 'hit/stand', (13, '3','N'): 'stand', (13, '4','N'): 'stand', (13, '5','N'): 'stand', (13, '6','N'): 'stand',
    (13, '7','N'): 'hit', (13, '8','N'): 'hit', (13, '9','N'): 'hit', (13, '10','N'): 'hit', (13, 'J','N'): 'hit', (13, 'Q','N'): 'hit', (13, 'K','N'): 'hit', (13, 'A','N'): 'hit',

    (14, '2','N'): 'stand', (14, '3','N'): 'stand', (14, '4','N'): 'stand', (14, '5','N'): 'stand', (14, '6','N'): 'stand',
    (14, '7','N'): 'hit', (14, '8','N'): 'hit', (14, '9','N'): 'hit', (14, '10','N'): 'hit', (14, 'J','N'): 'hit', (14, 'Q','N'): 'hit', (14, 'K','N'): 'hit', (14, 'A','N'): 'hit',

    (15, '2','N'): 'stand', (15, '3','N'): 'stand', (15, '4','N'): 'stand', (15, '5','N'): 'stand', (15, '6','N'): 'stand',
    (15, '7','N'): 'hit', (15, '8','N'): 'hit', (15, '9','N'): 'hit', (15, '10',4): 'hit/stand', (15, 'J',4): 'hit/stand', (15, 'Q',4): 'hit/stand', (15, 'K',4): 'hit/stand', (15, 'A',5): 'hit/stand',

    (16, '2','N'): 'stand', (16, '3','N'): 'stand', (16, '4','N'): 'stand', (16, '5','N'): 'stand', (16, '6','N'): 'stand',
    (16, '7','N'): 'hit', (16, '8','N'): 'hit', (16, '9',4): 'hit/stand', (16, '10',0): 'hit/stand', (16, 'J',0): 'hit/stand', (16, 'Q',0): 'hit/stand', (16, 'K',0): 'hit/stand', (16, 'A',3): 'hit/stand',

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
    (13, '2','N'): 'hit', (13, '3','N'): 'hit', (13, '4','N'): 'hit', (13, '5','N'): 'double', (13, '6','N'): 'double',
    (13, '7','N'): 'hit', (13, '8','N'): 'hit', (13, '9','N'): 'hit', (13, '10','N'): 'hit', (13, 'J','N'): 'hit', (13, 'Q','N'): 'hit', (13, 'K','N'): 'hit', (13, 'A','N'): 'hit',
    
    (14, '2','N'): 'hit', (14, '3','N'): 'hit', (14, '4','N'): 'hit', (14, '5','N'): 'double', (14, '6','N'): 'double',
    (14, '7','N'): 'hit', (14, '8','N'): 'hit', (14, '9','N'): 'hit', (14, '10','N'): 'hit', (14, 'J','N'): 'hit', (14, 'Q','N'): 'hit', (14, 'K','N'): 'hit', (14, 'A','N'): 'hit',

    (15, '2','N'): 'hit', (15, '3','N'): 'hit', (15, '4','N'): 'double', (15, '5','N'): 'double', (15, '6','N'): 'double',
    (15, '7','N'): 'hit', (15, '8','N'): 'hit', (15, '9','N'): 'hit', (15, '10','N'): 'hit', (15, 'J','N'): 'hit', (15, 'Q','N'): 'hit', (15, 'K','N'): 'hit', (15, 'A','N'): 'hit',

    (16, '2','N'): 'hit', (16, '3','N'): 'hit', (16, '4','N'): 'double', (16, '5','N'): 'double', (16, '6','N'): 'double',
    (16, '7','N'): 'hit', (16, '8','N'): 'hit', (16, '9','N'): 'hit', (16, '10','N'): 'hit', (16, 'J','N'): 'hit', (16, 'Q','N'): 'hit', (16, 'K','N'): 'hit', (16, 'A','N'): 'hit',

    (17, '2',1): 'hit/double', (17, '3','N'): 'double', (17, '4','N'): 'double', (17, '5','N'): 'double', (17, '6','N'): 'double',
    (17, '7','N'): 'hit', (17, '8','N'): 'hit', (17, '9','N'): 'hit', (17, '10','N'): 'hit', (17, 'J','N'): 'hit', (17, 'Q','N'): 'hit', (17, 'K','N'): 'hit', (17, 'A','N'): 'hit',

    (18, '2','N'): 'double', (18, '3','N'): 'double', (18, '4','N'): 'double', (18, '5','N'): 'double', (18, '6','N'): 'double',
    (18, '7','N'): 'stand', (18, '8','N'): 'stand', (18, '9','N'): 'hit', (18, '10','N'): 'hit', (18, 'J','N'): 'hit', (18, 'Q','N'): 'hit', (18, 'K','N'): 'hit', (18, 'A','N'): 'hit',

    (19, '2','N'): 'stand', (19, '3','N'): 'stand', (19, '4',3): 'stand/double', (19, '5',1): 'stand/double', (19, '6',0): 'stand/double',
    (19, '7','N'): 'stand', (19, '8','N'): 'stand', (19, '9','N'): 'stand', (19, '10','N'): 'stand', (19, 'J','N'): 'stand', (19, 'Q','N'): 'stand', (19, 'K','N'): 'stand', (19, 'A','N'): 'stand',

    (20, '2','N'): 'stand', (20, '3','N'): 'stand', (20, '4','N'): 'stand', (20, '5','N'): 'stand', (20, '6','N'): 'stand',
    (20, '7','N'): 'stand', (20, '8','N'): 'stand', (20, '9','N'): 'stand', (20, '10','N'): 'stand', (20, 'J','N'): 'stand', (20, 'Q','N'): 'stand', (20, 'K','N'): 'stand', (20, 'A','N'): 'stand',

    (21, '2','N'): 'stand', (21, '3','N'): 'stand', (21, '4','N'): 'stand', (21, '5','N'): 'stand', (21, '6','N'): 'stand',
    (21, '7','N'): 'stand', (21, '8','N'): 'stand', (21, '9','N'): 'stand', (21, '10','N'): 'stand', (21, 'J','N'): 'stand', (21, 'Q','N'): 'stand', (21, 'K','N'): 'stand', (21, 'A','N'): 'stand'

}

true_split_strategy = {
    (2, '2','N'): 'yes', (2, '3','N'): 'yes', (2, '4','N'): 'yes', (2, '5','N'): 'yes', (2, '6','N'): 'yes',
    (2, '7','N'): 'yes', (2, '8','N'): 'no', (2, '9','N'): 'no', (2, '10','N'): 'no', (2, 'J','N'): 'no', (2, 'Q','N'): 'no', (2, 'K','N'): 'no', (2, 'A','N'): 'no',

    (3, '2','N'): 'yes', (3, '3','N'): 'yes', (3, '4','N'): 'yes', (3, '5','N'): 'yes', (3, '6','N'): 'yes',
    (3, '7','N'): 'yes', (3, '8','N'): 'no', (3, '9','N'): 'no', (3, '10','N'): 'no', (3, 'J','N'): 'no', (3, 'Q','N'): 'no', (3, 'K','N'): 'no', (3, 'A','N'): 'no',

    (4, '2','N'): 'no', (4, '3','N'): 'no', (4, '4','N'): 'no', (4, '5','N'): 'yes', (4, '6','N'): 'yes',
    (4, '7','N'): 'no', (4, '8','N'): 'no', (4, '9','N'): 'no', (4, '10','N'): 'no', (4, 'J','N'): 'no', (4, 'Q','N'): 'no', (4, 'K','N'): 'no', (4, 'A','N'): 'no',

    (5, '2','N'): 'no', (5, '3','N'): 'no', (5, '4','N'): 'no', (5, '5','N'): 'no', (5, '6','N'): 'yes',
    (5, '7','N'): 'no', (5, '8','N'): 'no', (5, '9','N'): 'no', (5, '10','N'): 'no', (5, 'J','N'): 'no', (5, 'Q','N'): 'no', (5, 'K','N'): 'no', (5, 'A','N'): 'no',

    (6, '2','N'): 'yes', (6, '3','N'): 'yes', (6, '4','N'): 'yes', (6, '5','N'): 'yes', (6, '6','N'): 'yes',
    (6, '7','N'): 'no', (6, '8','N'): 'no', (6, '9','N'): 'no', (6, '10','N'): 'no', (6, 'J','N'): 'no', (6, 'Q','N'): 'no', (6, 'K','N'): 'no', (6, 'A','N'): 'no',

    (7, '2','N'): 'yes', (7, '3','N'): 'yes', (7, '4','N'): 'yes', (7, '5','N'): 'yes', (7, '6','N'): 'yes',
    (7, '7','N'): 'yes', (7, '8','N'): 'no', (7, '9','N'): 'no', (7, '10','N'): 'no', (7, 'J','N'): 'no', (7, 'Q','N'): 'no', (7, 'K','N'): 'no', (7, 'A','N'): 'no',

    (8, '2','N'): 'yes', (8, '3','N'): 'yes', (8, '4','N'): 'yes', (8, '5','N'): 'yes', (8, '6','N'): 'yes',
    (8, '7','N'): 'yes', (8, '8','N'): 'yes', (8, '9','N'): 'yes', (8, '10','N'): 'yes', (8, 'J','N'): 'yes', (8, 'Q','N'): 'yes', (8, 'K','N'): 'yes', (8, 'A','N'): 'yes',

    (9, '2','N'): 'yes', (9, '3','N'): 'yes', (9, '4','N'): 'yes', (9, '5','N'): 'yes', (9, '6','N'): 'yes',
    (9, '7','N'): 'no', (9, '8','N'): 'yes', (9, '9','N'): 'yes', (9, '10','N'): 'no', (9, 'J','N'): 'no', (9, 'Q','N'): 'no', (9, 'K','N'): 'no', (9, 'A','N'): 'no',

    (10, '2','N'): 'no', (10, '3','N'): 'no', (10, '4',6): 'no/yes', (10, '5',5): 'no/yes', (10, '6',4): 'no/yes',
    (10, '7','N'): 'no', (10, '8','N'): 'no', (10, '9','N'): 'no', (10, '10','N'): 'no', (10, 'J','N'): 'no', (10, 'Q','N'): 'no', (10, 'K','N'): 'no', (10, 'A','N'): 'no',

   (11, '2','N'): 'yes', (11, '3','N'): 'yes', (11, '4','N'): 'yes', (11, '5','N'): 'yes', (11, '6','N'): 'yes',
    (11, '7','N'): 'yes', (11, '8','N'): 'yes', (11, '9','N'): 'yes', (11, '10','N'): 'yes', (11, 'J','N'): 'yes', (11, 'Q','N'): 'yes', (11, 'K','N'): 'yes', (11, 'A','N'): 'yes'
}

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
        true_count = (count / int(len(cardsLeft) / 52))
        true_count = int(true_count)
    except ZeroDivisionError:
        true_count = count
    return true_count


# Reshuffles a new shoe of n decks
def reshuffle(n):
    cardsLeft = []
    for i in range(n):
        cardsLeft.extend(deck)
    random.shuffle(cardsLeft)
    return cardsLeft, 0
            
def checkAction(myAction,hand,true_count):
    if value([hand[0]]) == value([hand[1]]) and len(hand) == 2:
        values, soft = value([hand[0]])
        for ranges in ['N', 4, 5, 6]:
            key = (values, dealer[0][:-1], ranges)
            try:
                split = true_split_strategy[key]
                if ranges != 'N':
                    choice = split.split('/')
                    if ranges <= true_count:
                        split = choice[1]
                    else:
                        split = choice[0]
                break
            except KeyError:
                next
        if split == 'yes':
            return ['split', ('split'==myAction)]
    valuation, soft = value(hand)
    for ranges in ['N',-2, -1, 0, 1, 2, 3, 4, 5, 6]:
        key = (valuation, dealer[0][:-1], ranges)
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
        choice = action.split('/')
        if true_count >= key[2]:
            action = choice[1]
        else:
            action = choice[0]
            
    if (action == 'double' and len(hand) > 2):
            action = 'hit'
            if key in [(18,'2','N'),(18,'3','N'),(18,'4','N'),(18,'5','N'),(18,'6','N'),(19,'6','0')] and soft:
                action = 'stand'

    return [action, (action==myAction)]


# Simulates NPC strategy
def npc(cardsLeft, hand, dealer, count):
    while True:
        valuation, soft = value(hand)

        if valuation > 21:
            return cardsLeft, count, hand

        key = (valuation, dealer[:-1])
        if not soft:
            try:
                action = hard_strategy[key]
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
        elif action == 'double':
            cardsLeft, hand, count = takeCard(cardsLeft, hand, count)
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
    m = 200000  # Starting money
    n = 6       # Number of decks
    return n, m

def generateHand():
    global cards, cardsLeft, dealer, count, players
    players = [[]]
    dealer = []
    cards=[]
    for i in range(p):
        cards.append([])

    # Deal initial cards
    for i in range(2):
        cardsLeft, players[0], count = takeCard(cardsLeft, players[0], count)
        for j in range(p):
            cardsLeft, cards[j], count = takeCard(cardsLeft, cards[j], count)
        cardsLeft, dealer, count = takeCard(cardsLeft, dealer, count)
    for i in range(len(cards)):
        cardsLeft, count,cards[i] = npc(cardsLeft,cards[i],dealer[0],count)


# --- Setup & Globals ---

windowSize = pygame.FULLSCREEN
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0,0), windowSize)
screenSize = (screen.get_size())

# Basic state variables
count = 0
p = 5
newhand = True
cardsLeft = ['0']
numOfDecks = 6

# Card names and image file identifiers
deck = ['AH','AS','AD','AC','2H','2S','2D','2C','3H','3S','3D','3C','4H','4S','4D','4C','5H','5S','5D','5C','6H','6S','6D','6C','7H','7S','7D','7C','8H','8S','8D','8C','9H','9S','9D','9C','10H','10S','10D','10C','JH','JS','JD','JC','QH','QS','QD','QC','KH','KS','KD','KC']
fileName = ['ha','sa','da','ca','h2','s2','d2','c2','h3','s3','d3','c3','h4','s4','d4','c4','h5','s5','d5','c5','h6','s6','d6','c6','h7','s7','d7','c7','h8','s8','d8','c8','h9','s9','d9','c9','h10','s10','d10','c10','hj','sj','dj','cj','hq','sq','dq','cq','hk','sk','dk','ck','back']

# --- Load Images ---

background = pygame.image.load('/Users/sam/Documents/blackjack game/background.png')
doubleActive = pygame.image.load('/Users/sam/Documents/blackjack game/doubleActive.png')
doubleOut = pygame.image.load('/Users/sam/Documents/blackjack game/doubleOut.png')
newHandOut = pygame.image.load('/Users/sam/Documents/blackjack game/newHandOut.png')
newHandActive = pygame.image.load('/Users/sam/Documents/blackjack game/newHandActive.png')
splitActive = pygame.image.load('/Users/sam/Documents/blackjack game/splitActive.png')
splitOut = pygame.image.load('/Users/sam/Documents/blackjack game/splitOut.png')
hitOut = pygame.image.load('/Users/sam/Documents/blackjack game/hitOut.png')
hitActive = pygame.image.load('/Users/sam/Documents/blackjack game/hitActive.png')
standActive = pygame.image.load('/Users/sam/Documents/blackjack game/standActive.png')
standOut = pygame.image.load('/Users/sam/Documents/blackjack game/standOut.png')
countLabel = pygame.image.load('/Users/sam/Documents/blackjack game/countLabel.png')
arrow = pygame.image.load('/Users/sam/Documents/blackjack game/arrow.png')
square = pygame.image.load('/Users/sam/Documents/blackjack game/square.png')

# --- Scale Images ---

square = pygame.transform.scale(square, (numOfDecks*52*0.2+10+screenSize[0]/16,10+screenSize[1]/8))
arrow = pygame.transform.scale(arrow, (screenSize[0]/15,screenSize[1]/10))
countLabel = pygame.transform.scale(countLabel, (screenSize[0]/8,screenSize[1]/15))
doubleActive = pygame.transform.scale(doubleActive, (screenSize[0]/8,screenSize[1]/15))
doubleOut = pygame.transform.scale(doubleOut, (screenSize[0]/8,screenSize[1]/15))
standActive = pygame.transform.scale(standActive, (screenSize[0]/8,screenSize[1]/15))
standOut = pygame.transform.scale(standOut, (screenSize[0]/8,screenSize[1]/15))
hitActive = pygame.transform.scale(hitActive, (screenSize[0]/8,screenSize[1]/15))
hitOut = pygame.transform.scale(hitOut, (screenSize[0]/8,screenSize[1]/15))
splitActive = pygame.transform.scale(splitActive, (screenSize[0]/8,screenSize[1]/15))
splitOut = pygame.transform.scale(splitOut, (screenSize[0]/8,screenSize[1]/15))
newHandActive = pygame.transform.scale(newHandActive, (screenSize[0]/8,screenSize[1]/15))
newHandOut = pygame.transform.scale(newHandOut, (screenSize[0]/8,screenSize[1]/15))
background = pygame.transform.scale(background, screenSize)

# --- Fonts & Button Labels ---

myFont = pygame.font.Font('/Users/sam/Library/CloudStorage/OneDrive-Personal/Documents/University/Photos/Arial Black.ttf', 50)
doubleLabel = doubleActive
newHandLabel = newHandActive
splitLabel = splitActive
hitLabel = hitActive
standLabel = standActive

# --- Game State Flags & Timers ---

imagecards = []
timer = 10000
clicked = 0
id = 0
hitting = False
standing = False
newHands = False
splitting = False
showCount = False

# --- Load and Scale Card Images ---

for i in range(53):
    imagecards.append(pygame.image.load('/Users/sam/Documents/blackjack game/'+ fileName[i] + '.png'))
    imagecards[i] = pygame.transform.scale(imagecards[i], (screenSize[0]/16, screenSize[1]/8))

# --- Main Game Loop ---

done = False
while not done:
    # --- Handle Turn Logic ---

    mouse = pygame.mouse.get_pos()
    
    # New hand setup
    if newhand:
        if len(cardsLeft) < numOfDecks * 52 * 0.2:
            cardsLeft, count = reshuffle(numOfDecks)
        generateHand()
        id = 0
        hitting = False
        standing = False
        newhand = False
        newHands = False
        stands = True
        hits = True
        doubles = True
        dealerCard = 'flipped'
        valuation, soft = value(dealer)
        if valuation == 21:
            standing = True

    # Check for split possibility
    if value([players[id][0]]) == value([players[id][1]]) and len(players[id]) == 2:
        splits = True
    else:
        splits = False

    # Restrict options after hitting
    if hitting:
        doubles = False
        splits = False

    # Auto-stand if over 21
    valuation, soft = value(players[id])
    if standing or valuation >= 21:
        id += 1
        standing = False
        if id == len(players):
            id = 0
            finished = False
            dealerCard = 'unflipped'
            while not finished:
                valuation, soft = value(dealer)
                if valuation < 17 or (soft and valuation < 18):
                    cardsLeft, dealer,count = takeCard(cardsLeft, dealer,count)
                else:
                    finished = True
            newHands = True
            stands = False
            hits = False
            splits = False
            doubles = False

    # --- Update Button Labels ---

    splitLabel = splitActive if splits else splitOut
    hitLabel = hitActive if hits else hitOut
    standLabel = standActive if stands else standOut
    doubleLabel = doubleActive if doubles else doubleOut
    newHandLabel = newHandActive if newHands else newHandOut

    # --- Handle Button Clicks ---

    if newHands and clicked == 2 and mouse[0] >= screenSize[0]*0.86 and mouse[1] >= screenSize[1]*0.5 and mouse[1] < screenSize[1]*0.6:
        newhand = True

    elif splits and clicked == 2 and mouse[0] >= screenSize[0]*0.86 and mouse[1] >= screenSize[1]*0.6 and mouse[1] < screenSize[1]*0.7:
        splitting = True
        timer = 0
        action, answer = checkAction('split',players[id],trueCount(cardsLeft,count))
        players.append([])
        players[-1].append(players[id][0])
        del players[id][0]
        cardsLeft, players[-1], count = takeCard(cardsLeft, players[-1], count)
        cardsLeft, players[id], count = takeCard(cardsLeft, players[id], count)

    elif doubles and clicked == 2 and mouse[0] >= screenSize[0]*0.86 and mouse[1] >= screenSize[1]*0.7 and mouse[1] < screenSize[1]*0.8:
        timer = 0
        action, answer = checkAction('double',players[id],trueCount(cardsLeft,count))
        cardsLeft, players[id], count = takeCard(cardsLeft,players[id],count)
        standing = True

    elif stands and clicked == 2 and mouse[0] >= screenSize[0]*0.86 and mouse[1] >= screenSize[1]*0.8 and mouse[1] < screenSize[1]*0.9:
        standing = True
        action, answer = checkAction('stand',players[id],trueCount(cardsLeft,count))
        timer = 0

    elif hits and clicked == 2 and mouse[0] >= screenSize[0]*0.86 and mouse[1] >= screenSize[1]*0.9:
        timer = 0
        action, answer = checkAction('hit',players[id],trueCount(cardsLeft,count))
        cardsLeft, players[id], count = takeCard(cardsLeft,players[id],count)
        hitting = True

    # Toggle count display
    if clicked == 2 and mouse[0] >= screenSize[0]*0.86 and mouse[1] >= screenSize[1]*0.4 and mouse[1] <= screenSize[1]*0.5:
        showCount = not showCount

    # --- Draw UI Elements ---

    screen.blit(background, (0,0))
    screen.blit(countLabel, (screenSize[0]*0.86,screenSize[1]*0.4))
    screen.blit(doubleLabel, (screenSize[0]*0.86,screenSize[1]*0.7))
    screen.blit(standLabel, (screenSize[0]*0.86,screenSize[1]*0.8))
    screen.blit(hitLabel, (screenSize[0]*0.86,screenSize[1]*0.9))
    screen.blit(newHandLabel, (screenSize[0]*0.86,screenSize[1]*0.5))
    screen.blit(splitLabel, (screenSize[0]*0.86,screenSize[1]*0.6))

    pygame.draw.rect(screen, '#FFFFFF', [screenSize[0]*0.8, screenSize[1]*0.1, screenSize[0]/16, screenSize[1]/8])
    screen.blit(imagecards[52], (screenSize[0]*0.8 + (len(cardsLeft)*0.2),screenSize[1]*0.1))
    screen.blit(arrow, (screenSize[0]/3 + id*screenSize[0]/12,screenSize[1]*0.875))
    screen.blit(square, (screenSize[0]*0.8-5,screenSize[1]*0.1-5))

    if timer < 100:
        if answer:
            resultText = myFont.render('It is correct to '+action+'!', False, "#06FF06")
        else:
            resultText = myFont.render('Wrong, you should '+action+'!', False, "#FF0000")
        screen.blit(resultText, (screenSize[0]/3,screenSize[1]*0.1))

    if showCount:
        true_count = trueCount(cardsLeft,count)
        countText = myFont.render('Count: '+str(count)+ '  True: '+ str(true_count), False, "#FFFFFF")
        screen.blit(countText, (screenSize[0]/20,screenSize[1]*0.9))

    # Draw player hands
    for j in range(p):
        for i in range(len(cards[j])):
            locate = deck.index(cards[j][i])
            x = i*screenSize[0]/15 + screenSize[0]/50
            y = j*screenSize[1]/50 + j*screenSize[1]/8 + screenSize[1]/20
            screen.blit(imagecards[locate], (x,y))

    for j in range(len(players)):
        for i in range(len(players[j])):
            locate = deck.index(players[j][i])
            x = j*screenSize[0]/12 + i*screenSize[0]/70 + screenSize[0]/3
            y = screenSize[1]*0.7-i*screenSize[1]/16
            screen.blit(imagecards[locate], (x,y))

    for i in range(len(dealer)):
        locate = deck.index(dealer[i])
        x = i*screenSize[0]/15 + screenSize[0]*0.4
        y = screenSize[1]*0.2
        screen.blit(imagecards[locate], (x,y))

    if dealerCard == 'flipped':
        screen.blit(imagecards[52], (screenSize[0]*0.466666666, screenSize[1]*0.2))

    # Update display
    pygame.display.flip()

    # Reset click state
    if clicked == 2:
        clicked = 0

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN or clicked == 1:
            clicked = 1
            if event.type != pygame.MOUSEBUTTONDOWN:
                clicked = 2

    timer += 1
    clock.tick(30)

pygame.quit()
