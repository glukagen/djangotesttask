from django.core.management.base import BaseCommand, CommandError
from django.db.models.loading import get_models


class Command(BaseCommand):
    def handle(self, *args, **options):
        return "Project models:\n%s" % \
         "\n".join(["%s - %s" % (m._meta.object_name, m.objects.count())
                         for m in get_models()])
