from docx2pdf import convert

def convertFile(input, output):
    convert(input, output)

if __name__ == '__main__':
    convertFile(input='src/file.docx', output='src/file.pdf')
