from mlboard_client.writers import Writer
from random import random
import pytest


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


def test_add_scalars(writer: Writer) -> None:
    writer.add_scalars({
        'aaa': random(),
        'bbb': random(),
        'ccc': random(),
    })

