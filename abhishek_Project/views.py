from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'abhishek': 'priti'})


def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    wordlist = fulltext.split()
    wordDictionary = dict()
    for word in wordlist:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'wordDictionary': wordDictionary.items()})
