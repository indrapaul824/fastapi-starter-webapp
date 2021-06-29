import os.path
import markdown


def openFile(file):
    file_path = os.path.join("app/pages/", file)
    with open(file_path, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    

    html = markdown.markdown(text)
    data = {
        "text": html
    }

    return data