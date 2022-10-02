import os
import sys
sys.path.append('/opt/bitnami/projects/luca_roche_coach')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/apps/django/django_projects/luca_roche_coach/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "luca_roche_coach.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()