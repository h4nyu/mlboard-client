from mlboard_client import Writer
import pytest
from datetime import datetime, timezone
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


@pytest.mark.parametrize("ts", [
    (None),
    (datetime.now(timezone.utc))
])
def test_add_scalars(writer: Writer, ts) -> None:
    writer.add_scalars({
        f"{k}": 0.1
        for k
        in range(100)
    }, ts=ts)
