from django.core.exceptions import ValidationError

def validate_obieg(value):
	if "PW-" not in value:
		raise ValidationError("Poprawny format nazwy to PW-xxxxxx")
