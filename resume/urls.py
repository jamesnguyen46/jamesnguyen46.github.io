from django_distill import distill_path
from resume import views

def get_index():
    return None

urlpatterns = [
    distill_path('',
        views.index,
        name='index',
        distill_func=get_index,
        distill_file='index.html'),
]