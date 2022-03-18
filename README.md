# iamheadless_publisher_admin_redirects

App to render redirects item type in `iamheadless_publisher_admin` frontend.

## Installation

Requires `iamheadless_publisher_admin`

1. install package
2. add `iamheadless_publisher_admin_redirects` to `INSTALLED_APPS` in `settings.py`
3. add viewsets to `IAMHEADLESS_PUBLISHER_ADMIN_VIEWSET_LIST` in `settings.py`
```
[
    'iamheadless_publisher_admin_redirects.viewsets.RedirectCreateViewSet',
    'iamheadless_publisher_admin_redirects.viewsets.RedirectDeleteViewSet',
    'iamheadless_publisher_admin_redirects.viewsets.RedirectRetrieveUpdateViewSet',
]
```
