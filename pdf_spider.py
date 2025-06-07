from pprint import pprint
import pymupdf as pmdf
import scrapy as sc
import io

class Extractor(sc.Spider):
    name = 'PDF Text Spider'
    allowed_domains = ['pastpapers.papacambridge.com']
    start_urls = ['https://pastpapers.papacambridge.com/papers/caie/igcse-accounting-0452-2022-oct-nov']

    def parse(self, response):
        self.logger.info(f'Parsing page: {response.url}')
        links = response.css("a::attr(href)").getall()

        # for link in links:
        #     yield response.follow(link, callback=self.parse)
        
        pdfs = response.css('a[href$=".pdf"]::attr(href)').getall()
        # pdfs.extend(response.xpath('//a[contains(@href, "/upload/")]/@href').getall())

        self.logger.info(f'Found {len(pdfs)} potential PDF links on {response.url}')
        for pdf in pdfs:
            yield response.follow(pdf, callback=self.parse_pdf)
    
    def parse_pdf(self, response):
        pdf_in_memory_file = io.BytesIO(response.body)
        try:
           with pmdf.open(stream=pdf_in_memory_file, filetype="pdf") as paper:
               self.logger.info(f'Successfully opened PDF from {response.url}')
               file_name = response.url.split("/")[-1]
               for pg_num in range(len(paper)):
                    page = paper.load_page(pg_num)
                    needle = 'Prepare the income statement'
                    matches = page.search_for(needle)
                    if matches != []:
                        print(("{0} page {1} shows '{2}' in the following locations:").format(file_name, pg_num, needle))
                        pprint(matches)
                        pg_num = str(pg_num+1)
                        with open('results.txt', 'a') as file:
                            file.write(f'Paper: {file_name[:-4]}, page number: {pg_num}\n')
                    else:
                        print(("'{0}' does not occur in '{1}' page {2}.").format(needle, file_name, pg_num))
        except Exception as e:
            self.logger.error(f'Failed @ {response.url} due to {e}')
    

