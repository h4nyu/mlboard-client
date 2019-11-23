from mlboard_client.writers import Writer
from random import random
import pytest
from datetime import datetime


@pytest.fixture
def writer() -> Writer:
    return Writer(
        'http://api:5000/',
        'test0',
        {
            'p0': 12,
            'p1': {
                'p3': 'fasdfa'
            },
        }
    )


def test_add_scalar(writer: Writer) -> None:
    writer.add_scalar('aaa/test', 1)


@pytest.mark.parametrize("ts", [
    (None),
    (datetime.utcnow())
])
def test_add_scalars(writer: Writer, ts) -> None:
    writer.add_scalars({
        'aaa': random(),
        'bbb': random(),
        'ccc': random(),
    }, ts=ts)
