import pdfplumber
import asyncio
from converter import ConverterPdfHtml

async def main():
    conver = ConverterPdfHtml()
    await conver.convert()


if __name__ == '__main__':
    asyncio.run(main())