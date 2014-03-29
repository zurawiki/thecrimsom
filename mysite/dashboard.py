"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'mysite.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class MainDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # append a group for "Contracts"
        self.children.append(modules.AppList(
            _('Advertising Contracts'),
            column=1,
            collapsible=False,
            models=('contracts.*',),
        )
        )

        # append a group for "Administration" & "Applications"
        self.children.append(modules.Group(
            _('Advanced Settings'),
            column=2,
            collapsible=True,
            children=[
                modules.AppList(
                    _('Accounts'),
                    column=1,
                    css_classes=('collapse closed',),
                    models=('account.*', 'django.contrib.auth.*', 'mysite.*'),
                ),
                modules.AppList(
                    _('Administration'),
                    column=1,
                    collapsible=False,
                    exclude=('account.*', 'django.contrib.auth.*', 'mysite.*', 'contracts.*'),
                ),
            ]
        ))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Media Management'),
            column=3,
            children=[
                {
                    'title': _('File Browser'),
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                },
            ]
        ))


        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))


