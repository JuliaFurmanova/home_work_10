import json
import os

import allure
from allure import attachment_type


def test_attachments():
    allure.attach.file(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'resources/Octopus.png')), name="png", attachment_type=attachment_type.PNG)
    allure.attach("<h1>Hello, world</h1>", name="Html", attachment_type=attachment_type.HTML)
    allure.attach(json.dumps({"first": 1, "second": 2}), name="Json", attachment_type=attachment_type.JSON)