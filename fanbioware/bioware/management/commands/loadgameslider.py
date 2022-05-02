import os
from csv import DictReader
from django.core.management import BaseCommand
from django.core.files.uploadedfile import SimpleUploadedFile
from bioware.models import GameSliderImage
from fanbioware.settings import DATA_DIR


class Command(BaseCommand):
    """Загрузка данных в таблицу GameSliderImage.
    Можно указать путь к csv-файлу. Если путь не указан,
    загрузка выполняется из DEFAULT_FILE_PATH.
    """

    DEFAULT_FILE_PATH = os.path.join(DATA_DIR, 'gameslider.csv')
    IMAGE_DIR = os.path.join(DATA_DIR, 'sliders')
    help = 'Загружает данные из csv-файла в таблицу GameSliderImage.'

    def add_arguments(self, parser):
        parser.add_argument(
            'file_path', type=str, nargs='?', default=self.DEFAULT_FILE_PATH
        )

    def handle(self, *args, **options):
        file_path = options['file_path']
        with open(file_path) as csv_file:
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
                _, created = GameSliderImage.objects.get_or_create(
                    id=row['id'],
                    game_id=row['game_id'],
                    image=uploaded,
                )
        self.stdout.write(
            self.style.SUCCESS(
                f'Данные из {file_path} успешно загружены.'
            )
        )
