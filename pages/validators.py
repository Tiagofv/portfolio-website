
def validatePdf(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.png', '.jpg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Please use a pdf , doc , png , jpg extension for the CV.')