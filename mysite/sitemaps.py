from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewsSitemap(Sitemap):
    priority=0.5
    changefreq="daily"
    def items(self):
        return [
            "mysite:index",
            "mysite:contact",
            "mysite:about",
            "mysite:Login",
            "mysite:Signin",
            "mysite:text",
            "mysite:name_sorting",
            "mysite:grammar",
            "mysite:KeywordsExtraction",
            "mysite:texttobase64",
            "mysite:base64totext",
            "mysite:texttoimage",
            "mysite:imagetotext",
            "mysite:LangIdenti",
            "mysite:caesarCipher",
            "mysite:playfCipher",
            "mysite:Binaryconversion",
            "mysite:Decimalconversion",
            "mysite:Hexadecimalconversion",
            "mysite:Currencyconversion",
            "mysite:prefix_to_infix",
            "mysite:prefix_to_postfix",
            "mysite:infix_to_postfix",
            "mysite:cgpa_to_percentage",
            "mysite:postfix_to_infix",
            "mysite:infix_to_prefix",
            "mysite:Image_to_base64",
            "mysite:Base64_to_Image",
            "mysite:EnglishToHindi",
            "mysite:EnglishToMarathi",
            "mysite:EnglishToGerman",
            "mysite:EnglishToFrench",
            "mysite:EnglishToArabian",
            "mysite:EnglishToSpanish",
            "mysite:EnglishToThai",
            "mysite:HindiToEnglish",
            "mysite:HindiToMarathi",
            "mysite:HindiToGerman",
            "mysite:HindiToFrench",
            "mysite:HindiToArabian",
            "mysite:HindiToSpanish",
            "mysite:HindiToThai",
            "mysite:Loan_calculator",
            "mysite:GCD_calculator",
            "mysite:BMI_calculator",
            "mysite:Postfix_calculator",
            "mysite:Prefix_calculator",
            "mysite:material_weight_calculator",
            "mysite:linear_regression_calculator",
            "mysite:PrivacyPolicy",
        ]
    def location(self, item):
        return reverse(item)