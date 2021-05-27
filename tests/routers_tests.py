import unittest
from tests.base import BaseTestCase


class RoutesTests(BaseTestCase):
    # Ensures route '/' renders notifications view
    def test_default_route_should_render_default_view(self):
        # act
        self.client.get('/')

        # assert
        self.assert_template_used('notifications.html')


if __name__ == '__main__':
    unittest.main()
