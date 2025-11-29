from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    """
    Sitemap pour les pages statiques du site.
    """
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        """
        Retourne la liste des noms de vues statiques.
        """
        return ['index', 'about', 'services', 'contact']

    def location(self, item):
        """
        Retourne l'URL de chaque page.
        """
        return reverse(item)

