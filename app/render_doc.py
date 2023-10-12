from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File
import mammoth
import os


def docx_as_html():

    path = os.path.dirname(__file__)
    doc_dest = os.path.join(path, 'TCR-doc-of-truth.docx')
    html_dest = os.path.join(path, 'templates/TCR-doc-of-truth.html')

    url = "https://emckclac.sharepoint.com/sites/MT-CCC-CB"
    username = "k2367592@kcl.ac.uk"
    password = "Babyruiz122!"
    relative_url = '/sites/MT-CCC-CB/Shared%20Documents/Shared/TCR-doc-of-truth.docx'

    ctx_auth = AuthenticationContext(url)
    ctx_auth.acquire_token_for_user(username, password)   
    ctx = ClientContext(url, ctx_auth)
    response = File.open_binary(ctx, relative_url)
    with open(doc_dest, 'wb') as local_file:
        local_file.write(response.content)

    with open(doc_dest, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)
    with open(html_dest, "w") as html_file:
        html_file.write(result.value)

    line = '{% extends "layout.html" %} {% block content %}'
    with open(html_dest, 'r+') as html_file:
        content = html_file.read()
        html_file.seek(0, 0)
        html_file.write(line.rstrip('\r\n') + '\n' + content)

    print("TRYNA WRITE")
    with open(html_dest, "a") as html_file:
        html_file.write("{% endblock content %}")
    
