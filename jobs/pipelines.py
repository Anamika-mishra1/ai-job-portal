# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from itemadapter import ItemAdapter

class JobsPipeline:
    def open_spider(self, spider):
        self.jobs = []

    def process_item(self, item, spider):
        self.jobs.append(ItemAdapter(item).asdict())
        return item

    def close_spider(self, spider):
        with open('jobs_naukri.json', 'w') as f:
            json.dump(self.jobs, f, indent=2)
        
        # CSV for Django
        import pandas as pd
        df = pd.DataFrame(self.jobs)
        df.to_csv('jobs_naukri.csv', index=False)
