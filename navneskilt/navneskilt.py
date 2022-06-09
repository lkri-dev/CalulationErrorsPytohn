import webbrowser, os
print("Dette program udprinter navneskilte til nye elever")
underviser = "Konrad Sommer"

navn = input("Indtast dit navn: ")
htmlTilUdprint = "Elev:<br><h1>" + underviser + "</h1>"
print("Printer navneskilt for '"+navn+"'")

with open('navneskilt.html', 'w') as f:
    f.write('<div style="border: 1px solid gray; display:inline-block;padding:4px 16px 4px 16px;font-family:arial">'
            +htmlTilUdprint
            +"</div>")

webbrowser.open('navneskilt.html')
