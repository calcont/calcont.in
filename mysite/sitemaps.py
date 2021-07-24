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
            "mysite:Binaryconversion",
            "mysite:Decimalconversion",
            "mysite:Hexadecimalconversion",
            "mysite:Currencyconversion",
            "mysite:Unitconversion",
            "mysite:Unit_mtocm_conversion",
            "mysite:Unit_mtomm_conversion",
            "mysite:Unit_mtoinch_conversion",
            "mysite:Unit_mtofoot_conversion",
            "mysite:Unit_mtomile_conversion",
            "mysite:Unit_mtoyard_conversion",
            "mysite:Unit_mtoangstrom_conversion",
            "mysite:Unit_cmtomm_conversion",
            "mysite:Unit_cmtoinch_conversion",
            "mysite:Unit_cmtofoot_conversion",
            "mysite:Unit_cmtomile_conversion",
            "mysite:Unit_cmtoyard_conversion",
            "mysite:Unit_cmtoangstrom_conversion",
            "mysite:EnglishToHindi",
            "mysite:EnglishToMarathi",
            "mysite:EnglishToGerman",
            "mysite:EnglishToFrench",
            "mysite:EnglishToArabian",
            "mysite:Loan_calculator",
            "mysite:GCD_calculator",
            "mysite:BMI_calculator",
            "mysite:Postfix_calculator",
            "mysite:PrivacyPolicy",
            "mysite:infix_to_postfix",
            "mysite:infix_to_prefix",
            "mysite:cgpa_to_percentage",
            "mysite:postfix_to_infix",
        ]
    def location(self, item):
        return reverse(item)