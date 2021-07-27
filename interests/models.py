from django.db import models

class Interest(models.Model):
    #     interests = [
    # ('RE', 'Reading'),
    # ('TR', 'Travelling'),
    # ('CO', 'Coding'),
    # ('MU', 'Music'),
    # ('SM', 'Social Media'),
    # ('EX', 'Exercise'),
    # ('PH', 'Photography'),
    # ('CK', 'Cooking'),
    # ('TW', 'Twerking'),
    # ('AS', 'Airsoft'),
    # ('GA', 'Gaming')
    # ]
    #     interests = models.CharField(
    #   max_length=20,
    #   choices=interests,
    #   null=True
    # )
    label = models.CharField(max_length=50, default=None)

    def __str__(self):
        return f"{self.label}"
