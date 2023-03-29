from django.urls import reverse, resolve
from blog.views import api_get_post
import pytest

class TestUrls():
    
    def test_api_posts_url_resolves(self):
        # otrzymujemy url o name='api_posts'
        url = reverse('api_posts')
        # sprawdzamy czy podanym url jest widok, który tam powinien być.
        assert resolve(url).func == api_get_post