from . import urls_authentication
from . import urls_calculators
from . import urls_converters
from . import urls_textanalyzer
from . import urls_translators
from . import other_urls

all_urls = [urls_authentication.urlpatterns(), urls_calculators.urlpatterns(), urls_converters.urlpatterns(), urls_textanalyzer.urlpatterns(), urls_translators.urlpatterns(), other_urls.urlpatterns()]

urlpatterns = []

for i in range(len(all_urls)):
    for val in all_urls[i]:
        urlpatterns.append(val)
