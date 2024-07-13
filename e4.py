import webbrowser

user_term = input('Enter a search term: ')

webbrowser.open('https://google.com/search?q=' + user_term)


# webbrowser allows to automate operations with your browser (searches,collecting data etc.)