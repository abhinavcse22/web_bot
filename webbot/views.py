from django.shortcuts import render
import speech_recognition as sr
import pyttsx3
import wolframalpha
import wikipedia
import webbrowser

def index(request):
    return render(request, 'webbot/index.htm')


def bot_search(request):
    query = request.GET.get('query')

    
    try:
        client = wolframalpha.Client("HEA9AV-EJ2RAPK9RR")
        res = client.query(query)
        ans = next(res.results).text
        return render(request, 'webbot/index.htm', {'ans': ans, 'query': query})

            
    except Exception:
        try:
            ans = wikipedia.summary(query, sentences=10)
            return render(request, 'webbot/index.htm', {'ans': ans, 'query': query})

        except Exception:
            try:
                ans = webbrowser.summary('https://google.com/?#q=' + query)
                return render(request, 'webbot/index.htm', {'ans': ans, 'query': query})
            
            except Exception:
                ans = "It is weird, but I got nothing. Search another question."
                return render(request, 'webbot/index.htm', {'ans': ans, 'query': query})
