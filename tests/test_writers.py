from mlboard_client.writers import Writer
from random import random
import pytest
from datetime import datetime
from logging import getLogger, StreamHandler, Formatter, DEBUG


@pytest.fixture
def writer() -> Writer:
    logger = getLogger("LogTest")
    logger.setLevel(DEBUG)
    stream_handler = StreamHandler()
    stream_handler.setLevel(DEBUG)
    handler_format = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(handler_format)
    logger.addHandler(stream_handler)
    return Writer(
        'http://api:5000/',
        'test0',
        {
            'p0': 12,
            'p1': {
                'p3': 'fasdfa'
            },
        },
        logger=logger,
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
