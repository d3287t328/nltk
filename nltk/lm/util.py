# Natural Language Toolkit
#
# Copyright (C) 2001-2023 NLTK Project
# Author: Ilia Kurenkov <ilia.kurenkov@gmail.com>
# URL: <https://www.nltk.org/>
# For license information, see LICENSE.TXT
"""Language Model Utilities"""

from math import log

NEG_INF = float("-inf")
POS_INF = float("inf")


def log_base2(score):
    """Convenience function for computing logarithms with base 2."""
    return NEG_INF if score == 0.0 else log(score, 2)
