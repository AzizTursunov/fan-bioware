import os
from csv import DictReader
from django.core.management import BaseCommand
from django.core.files.uploadedfile import SimpleUploadedFile
from bioware.models import Studio
from fanbioware.settings import DATA_DIR


class Command(BaseCommand):
    """Загрузка данных в таблицу Studio.
    Можно указать путь к csv-файлу. Если путь не указан,
    загрузка выполняется из DEFAULT_FILE_PATH.
    """

    DEFAULT_FILE_PATH = os.path.join(DATA_DIR, 'studios.csv')
    IMAGE_DIR = os.path.join(DATA_DIR, 'cards')
    help = 'Загружает данные из csv-файла в таблицу Studio.'

    def add_arguments(self, parser):
        parser.add_argument(
            'file_path', type=str, nargs='?', default=self.DEFAULT_FILE_PATH
        )

    def handle(self, *args, **options):
        file_path = options['file_path']
        with open(file_path, encoding='utf-8') as csv_file:
            reader = DictReader(csv_file)
            for row in reader:
                image_path = os.path.join(self.IMAGE_DIR, row['image'])
                with open(image_path, 'rb') as img_file:
                    image = img_file.read()
                uploaded = SimpleUploadedFile(
                    name=row['image'],
                    content=image,
                    content_type='image/jpg'
                )
                _, created = Studio.objects.get_or_create(
                    id=row['id'],
                    location=row['location'],
                    address1=row['address1'],
                    address2=row['address2'],
                    zip_code=row['zip_code'],
                    phone=row['phone'],
                    email=row['email'],
                    description=row['description'],
                    image=uploaded,
                )
        self.stdout.write(
            self.style.SUCCESS(
                f'Данные из {file_path} успешно загружены.'
            )
        )
