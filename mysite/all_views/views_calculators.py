from .. import MyFunctions
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json

SideMap = MyFunctions.ArrangeSideMapForWebpage()

def Loan_calculator(request):
    link_string1, link_string2 = SideMap.arrange(0, 4, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/calculator/loan_calculator.html', param)



def GCD_calculator(request):
    link_string1, link_string2 = SideMap.arrange(1, 4, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/calculator/GCD_calculator.html', param)


def BMI_calculator(request):
    link_string1, link_string2 = SideMap.arrange(2, 4, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/calculator/BMI_calculator.html', param)


def Postfix_calculator(request):
    link_string1, link_string2 = SideMap.arrange(3, 4, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/calculator/Postfix_calculator.html', param)


def Prefix_calculator(request):
    link_string1, link_string2 = SideMap.arrange(4, 4, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/calculator/Prefix_calculator.html', param)


def material_weight_calculator(request):
    link_string1, link_string2 = SideMap.arrange(5, 4, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/calculator/material_weight_calculator.html', param)


def Linear_regression_calculator(request):
    link_string1, link_string2 = SideMap.arrange(6, 4, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    if request.method == "POST":
        tableArr = request.POST.getlist('tableArr[]')
        try:
            tableArr = [val.split(',') for val in tableArr]
            x = [int(i[0]) for i in tableArr]
            y = [int(i[1]) for i in tableArr]
            x_sum = sum(x)
            y_sum = sum(y)
            x2 = sum([i**2 for i in x])
            y2 = sum([i**2 for i in y])
            xy = sum([i*j for i, j in zip(x, y)])
            a = (sum(y)*x2-sum(x)*xy)/(len(x)*x2-sum(x)*sum(x))
            b = (len(x)*xy-sum(x)*sum(y))/(len(x)*x2-sum(x)*sum(x))
            eqn = f'y = {format(b,".2f")}x + {format(a,".2f")}'
            response = json.dumps({'Σx': x_sum, 'Σy': y_sum, 'Σx^2': x2, 'Σy^2': y2,
                                  'Σxy': xy, 'Linear Regression Equation(bx + a)': eqn}, default=str)
        except ZeroDivisionError:
            response = json.dumps({'error': 'Division by zero'}, default=str)
        return HttpResponse(response)
    return render(request, '../templates/calculator/linear_regression_calculator.html', param)
# hcf_lcm calculator


def HCF_LCM_calculator(request):
    link_string1, link_string2 = SideMap.arrange(7, 4, 'CC')
    param = {'link_string1': link_string1, 'link_string2': link_string2}
    return render(request, '../templates/calculator/HCF_LCM_calculator.html', param)