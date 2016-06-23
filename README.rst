dataporten-auth
===============

Dataporten_ is an authentication, authorization and API platform
for higher and lower education and research in Norway. Dataporten
offers authentication of users to applications using OAuth 2.0 and
the OpenID Connect.

Dataporten-auth is a client for dataporten that depends on
python-social-auth_.

Installation
------------

Install with ``pip`` or by downloading the source and running
``setup.py``.

Usage
-----

There needs to exist an entry for your site/app at dataporten. Log
in to `dataporten's dashboard`_ and create an application.

You'll need to set the client id and client secret in the
settings of your app/site, while the application at dataporten
will need one or more redirect uris.

Both the name of the settings and the redirect uris depend on the
plugins used. Add at least one of the plugins below. See
`python-social-auth's documentation`_ for how.

The redirect uri is of the form ``<type>://<domainpath>/<suffix>/``,
where ``<type>`` is one of ``http`` or ``https``, ``<domainpath>`` is
the domain name of your site and an optional path, and the ``<suffix>`` is
plugin-dependent. See the examples.

You can have several redirect-uris, and you will be needing at least
one per plugin used.

dataporten.psa.DataportenOauth2
...............................

Plugin name
    ``dataporten.psa.DataportenOauth2``

Settings
    Client id: ``SOCIAL_AUTH_DATAPORTEN_KEY``

    Client secret: ``SOCIAL_AUTH_DATAPORTEN_SECRET``

Scopes needed
    ``userid`` and ``profile``, this is the default.

Username generated:
    Unique, alphanumeric string. You might want to let users
    change this generated username. The plugin only cares that a
    username exists and won't change the username back.

Redirect-uri ends with
    /complete/dataporten/

Example redirect uri:
    http://127.0.0.1/complete/dataporten/

dataporten.psa.DataportenEmailOauth2
....................................

Plugin name
    ``dataporten.psa.DataportenEmailOauth2``

Settings
    Client id: ``SOCIAL_AUTH_DATAPORTEN_EMAIL_KEY``

    Client secret: ``SOCIAL_AUTH_DATAPORTEN_EMAIL_SECRET``

Scopes needed
    ``email``, this must be explicitly allowed in the dashboard.

Username generated:
    From email-address

Redirect-uri ends with
    /complete/dataporten_email/

Example redirect uri:
    https://supersites.exmaple.net/mysite/complete/dataporten_email/

dataporten.psa.DataportenFeideOauth2
....................................

Plugin name
    ``dataporten.psa.DataportenEmailOauth2``

Settings
    Client id: ``SOCIAL_AUTH_DATAPORTEN_FEIDE_KEY``

    Client secret: ``SOCIAL_AUTH_DATAPORTEN_FEIDE_SECRET``

Scopes needed
    ``userid-feide``, this must be explicitly allowed in the dashboard.

Username generated:
    From the Feide attribute ``eduPersonPrincipalName``, which looks
    like an email address.

Redirect-uri ends with
    /complete/dataporten_feide/

Example redirect uri:
    https://example.com/cheatsheet/complete/dataporten_feide/

Demo
----

1. Get the source code
2. Install dependencies: ``pip install -r requirements/demo.txt``
3. Make an application at dataporten
4. Edit the settings-file to set ``SOCIAL_AUTH_DATAPORTEN_KEY`` and ``SOCIAL_AUTH_DATAPORTEN_SECRET``
5. Set three redirect-uris, all starting with ``http://127.0.0.1:8000``
6. Run ``python mange.py runserver``
7. Visit http://127.0.0.1:8000 in a fresh browser. Log out doesn't work (yet),
   so to reset, delete the file ``db.sqlite3`` and run ``python mange.py runserver`` again

Optionally, you can add other python-social-auth plugins as well.

.. _Dataporten: https://docs.dataporten.no/
.. _python-social-auth: http://psa.matiasaguirre.net/docs/
.. _`dataporten's dashboard`: https://dashboard.dataporten.no/
.. _python-social-auth's documentation: http://psa.matiasaguirre.net/docs/configuration/



:Version: 0.1
