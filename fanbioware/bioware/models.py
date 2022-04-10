from multiselectfield import MultiSelectField
from django.db import models


class Game(models.Model):
    class Platforms(models.TextChoices):
        XBOX_ONE = 'XB_ONE', 'Xbox One Series'
        XBOX_360 = 'XB_360', 'Xbox 360 Series'
        Windows = 'PC', 'Windows PC'
        PLAYSTATION_3 = 'PS_3', 'PlayStation 3'
        PLAYSTATION_4 = 'PS_4', 'PlayStation 4'
        PLAYSTATION_5 = 'PS_5', 'PlayStation 5'

    class Genres(models.TextChoices):
        ACTION = 'AC', 'Action'
        ADVENTURE = 'ADV', 'Adventure'
        FIGHTING = 'F', 'Fighting'
        PLATFORM = 'P', 'Platform'
        RPG = 'RPG', 'RPG'
        SHOOTER = 'SH', 'Shooter'
        SIMULATION = 'SIM', 'Simulation'
        STRATEGY = 'STR', 'Strategy'

    title = models.CharField(
        max_length=255,
        verbose_name='Game',
        help_text='Enter the name of the game',
    )
    slug = models.SlugField(unique=True, verbose_name='URL')
    description = models.CharField(
        max_length=650,
        verbose_name='Description',
        help_text='Enter a description of the game'
    )
    image = models.ImageField(
        verbose_name='Cover',
        help_text='Attach the cover of the game',
        upload_to='bioware/games/',
        blank=False
    )
    rel_date = models.DateField(
        verbose_name='Release date',
        help_text='Enter the release date'
    )
    platforms = MultiSelectField(
        verbose_name='Platforms',
        help_text='Select the available platforms',
        choices=Platforms.choices,
        default=Platforms.XBOX_ONE,
    )
    genre = MultiSelectField(
        verbose_name='Genre',
        help_text='Select the game genre',
        choices=Genres.choices,
        default=Genres.RPG
    )
    is_online = models.BooleanField(default=True)
    is_released = models.BooleanField(default=False)


class News(models.Model):
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, null=True,
        related_name='news',
        verbose_name='Game',
        help_text='Choose the game',
    )
    title = models.CharField(
        max_length=45,
        verbose_name='Title',
        help_text='Enter a title of the news'
    )
    pub_date = models.DateField(auto_now=True)
    intro = models.CharField(
        max_length=90,
        verbose_name='Intro',
        help_text='Enter a short intro of the news',
    )
    text = models.TextField(
        verbose_name='Text',
        help_text='Enter the news text'
    )
    image = models.ImageField(
        verbose_name='Cover',
        help_text='Attach the cover of the news',
        upload_to='bioware/news/',
    )
    is_publicated = models.BooleanField(default=False)

    class Meta:
        ordering = ['-pub_date']


class Opening(models.Model):
    class EmploymentType(models.TextChoices):
        FULL_TIME = 'FT', 'Full-Time'
        PART_TIME = 'PT', 'Part-Time'
        TEMPORARY = 'T', 'Temporary'

    studio = models.ForeignKey(
        'Studio', on_delete=models.CASCADE,
        related_name='openings',
        verbose_name='Studio',
        help_text='Choose the studio'
    )
    team = models.CharField(
        max_length=255,
        verbose_name='Team',
        help_text='Enter the role'
    )
    role = models.CharField(
        max_length=255,
        verbose_name='Role',
        help_text='Enter the role'
    )
    description = models.TextField(
        verbose_name='Description',
        help_text='Enter a description of the opening'
    )
    emp_type = MultiSelectField(
        verbose_name='Type of employment',
        help_text='Choose the type of employment',
        choices=EmploymentType.choices,
        default=EmploymentType.FULL_TIME
    )
    remote = models.BooleanField(
        verbose_name='Remote',
        help_text='Remote is accessible',
        default=True
    )
    responsibilities = models.TextField(
        verbose_name='Responsibilities',
        help_text='Describe the responsibilities separated by semicolons'
    )
    qualifications = models.TextField(
        verbose_name='Qualifications',
        help_text='Describe the responsibilities separated by semicolons'
    )
    perks = models.TextField(
        verbose_name='Perks',
        help_text='Describe the perks separated by semicolons'
    )


class Studio(models.Model):
    location = models.CharField(
        max_length=255,
        verbose_name='Location',
        help_text='Enter the name of the city and country separated by commas'
    )
    address1 = models.CharField(
        max_length=255,
        verbose_name='Address',
        help_text='Enter the street name and building number',
    )
    address2 = models.CharField(
        max_length=255,
        verbose_name='City',
        help_text='Enter the city',
    )
    zip_code = models.CharField(
        max_length=255,
        verbose_name='Zip Code',
        help_text='Enter the zip code'
    )
    phone = models.CharField(
        max_length=20,
        verbose_name='Phone',
        help_text='Enter the phone number'
    )
    email = models.EmailField(
        verbose_name='Email',
        help_text='Enter e-mail',
    )
    description = models.TextField(
        verbose_name='Descrpition',
        help_text='Enter a description of the studio'
    )
    image = models.ImageField(
        verbose_name='Image',
        help_text='Attach the cover of the studio',
        upload_to='bioware/studio/'
    )
