import os
import re
import docx


def get_filenames_from_folder(folder_path, extension):
    '''Receives a folder path and a file extension and returns a list of its files names'''
    return [file.replace(extension, '') for file in os.listdir(folder_path) if file.endswith(extension)]


def get_text_from_docx(filename):
    '''Receives a .docx filename and returns a string with its contents'''
    doc = docx.Document(filename+'.docx')
    full_text = ''
    for paragraph in doc.paragraphs:
        full_text += paragraph.text + '\n'
    return full_text


def cleanup(text):
    '''Receves a string and returns a formatted string following the rules specified by regex'''

    # Remove the number of scenes from the title
    removeNumberOfScenes = re.sub(r'\(\S+\s*[Ss][Cc][Ee][Nn][Ee][Ss]\s*\)\s*',
                                  '-> ', text)
    # Remove the scene identification
    # REGEX: '('+'SCENE with lower or uppercase'+'whitespace'+'one or more chars'+'whitespace'+')'+'whitespace'
    # Ex: (SCENE 1), (Scene 21), (sCeNe   12-13),...
    removeScene = re.sub(r'\([Ss][Cc][Ee][Nn][Ee]\s*\S+\s*\)\s*',
                         '', removeNumberOfScenes)
    # Remove the slide identification
    removeSlide = re.sub(r'\([Ss][Ll]\s*\S+\s*\)\s*',
                         '', removeScene)
    # Remove dashes
    removeDashes = re.sub(r'\s+-+\s+', ' ', removeSlide)
    # Remove slashes
    # REGEX: Using substitution groups to keep the period (.) if it's there
    removeSlashes = re.sub(r'([\s+.])(/+)(\s+)', r'\1 ', removeDashes)
    # Remove newlines
    removeNewLine = removeSlashes.replace('\n', ' ')
    # Remove excess whitespace
    removeWhiteSpace = re.sub(r'\s+', ' ', removeNewLine)

    return removeWhiteSpace


def create_txt(text, filename):
    '''Receives a string and a filename and create a .txt file in the txt folder'''
    if not os.path.exists('./txt'):
        os.mkdir('./txt')
    with open(r'./txt/'+filename+r'.txt', 'w', encoding="utf-8") as fh:
        fh.write(text)

# EXECUTION


filenames = get_filenames_from_folder('./', '.docx')

for filename in filenames:
    docx_txt = get_text_from_docx(filename)
    clean_text = cleanup(docx_txt)
    create_txt(clean_text, filename)
    print(f'{filename} ok!')
