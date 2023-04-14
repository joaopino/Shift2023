from django.db import models


# Has to be defined before the other imports to avoid issues
def fk(model):
    return models.ForeignKey(model, on_delete=models.CASCADE)


from moelasware.models.quiz import *
from moelasware.models.review import *
from moelasware.models.submission import *
from moelasware.models.tag import *
from moelasware.models.test import *
from moelasware.models.user import *
