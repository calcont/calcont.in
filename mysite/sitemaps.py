from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewsSitemap(Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return [
            "index",
            "contact",
            "Login",
            "Signin",
            "text",
            "name_sorting",
            "grammar",
            "KeywordsExtraction",
            "texttobase64",
            "base64totext",
            "texttoimage",
            "imagetotext",
            "LangIdenti",
            "caesarCipher",
            "playfCipher",
            "Binaryconversion",
            "Decimalconversion",
            "Hexadecimalconversion",
            "Currencyconversion",
            "prefix_to_infix",
            "prefix_to_postfix",
            "infix_to_postfix",
            "cgpa_to_percentage",
            "postfix_to_infix",
            "infix_to_prefix",
            "Image_to_base64",
            "Base64_to_Image",
            "Epoch_Timestamp_Converter",
            "IST_UTC_Converter",
            "EnglishToHindi",
            "EnglishToMarathi",
            "EnglishToGerman",
            "EnglishToFrench",
            "EnglishToArabian",
            "EnglishToSpanish",
            "EnglishToThai",
            "HindiToEnglish",
            "HindiToMarathi",
            "HindiToGerman",
            "HindiToFrench",
            "HindiToArabian",
            "HindiToSpanish",
            "HindiToThai",
            "Loan_calculator",
            "GCD_calculator",
            "BMI_calculator",
            "Postfix_calculator",
            "Prefix_calculator",
            "material_weight_calculator",
            "Linear_regression_calculator",
            "HCF_LCM_calculator",
            "SIP_calculator",
            "PrivacyPolicy",
        ]

    def location(self, item):
        return reverse(item)
