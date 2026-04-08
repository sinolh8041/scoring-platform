from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_default_admin(sender, **kwargs):
    from django.contrib.auth.models import User
    try:
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    except Exception:
        pass

class ScoringAppConfig(AppConfig):
    name = 'scoring_app'

    def ready(self):
        post_migrate.connect(create_default_admin, sender=self)
