from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from people.models import Person


@receiver(post_save, sender=Person)
def create_user_for_person(
    sender: Person, instance: Person, created: bool, **kwargs
):
    if created and not instance.user:
        create_user(instance)


def create_user(person: Person):
    user, created = User.objects.get_or_create(
        username=person.personal_email,
        defaults={
            "email": person.personal_email,
            "first_name": person.first_name,
            "last_name": person.last_name,
            "is_staff": True,
        },
    )
    if created:
        person.user = user
        person.save()


def deactivate_user(person: Person):
    if not person.user_id:
        return
    person.user.is_staff = False
    person.user.is_active = False
    person.user.save()
