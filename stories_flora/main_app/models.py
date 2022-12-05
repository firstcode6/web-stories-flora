from django.db import models
from django.contrib.postgres.fields import ArrayField


# Table Languages with 2 columns
class Languages(models.Model):
    language = models.CharField('Language', max_length=50)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'


class Categories(models.Model):
    category_priority = models.IntegerField('Category priority', default=50)

    def __str__(self):
        categ_i18n = Categories_i18n.objects.get(category=self.pk, language=1).name
        return "{} - {}".format(self.pk, categ_i18n)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-pk']


class Categories_i18n(models.Model):
    name = models.CharField('Category', max_length=500, default="News")
    language = models.ForeignKey(Languages, verbose_name='Language id', on_delete=models.PROTECT)
    category = models.ForeignKey(Categories, related_name="categoriesi18n_categories", verbose_name='Category id', on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}".format(self.name, self.language)

    class Meta:
        verbose_name = 'Category_i18n'
        verbose_name_plural = 'Categories_i18n'


class Stories(models.Model):
    category = models.ForeignKey(Categories, related_name="stories_categories", verbose_name='Category id', on_delete=models.PROTECT)
    hide_in_stories = models.BooleanField('Hide in stories', default=True)
    post_priority = models.IntegerField('Post priority', default=20)
    fresh_after = models.DateField('Fresh after')
    fresh_before = models.DateField('Fresh before')
    clients_eligible = ArrayField(models.IntegerField(), default=[2])  # default=list

    # def get_default_something():
    #     return [2]

    #  sets what will be output
    def __str__(self):
        return str(self.pk)

    #  forwarding after saving changes(editing)
    def get_absolute_url(self):
        return f'/story={self.pk}'

    # singular, plural variant
    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'
        ordering = ['-pk']  # the first is the newest story


# Table
class Stories_i18n(models.Model):
    story = models.ForeignKey(Stories, related_name="storiesi18n_stories", verbose_name='Story id', on_delete=models.PROTECT)
    language = models.ForeignKey(Languages, verbose_name='Language id', on_delete=models.PROTECT)
    title = models.CharField('Title', max_length=500)
    subtitle = models.CharField('Subtitle', max_length=500)
    title_icon = models.CharField('Title icon', max_length=500)
    title_image = models.CharField('Title image', max_length=500)

    def __str__(self):
        return "{}-{} ({})".format(self.pk, self.language, self.story )

    def get_absolute_url(self):
        return f'/story={self.story}/story_i18n={self.pk}/'

    class Meta:
        verbose_name = 'Story_i18n'
        verbose_name_plural = 'Stories_i18n'


class Pages(models.Model):
    story_i18n = models.ForeignKey(Stories_i18n, related_name="pages_storiesi18n", verbose_name='Story_i18n id', on_delete=models.PROTECT)
    image = models.CharField('Image', max_length=300)
    icon = models.CharField('Icon', max_length=300, default="assets/icon/icon_startscreen_new.svg")
    headline = models.CharField('Headline', max_length=500)
    text = models.TextField('Text')
    deleted = models.BooleanField('Deleted', default=False)

    def __str__(self):
        return "id:{} story:{}".format(self.pk, self.story_i18n)

    def get_absolute_url(self):
        return f'/story={self.story_i18n.story}/story_i18n={self.story_i18n.pk}/'

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
