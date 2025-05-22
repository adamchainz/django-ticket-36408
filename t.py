import os

os.environ["DJANGO_SETTINGS_MODULE"] = "example.settings"
import django

django.setup()

from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import OuterRef, Subquery

from example.models import Book, Chapter

Book.objects.annotate(
    chapter_ids=Subquery(
        Chapter.objects.annotate(
            ids=ArrayAgg(
                "id",
                order_by=[OuterRef("position")],
            )
        ).values("ids")[:1]
    )
)
