from . import urls_authentication
from . import urls_calculators
from . import urls_converters
from . import urls_textanalyzer
from . import urls_translators
from . import other_urls

app_name="mysite"

all_urls = [urls_authentication.urlpatterns(), urls_calculators.urlpatterns(), urls_converters.urlpatterns(), urls_textanalyzer.urlpatterns(), urls_translators.urlpatterns(), other_urls.urlpatterns()]

urlpatterns = []

for all_url in all_urls:
    urlpatterns.extend(iter(all_url))
