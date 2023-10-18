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
    username = ""
    password = ""
    relative_url = '/sites/MT-CCC-CB/Shared%20Documents/Shared/TCR-doc-of-truth.docx'

    ctx_auth = AuthenticationContext(url)
    ctx_auth.acquire_token_for_user(username, password)   
    ctx = ClientContext(url, ctx_auth)
    response = File.open_binary(ctx, relative_url)

    with open(doc_dest, 'wb') as local_file:
        local_file.write(response.content)

    with open(doc_dest, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file)

    link = '<a href="https://emckclac.sharepoint.com/:w:/s/MT-CCC-CB/EQwPPVahenlEqKSQvxFIUawBmA_n9rXgBDEslKcEKua4Tg?e=49i7BL" target="_blank">Click here to edit shared document</a>'
    content = '{% extends "layout.html" %} {% block content %}' + link + result.value + "{% endblock content %}"

    with open(html_dest, "wb") as html_file:
        html_file.write(content.encode('utf8'))
