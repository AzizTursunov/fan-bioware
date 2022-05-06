import os
from django.urls import reverse
from django.conf import settings

NEWS_ON_PAGE = 4

BIOWARE_URL_VS_TEMPLATE = {
    '/': 'bioware/index.html',
    '/about/': 'bioware/about.html',
    '/games/': 'bioware/game_list.html',
    '/games/mass-effect/': 'bioware/mass-effect.html',
    '/careers/': 'bioware/careers.html',
    '/contacts/': 'bioware/contacts.html'
}

BIOWARE_REVERSE_URL_VS_TEMPLATE = {
    reverse('bioware:index'): 'bioware/index.html',
    reverse('bioware:about'): 'bioware/about.html',
    reverse('bioware:game_list'): 'bioware/game_list.html',
    reverse(
        'bioware:game_detail', args=('mass-effect',)
        ): 'bioware/mass-effect.html',
    reverse('bioware:careers'): 'bioware/careers.html',
    reverse('bioware:contacts'): 'bioware/contacts.html'
}


def run_field_parameter_test(
        instance, self_,
        field_and_parametr_value,
        parameter_name):
    """Checking the parameter value for all model objects."""
    for field, expected_value in field_and_parametr_value.items():
        with self_.subTest(field=field):
            parameter_real_value = getattr(
                instance._meta.get_field(field), parameter_name
            )
            self_.assertEqual(parameter_real_value, expected_value)


'''def run_max_field_len_test(instance, self_, field_and_max_len):
    """Checking maximum length of the model fields."""
    for field, expected_max_len in field_and_max_len.items():
        with self_.subTest(field=field):
            field_real_max_len = instance._meta.get_field(field).max_length
            self_.assertEqual(field_real_max_len, expected_max_len)'''


class TestVerboseNameMixin:
    """Mixin for checking verbose_name."""
    def run_verbose_name_test(self, instance):
        """Checking vebose_name method."""
        run_field_parameter_test(
            instance, self, self.field_and_verbose_name, 'verbose_name'
        )


class TestHelpTextMixin:
    """Mixin for checking help_text."""
    def run_help_text_test(self, instance):
        """Checking help_text method."""
        run_field_parameter_test(
            instance, self, self.field_and_help_text, 'help_text'
        )


class TestFiedlMaxLengthMixin:
    """Mixin for checking max_length of the model fields."""
    def run_fields_max_len_test(self, instance):
        """Checking max_length of the model fields."""
        run_field_parameter_test(
            instance, self, self.field_and_max_len, 'max_length'
        )


def create_test_template(slug, template_dir=settings.TEMPLATES_DIR):
    file_path = os.path.join(
        template_dir,
        os.path.join(
            'bioware',
            f'{slug}.html'
        )
    )
    open(file_path, 'w').close()
    return file_path
