from .. import all_views
from django.contrib import admin
from django.urls import path, include


def urlpatterns():
    urlpatterns = [
        # calculator

        # Loancalculator
        path('Calculator/EMI_calculator/',
             all_views.views_calculators.Loan_calculator, name="Loan_calculator"),
        # gcd calculator
        path('Calculator/GCD_calculator/',
             all_views.views_calculators.GCD_calculator, name="GCD_calculator"),
        # BMI calculator
        path('Calculator/BMI_calculator/',
             all_views.views_calculators.BMI_calculator, name="BMI_calculator"),
        # postfix calculator
        path('Calculator/Postfix_calculator/',
             all_views.views_calculators.Postfix_calculator, name="Postfix_calculator"),
        # Prefix calculator
        path('Calculator/Prefix_calculator/',
             all_views.views_calculators.Prefix_calculator, name="Prefix_calculator"),
        # Material weight calculator
        path('Calculator/Material-weight-calculator/',
             all_views.views_calculators.material_weight_calculator, name="material_weight_calculator"),
        # Linear regression calculator
        path('Calculator/Linear-regression-calculator/',
             all_views.views_calculators.Linear_regression_calculator, name="Linear_regression_calculator"),
        # hcf and lcm calculator
        path('Calculator/HCF-LCM-calculator/',
             all_views.views_calculators.HCF_LCM_calculator, name="HCF_LCM_calculator"),
    ]
    return urlpatterns
