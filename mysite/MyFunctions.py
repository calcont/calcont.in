from . import globals
import json
from django.shortcuts import render
from django.http import HttpResponse
from .Services.TextService import translate_text

urls = globals.urlSideMapList()


class TranslatorFun:

    def english_to_other(self, request, indi_id, dest, html_file):
        link_string1, link_string2 = ArrangeSideMapForWebpage.arrange(
            self, indi_id, 3, 'AT')
        if request.method == "POST":
            input_text = request.POST.get('text', 'default')
            try:
                translated_text = translate_text(input_text, src='en', target=dest)
                alt = True
                param = {"ortext": input_text, "text": translated_text, "alt": alt,
                         'link_string1': link_string1, 'link_string2': link_string2}
            except Exception:
                param = {"ortext": input_text,
                         "text": "There is some Error while processing, can be due to invalid input such as blank space",
                         "alt": True,
                         'link_string1': link_string1, 'link_string2': link_string2}
        else:
            param = {'link_string1': link_string1, 'link_string2': link_string2}
        return render(request, html_file, param)

    def hindi_to_other(self, request, indi_id, dest, src, html_file):
        link_string1, link_string2 = ArrangeSideMapForWebpage.arrange(
            self, indi_id, 3, 'AT')
        if request.method == "POST":
            try:
                text = request.POST['text']
                if text == "":
                    res = json.dumps({'ConTex': ""}, default=str)
                else:
                    translated_text = translate_text(text, src, dest)
                    res = json.dumps({'ConTex': translated_text}, default=str)
            except Exception:
                res = json.dumps(
                    {'ConTex': "There is some Error while processing,edit some text or type some.It may work"},
                    default=str)
            return HttpResponse(res)
        param = {'link_string1': link_string1, 'link_string2': link_string2}
        return render(request, html_file, param)


class ArrangeSideMapForWebpage:

    def arrange(self, indi_id, grp_id, same_grps_id):
        links_strings_1 = []
        links_strings_2 = []
        for link in range(len(urls)):

            if urls[link][3] == same_grps_id:
                if urls[link][2] == grp_id:
                    if urls[link][4] != indi_id:
                        links_strings_1.append([urls[link][0], urls[link][1]])
                else:
                    links_strings_2.append([urls[link][0], urls[link][1]])
        return links_strings_1, links_strings_2
