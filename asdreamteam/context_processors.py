from django.conf import settings


def site_settings(request):
    return {
        "SITE_NAME": settings.SITE_NAME,
        "SITE_TAGLINE": settings.SITE_TAGLINE,
        "DEVELOPER_NAME": settings.DEVELOPER_NAME,
        "DEVELOPER_URL": settings.DEVELOPER_URL,
    }


def menu_items_context(request):
    menu_items = [
        {'label': 'Accueil', 'url': 'home', 'page': 'home'},
        # {'label': 'Actualités', 'url': 'news', 'page': 'news'},
        {
            'label': 'Équipe',
            'dropdown': True,
            'items': [
                {'label': 'Présentation', 'url': 'presentation', 'page': 'presentation'},
                {'label': 'Nos activités', 'url': 'activities', 'page': 'activities'},
                {'label': 'Membres', 'url': 'members', 'page': 'members'},
                {'label': 'Sponsors', 'url': 'sponsors', 'page': 'sponsors'},
            ]
        },
        {'label': 'Galerie', 'url': 'gallery', 'page': 'gallery'},
        {'label': 'À propos', 'url': 'about', 'page': 'about'},
        {'label': 'Contact', 'url': 'contact', 'page': 'contact'},
    ]
    
    return {'menu_items': menu_items}