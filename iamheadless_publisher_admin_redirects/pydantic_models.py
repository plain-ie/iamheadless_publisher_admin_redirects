import datetime
import re
from typing import List, Optional

from django.core.exceptions import ValidationError
from django.template.loader import render_to_string

from iamheadless_publisher_admin.pydantic_models import BaseItemPydanticModel, BaseItemDataPydanticModel, BaseItemContentsPydanticModel

from .conf import settings
from . import forms


class RedirectDataPydanticModel(BaseItemDataPydanticModel):
    source_url: str
    destination_url: str


class RedirectPydanticModel(BaseItemPydanticModel):

    _content_model = None
    _data_model = RedirectDataPydanticModel
    _display_name_plural = 'redirects'
    _display_name_singular = 'redirect'
    _item_type = settings.ITEM_TYPE
    _project_admin_required = True
    _tenant_required = False

    data: RedirectDataPydanticModel

    @property
    def TITLE(self):
        data = self.dict()
        return data['data']['source_url']

    @property
    def EDIT_URL(self):

        _data = self.DATA

        project_id = _data.get('project', None)
        item_id = _data.get('id', None)

        return reverse(
            settings.URLNAME_RETRIEVE_UPDATE_ITEM,
            kwargs={
                'project_id': project_id,
                'item_id': item_id
            }
        )

    #

    @classmethod
    def viewsets(cls):
        return [
            f'{settings.APP_NAME}.viewsets.RedirectCreateViewSet',
            f'{settings.APP_NAME}.viewsets.RedirectDeleteViewSet',
            f'{settings.APP_NAME}.viewsets.RedirectRetrieveUpdateViewSet',
        ]

    @classmethod
    def get_item_type(cls, data):
        return data['item_type']

    @classmethod
    def render_form(
            cls,
            request,
            initial_data
            ):

        initial_item = initial_data.get('data', {})

        form = forms.RedirectForm(initial=initial_item)

        if request.method == 'POST':
            form = forms.RedirectForm(request.POST, initial=initial_item)

        return render_to_string(
            'iamheadless_publisher_admin_redirects/form.html',
            context={
                'form': form,
            }
        )

    @classmethod
    def validate_form(
            cls,
            request,
            initial_data
            ):

        data = {}
        if request.method == 'POST':
            data = request.POST

        initial_item = initial_data.get('data', {})

        form = forms.RedirectForm(request.POST, initial=initial_item)

        valid = []

        valid.append(form.is_valid())

        if False in valid:
            raise ValidationError('Form is invalid')

        validated_data =  {
            'data': form.cleaned_data,
        }

        return validated_data

    @classmethod
    def pre_create(cls, request, data):

        source_url = data['data']['source_url']

        indexes = {
            'text': [{
                'language': 'null',
                'field_name': 'source_url',
                'value': source_url,
            }]
        }

        data['indexes'] = indexes

        return data

    @classmethod
    def pre_update(cls, request, data):
        return cls.pre_create(request, data)
