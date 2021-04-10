# import PySimpleGUI as sg
import webbrowser

# sg.theme('DarkAmber') # Color

# search_terms = []

# # Design the inside of the window
# layout = [  [sg.Text('UPC Codes to Search')],
#             [sg.InputText()],
#             [sg.Button('Search'), sg.Button('Cancel')] ]

# # Create the Window
# window = sg.Window('UPC Searcher', layout)

# # Event Loop
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
#         break
#     print('You entered ', values[0])
#     search_terms.append(values[0])

# window.close()

# # Result
# print('Search terms: ', search_terms)


chrome_path = "open -a /Applications/Google\ Chrome.app %s"
url='https://www.google.com/search?tbm=isch&q='
searchTerm='test'
searchURL=url+searchTerm
webbrowser.get(chrome_path).open(searchURL)
