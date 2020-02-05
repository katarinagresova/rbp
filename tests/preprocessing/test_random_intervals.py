import pytest
import pandas as pd
from rbp.preprocessing import random_intervals


def test_gen_random_intervals():
    df = random_intervals.gen_random_intervals(
        sample_size=10, interval_size=100, reference='hg19'
    )
    assert df.shape == (10, 6)
    df['mean'] = df.end - df.start
    assert df.mean == 100
