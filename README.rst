django-ticket-36408
===================

Reproduction for `Ticket #36408 <https://code.djangoproject.com/ticket/36408>`__.

Setup:

.. code-block:: console

    $ python -m venv .venv
    $ source .venv/bin/activate
    $ docker compose up -d
    $ pip install psycopg[binary]==3.2.9 django==5.2.1  # or -e /path/to/django
    $ ./manage.py migrate

Then:

.. code-block:: console

    $ python t.py
    Traceback (most recent call last):
      File "/.../t.py", line 15, in <module>
        Chapter.objects.annotate(
        ~~~~~~~~~~~~~~~~~~~~~~~~^
            ids=ArrayAgg(
            ^^^^^^^^^^^^^
        ...<2 lines>...
            )
            ^
        ).values("ids")[:1]
        ^
      File "/.../django/db/models/manager.py", line 87, in manager_method
        return getattr(self.get_queryset(), name)(*args, **kwargs)
               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
      File "/.../django/db/models/query.py", line 1647, in annotate
        return self._annotate(args, kwargs, select=True)
               ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/.../django/db/models/query.py", line 1699, in _annotate
        clone.query.add_annotation(
        ~~~~~~~~~~~~~~~~~~~~~~~~~~^
            annotation,
            ^^^^^^^^^^^
            alias,
            ^^^^^^
            select=select,
            ^^^^^^^^^^^^^^
        )
        ^
      File "/.../django/db/models/sql/query.py", line 1218, in add_annotation
        annotation = annotation.resolve_expression(self, allow_joins=True, reuse=None)
      File "/.../django/contrib/postgres/aggregates/mixins.py", line 33, in resolve_expression
        return super().resolve_expression(*args, **kwargs)
               ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
      File "/.../django/db/models/aggregates.py", line 63, in resolve_expression
        c = super().resolve_expression(query, allow_joins, reuse, summarize)
      File "/.../django/db/models/expressions.py", line 300, in resolve_expression
        expr.resolve_expression(query, allow_joins, reuse, summarize)
        ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/.../django/db/models/expressions.py", line 300, in resolve_expression
        expr.resolve_expression(query, allow_joins, reuse, summarize)
        ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/.../django/db/models/expressions.py", line 941, in resolve_expression
        col = super().resolve_expression(*args, **kwargs)
      File "/.../django/db/models/expressions.py", line 902, in resolve_expression
        return query.resolve_ref(self.name, allow_joins, reuse, summarize)
               ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/.../django/db/models/sql/query.py", line 2049, in resolve_ref
        join_info = self.setup_joins(
            field_list, self.get_meta(), self.get_initial_alias(), can_reuse=reuse
        )
      File "/.../django/db/models/sql/query.py", line 1900, in setup_joins
        path, final_field, targets, rest = self.names_to_path(
                                           ~~~~~~~~~~~~~~~~~~^
            names[:pivot],
            ^^^^^^^^^^^^^^
        ...<2 lines>...
            fail_on_missing=True,
            ^^^^^^^^^^^^^^^^^^^^^
        )
        ^
      File "/.../django/db/models/sql/query.py", line 1805, in names_to_path
        raise FieldError(
        ...<2 lines>...
        )
    django.core.exceptions.FieldError: Cannot resolve keyword 'position' into field. Choices are: book, book_id, id
