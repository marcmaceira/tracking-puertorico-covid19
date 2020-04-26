import json
from datetime import datetime
import scrapy

from .utils import strip_accents, is_float, is_int, is_blank

def normalize_date(date_ms):
    return datetime.fromtimestamp(date_ms/1000)

class PuertoRicoCovid19Spider(scrapy.Spider):
    name = 'puertorico-covid19'
    start_urls = ['https://services5.arcgis.com/klquQoHA0q9zjblu/arcgis/rest/services/Datos_Totales/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outSR=102100&resultOffset=0&resultRecordCount=50&cacheHint=true']
    date_fields = [
        "EditDate",
        "CreationDate"
    ]
    excluded_fields = [
        "OBJECTID",
        "IDNumber",
        "Creator",
        "CreationDate",
        "EditDate",
        "Editor"
    ]

    def parse(self, response):
        pr_covid_data = json.loads(response.body_as_unicode())
        fields = pr_covid_data["fields"]
        attributes = pr_covid_data["features"][0]["attributes"]
        last_update_at = normalize_date(pr_covid_data["features"][0]["attributes"]["EditDate"])
        editor = pr_covid_data["features"][0]["attributes"]["Editor"]
        creator = pr_covid_data["features"][0]["attributes"]["Creator"]
        creation_date = normalize_date(pr_covid_data["features"][0]["attributes"]["CreationDate"])

        for field in fields:
            field_name = field["name"]

            if field_name not in self.excluded_fields:
                value = attributes[field_name]

                if field_name in self.date_fields:
                    value = datetime.fromtimestamp(value//1000.0)

                yield {
                    "path": field_name.lower(),
                    "label": field["alias"],
                    "value": value,
                    "last_updated_at": last_update_at,
                    "editor": editor,
                    "creator": creator,
                    "creationDate": creation_date,
                }
