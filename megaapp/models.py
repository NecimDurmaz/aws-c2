from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Register your models here.


# glass
class GlassCategory(models.Model):
    title = models.CharField(max_length=50)
    description = RichTextField()
    slug = models.SlugField(
        unique=True, max_length=50, blank=True, db_index=True, editable=False
    )

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class GlassBrand(models.Model):
    title = models.CharField(max_length=50)
    description = RichTextField()
    slug = models.SlugField(
        unique=True, max_length=50, blank=True, db_index=True, editable=False
    )

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Glass(models.Model):
    title = models.CharField(max_length=50)
    description = RichTextField()
    slug = models.SlugField(
        unique=True, max_length=50, blank=True, db_index=True, editable=False
    )
    image = models.ImageField(upload_to="glass")
    category = models.ForeignKey(GlassCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(
        GlassBrand, on_delete=models.CASCADE, null=True, blank=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# watch
class WatchCategory(models.Model):
    title = models.CharField(max_length=50)
    description = RichTextField()
    slug = models.SlugField(
        unique=True, max_length=50, blank=True, db_index=True, editable=False
    )

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class WatchBrand(models.Model):
    title = models.CharField(max_length=50)
    description = RichTextField()
    slug = models.SlugField(
        unique=True, max_length=50, blank=True, db_index=True, editable=False
    )

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Watch(models.Model):
    title = models.CharField(max_length=50)
    description = RichTextField()
    slug = models.SlugField(
        unique=True, max_length=50, blank=True, db_index=True, editable=False
    )
    image = models.ImageField(upload_to="watch")
    category = models.ForeignKey(WatchCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(
        WatchBrand, on_delete=models.CASCADE, null=True, blank=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# coffe
class CoffeCategory(models.Model):
    title = models.CharField(max_length=50)
    description = RichTextField()
    slug = models.SlugField(
        unique=True, max_length=50, blank=True, db_index=True, editable=False
    )

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class CoffeBrand(models.Model):
    title = models.CharField(max_length=50)
    description = RichTextField()
    slug = models.SlugField(
        unique=True, max_length=50, blank=True, db_index=True, editable=False
    )

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Coffe(models.Model):
    title = models.CharField(max_length=50)
    description = RichTextField()
    slug = models.SlugField(
        unique=True, max_length=50, blank=True, db_index=True, editable=False
    )
    image = models.ImageField(upload_to="coffe")
    category = models.ForeignKey(CoffeCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(
        CoffeBrand, on_delete=models.CASCADE, null=True, blank=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
