import pdfplumber 
import aiofiles


class ConverterPdfHtml:
    def __init__(self):
        pass
    
    async def convert(self):
        html :list = []

        html.extend(Header.add_header())

        with pdfplumber.open('test_data/szv.pdf') as pdf:
            for page in pdf.pages:
                p = Page(page=page)
                page = await p.convert_to_html()
                html.extend(page)

        html.extend(Footer.add_footer())
        async with aiofiles.open(f'3.html', mode='a') as f:
            await f.write('\n'.join(html))


class Header():
    @staticmethod
    def add_header():
        return ['<html>','\t<head>','\t</head>','\t<body>']

class Footer():
    @staticmethod
    def add_footer():
        return ['\t</body>','</html>']


class Page:
    def __init__(self, page: pdfplumber.page) -> None:
        self.page_text :str = page.extract_text()
        self.tables :list = page.extract_tables()
        self.lines :list = []

    async def convert_to_html(self):
        page :list = []

        for line in self.page_text.split('\n'):
            if line:
                html_file = f'\t\t<div> {line} </div>'
                page.append(html_file)
        

        for table in self.tables:
            if table:
                page.append('\t\t<table>')
                for row in table:
                    if row: 
                        page.append('\t\t\t<tr>')
                        for element in row:
                            page.append(f'\t\t\t\t<td>{element}</td>')
                        page.append('\t\t\t</tr>')
                page.append('\t\t</table>')

        return page
                
            
        
                


    