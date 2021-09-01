from celle import Celle
from spillebrett import Spillebrett
import random

spillebrett = Spillebrett(3, 3)
#spillebrett.tegnBrett()
spillebrett._generer()

print('*' * 20)

print(spillebrett.brett)
spillebrett.oppdatering()

