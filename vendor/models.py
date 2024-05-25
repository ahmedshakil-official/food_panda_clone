from django.db import models

from accounts.models import User, UserProfile
from vendor.utils import send_notification_email


class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    user_profile = models.OneToOneField(
        UserProfile, on_delete=models.CASCADE, related_name="user_profile"
    )
    vendor_name = models.CharField(max_length=100)
    vendor_licence = models.ImageField(upload_to="vendor/licence")
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor_name

    def save(self, *args, **kwargs):
        if self.pk:
            current_status = Vendor.objects.get(pk=self.pk).is_approved
            if current_status != self.is_approved:
                template = "vendor/email/admin_approved.html"
                context = {
                    "user": self.user,
                    "is_approved": self.is_approved,
                }
                if self.is_approved:
                    subject = "Congratulations, you are approved!"
                    send_notification_email(subject, template, context)
                else:
                    subject = "Sorry, you are not approved!"
                    send_notification_email(subject, template, context)
        return super(Vendor, self).save(*args, **kwargs)
