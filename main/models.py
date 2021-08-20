from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager
from django.utils.translation import ugettext_lazy as _

class User(AbstractBaseUser, PermissionsMixin):
    email       = models.EmailField(_("email"), max_length=254)
    phone       = models.CharField(_("phone"), max_length=14, unique=True)
    picture     = models.ImageField(_("picture"), blank=True, null=True, upload_to="media/")
    is_staff    = models.BooleanField(_("is staff"), default=False)
    last_name   = models.CharField(_("lastname"), max_length=50)
    is_active   = models.BooleanField(_("is active"), default=True)
    first_name  = models.CharField(_("firstname"), max_length=50)
    other_name  = models.CharField(_("other name"), blank=True, max_length=50)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def get_full_name(self):
        return f"{self.first_name} {self.last_name} {self.other_name}"

    def get_picture(self):
        return self.picture.url if self.picture else ""

class Post(models.Model):
    body        = models.TextField()
    likes       = models.IntegerField(default=0)
    picture     = models.ImageField(upload_to="media/")
    timestamp   = models.DateTimeField(auto_now_add=True)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)