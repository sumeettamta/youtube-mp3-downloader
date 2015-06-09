#from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, User
from django.db import models
from django.utils.translation import ugettext_lazy as _
#from django.contrib.auth.models import AbstractBaseUser
from . import manager
class User(AbstractBaseUser):
    first_name = models.CharField(_('first name'), max_length=254)
    last_name = models.CharField(_('last_name name'), max_length=254)

    email = models.EmailField(_('email address'), max_length=254, unique=True)
    phone_number = models.CharField(_('phone_number'), max_length=20, blank=True, default="")

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, default="")
    dob = models.DateField(_('dob'), blank=True, default="9999-01-01")

    #objects = manager.CustomUserManager()
    is_active = models.BooleanField(_('active'), default=False,
                                          help_text=_('Designates whether this user should be treated as active. '
                                                      'Unselect this instead of deleting accounts.'))

    USERNAME_FIELD = 'email'
    #username = 'email'
    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        parts = [self.first_name, self.middle_name, self.last_name]
        return " ".join(x for x in parts if x)

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

    #USERNAME_FIELD = 'email'

    #def email_user(self, subject, message, from_email=None):
     #   """
      #  Sends an email to this User.
       # """
        #send_mail(subject, message, from_email, [self.email])
    def password_change(self):
        password = User.objects.make_random_password()
        self.set_password(password)

    def save(self, *args, **kwargs):
        """
        Override save to add User password and send mail for password change
        """
        #if self.pk is None:
        #    User.password_change(self)
        super(User, self).save(*args, **kwargs)

    def forgot_password(self, *args, **kwargs):
        """
        send random password and link the password edit form
        """

        User.password_change(self)
        super(User, self).save(*args, **kwargs)

