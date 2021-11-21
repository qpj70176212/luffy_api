from django.test import TestCase

# Create your tests here.
from django.conf import settings
# phone = 17260808696
phone = "17260808696"
res = "sms_cache_phone_%s" % phone
print(res)