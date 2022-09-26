import pytest

from django.urls import reverse


class TestMainappSmoke:

    @pytest.mark.parametrize('name ,code', [
        ('mainapp:get-status', 200),
        ('mainapp:post-message', 200),
            ])
    def mainapp_test(self, client, name, code):
        assert client.get(reverse(name)).status_code == code
