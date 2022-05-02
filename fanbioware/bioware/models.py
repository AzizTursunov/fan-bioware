from datetime import date
from multiselectfield import MultiSelectField
from django.db import models


class Game(models.Model):
    """"Creating the Game model."""

    class Platforms(models.TextChoices):
        """Creating platform choice to Game model."""

        XBOX_ONE = 'Xbox One', 'Xbox One Series'
        XBOX_360 = 'Xbox 360', 'Xbox 360 Series'
        Windows = 'PC', 'Windows PC'
        PLAYSTATION_3 = 'PS3', 'PlayStation 3'
        PLAYSTATION_4 = 'PS4', 'PlayStation 4'
        PLAYSTATION_5 = 'PS5', 'PlayStation 5'

    class Genres(models.TextChoices):
        """Creating genre choise to Game model."""

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
        verbose_name='Name of the game',
        help_text='Enter the name of the game',
    )
    slug = models.SlugField(unique=True, verbose_name='URL')
    intro = models.CharField(
        max_length=650,
        verbose_name='Intro',
        help_text='Enter the game intro'
    )
    description = models.TextField(
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
    origin_url = models.URLField(
        blank=True, null=True,
        verbose_name='Origin',
        help_text='Enter the link to the Origin'
    )
    ps_url = models.URLField(
        blank=True, null=True,
        verbose_name='PS',
        help_text='Enter the link to PS Store'
    )
    xbox_url = models.URLField(
        blank=True, null=True,
        verbose_name='XboX',
        help_text='Enter the link to the XboX Store'
    )
    steam_url = models.URLField(
        blank=True, null=True,
        verbose_name='Steam',
        help_text='Enter the link to the Steam'
    )

    is_released = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
        ordering = ['id']

    def __str__(self):
        """Return the title of the Game."""
        return self.title

    @property
    def platforms_available(self):
        """Returns available platforms."""
        platforms = []
        if 'PC' in self.platforms:
            pc_stores = []
            store_vs_url = {'Origin': self.origin_url, 'Steam': self.steam_url}
            for store, url in store_vs_url.items():
                if url:
                    pc_stores.append(store)
            pc_text = 'PC ({})'.format(', '.join(pc_stores))
            platforms.append(pc_text)
        console_platforms = [
            platform for platform in self.platforms if platform != 'PC'
        ]
        if console_platforms:
            console_text = 'Console ({}, compatible with next gen)'.format(
                ', '.join(console_platforms)
            )
            platforms.append(console_text)
        return platforms


class News(models.Model):
    """Creating the News model."""

    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, blank=True,
        null=True, related_name='news',
        verbose_name='Game',
        help_text='Choose the game',
    )
    title = models.CharField(
        max_length=45,
        verbose_name='Title',
        help_text='Enter a title of the news'
    )
    pub_date = models.DateField(default=date.today())
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
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        """Return the title of the News."""
        return self.title


class Opening(models.Model):
    """Creating the Opening model."""

    class EmploymentType(models.TextChoices):
        """Creating employment type choice to the Opening model."""
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
        help_text='Enter the team'
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

    class Meta:
        verbose_name = 'Job opening'
        verbose_name_plural = 'Job openings'

    def __str__(self):
        """Return the role of the Opening."""
        return self.role


class Studio(models.Model):
    """Creating the Studio model."""

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
        verbose_name='Description',
        help_text='Enter a description of the studio'
    )
    image = models.ImageField(
        verbose_name='Cover',
        help_text='Attach the cover of the studio',
        upload_to='bioware/studio/'
    )

    class Meta:
        verbose_name = 'Studio'
        verbose_name_plural = 'Studois'

    def __str__(self):
        """Return the location of the Game."""
        return self.location


class GameSliderImage(models.Model):
    game = models.ForeignKey(
        Game,
        related_name='Slide',
        null=True, blank=None,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        verbose_name='Slide',
        help_text='Attach the slide',
        upload_to='bioware/sliders/games/'
    )


class StudioSliderImage(models.Model):
    studio = models.ForeignKey(
        Studio,
        related_name='Slide',
        null=True, blank=None,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        verbose_name='Slide',
        help_text='Attach the slide',
        upload_to='bioware/sliders/studios/'
    )
