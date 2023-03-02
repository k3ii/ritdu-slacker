import responses

from pyfakefs.fake_filesystem_unittest import Patcher
from pytest import fixture

from ritdu_slacker.cli import SlackMessageCLI


@fixture
def mocked_responses():
    with responses.RequestsMock() as rsps:
        yield rsps


@fixture
def cli():
    yield SlackMessageCLI()


@fixture
def filesystem():
    with Patcher(allow_root_user=False) as patcher:
        yield patcher.fs
