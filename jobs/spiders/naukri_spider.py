import scrapy

class NaukriSpider(scrapy.Spider):
    name = 'naukri'
    start_urls = ['https://www.naukri.com/python-jobs-in-gurgaon']
    
    def parse(self, response):
        print(f"DEBUG: Status {response.status}, URL: {response.url}")
        print(f"DEBUG: Found {len(response.css('a[href*=\"job\"]'))} job links")
        
        # Generic job links approach
        for link in response.css('a[href*="job"], a[href*="/job/"]')[:5]:
            job_url = link.attrib.get('href')
            if job_url:
                yield response.follow(job_url, callback=self.parse_job)
        
        # Try common job containers
        for job in response.css('div[class*="job"], li[class*="job"]')[:3]:
            yield {
                'title': job.css('a::text, h3::text').get(''),
                'company': job.css('.company::text, span::text').get('')
            }

    def parse_job(self, response):
        yield {
            'title': response.css('h1::text, .jd-header::text').get(''),
            'company': response.css('.company::text').get('')
        }
