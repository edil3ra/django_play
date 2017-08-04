import os
from django.utils.timezone import now as timezone_now


def upload_to(instance, filename):
    now = timezone_now()
    filename_base , filename_ext = os.path.splitext(filename)
    return 'quotes/{}{}'.format(now.strftime('%Y/%m/%Y%m%d%H%M%S')
                                ,filename_ext.lower())
