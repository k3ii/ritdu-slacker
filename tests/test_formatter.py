# Import from your actual file
from ritdu_slacker.formatter import MessageFormatter
import pytest
import json


@pytest.fixture
def formatter():
    return MessageFormatter()


def test_init_messages(formatter):
    category = "INFO"
    title = "Title"
    details = "Details"
    code = True
    expected_blocks = {
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": f":information_source: {title}",
                },
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"```\n{details}\n```",
                },
            },
        ]
    }

    assert formatter.init_messages(category, title, details, code) == expected_blocks

    # Test with invalid category
    category = "INVALID"
    expected_blocks["blocks"][0]["text"]["text"] = ":question: Title"
    assert formatter.init_messages(category, title, details, code) == expected_blocks

    # Test without code formatting
    code = False
    expected_blocks["blocks"][1]["text"]["text"] = details
    assert formatter.init_messages(category, title, details, code) == expected_blocks


def test_thread_messages(formatter):
    details = "Details"
    code = True
    expected_blocks = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"```\n{details}\n```",
                },
            },
        ]
    }

    assert formatter.thread_messages(details, code) == expected_blocks

    # Test without code formatting
    code = False
    expected_blocks["blocks"][0]["text"]["text"] = details
    assert formatter.thread_messages(details, code) == expected_blocks

    # Test with list details
    details = ["Item 1", "Item 2"]
    expected_blocks["blocks"][0]["text"]["text"] = json.dumps(details, indent=2)
    assert formatter.thread_messages(details, code) == expected_blocks
