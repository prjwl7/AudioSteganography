from django.contrib import admin
from django.urls import path
from first.views import home_view
from first.views import speech_view
from first.views import output_speech
from first.views import output_speech2
from first.views import output_speech3
from first.views import speech_view2
from first.views import decryption_fhss
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('speech.html', speech_view, name='speech_page'),
    path('output_speech/', output_speech, name='output_speech'),  # Corrected name
    path('output_speech2/', output_speech2, name='output_speech2'),  # Corrected name
    path('output_speech3/', output_speech3, name='output_speech3'),  # Corrected name
    path('speech2.html', speech_view2, name='speech2'),  # Corrected name
    path('decryption_audio.html', decryption_fhss, name='decryption_fhss'),  # Corrected name
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)