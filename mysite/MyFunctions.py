
from googletrans import Translator
from . import globals
import json
from django.shortcuts import render
from django.http import HttpResponse
urls = globals.urlSideMapList()


class TranslatorFun:
    def Translate(self, text, dest, src='en'):
        trans = Translator()
        return trans.translate(text, dest=dest, src=src)

    def EnglishToOther(self, request, indi_id, dest, htmlFile):
        link_string1, link_string2 = ArrangeSideMapForWebpage.arrange(
            self, indi_id, 3, 'AT')
        if request.method == "POST":
            try:
                text = request.POST.get('text', 'default')
                t = self.Translate(text, dest)
                alt = True
                param = {"ortext": text, "text": t.text, "alt": alt,
                         'link_string1': link_string1, 'link_string2': link_string2}
            except Exception:
                param = {"ortext": text, "text": "There is some Error while processing, can be due to invalid input such as blank space", "alt": True,
                         'link_string1': link_string1, 'link_string2': link_string2}
        else:
            param = {'link_string1': link_string1, 'link_string2': link_string2}
        return render(request, htmlFile, param)

    def HindiToOther(self, request, indi_id, dest, src, htmlFile):
        link_string1, link_string2 = ArrangeSideMapForWebpage.arrange(
            self, indi_id, 3, 'AT')
        if request.method == "POST":
            try:
                text = request.POST['text']
                if text == "":
                    res = json.dumps({'ConTex': ""}, default=str)
                else:
                    t = self.Translate(text, dest, src=src)
                    res = json.dumps({'ConTex': t.text}, default=str)
            except Exception:
                res = json.dumps({'ConTex': "There is some Error while processing,edit some text or type some.It may work"}, default=str)
            return HttpResponse(res)
        param = {'link_string1': link_string1, 'link_string2': link_string2}
        return render(request, htmlFile, param)


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
