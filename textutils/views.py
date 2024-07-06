from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params = {
        'name': 'Django',
        'Place': 'Earth'
    }
    return render(request,'index.html', params)
def analyze(request):

    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    caps = request.POST.get('caps','off')
    newlineremover = request.POST.get('newlineremover')
    extralineremover = request.POST.get('extralineremover')
    charcount = request.POST.get('charcount')

    analyzed = djtext
    purpose_list = []

    if removepunc == 'on':
        punctuations = '''.,?!:;$'"-–—()[]{}\/@#%&*^~_|¶§©®™...'''
        analyzed = ''.join(char for char in analyzed if char not in punctuations)
        purpose_list.append("Removed Punctuations")

    if caps == 'on':
        analyzed = analyzed.upper()
        purpose_list.append("Changed to Uppercase")

    if newlineremover == 'on':
        analyzed = ''.join(char for char in analyzed if char != '\n' and char != '\r')
        purpose_list.append("Removed New Lines")

    if extralineremover == 'on':
        analyzed = ' '.join(analyzed.split())
        purpose_list.append("Removed Extra Spaces")

    if charcount == 'on':
        char_count = len(analyzed)
        purpose_list.append(f"Total Characters: {char_count}")
    else:
        char_count = None

    if not purpose_list:
        return HttpResponse("Error: No options selected")

    params = {
        'purpose': ', '.join(purpose_list),
        'analyzed_text': analyzed,
        'char_count': char_count
    }
    return render(request, 'analyze.html', params)
