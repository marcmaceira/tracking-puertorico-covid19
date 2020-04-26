# Tracking Puerto Rico COVID-19 Dashboard

This tool consumes the [official COVID-19 dashboard of Puerto Rico](https://bioseguridad.maps.arcgis.com/apps/opsdashboard/index.html#/3bfb64c9a91944bc8c41edd8ff27e6df) [JSON source](https://services5.arcgis.com/klquQoHA0q9zjblu/arcgis/rest/services/Datos_Totales/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outSR=102100&resultOffset=0&resultRecordCount=50&cacheHint=true) every hour and keeps tracks of changing metrics in order to help visualize and measure progress. Data is also made available in CSV and JSON formats.

## Requirements

Before running this project locally you need to have MongoDB installed.

- [Take a look at the MongoDB docs](https://docs.mongodb.com/manual/installation/) for installation instructions.
- If you are using MacOS you can also use [Giovanni Collazo's MongoApp](https://gcollazo.github.io/mongodbapp/).

## Running

### Project Setup

To install the project's Python dependencies you can user the `requirements.txt` or the project's `Pipfile` using [Pipenv](https://pipenv.pypa.io/en/latest/).

Using Pip:

```shell
> pip install -r requirements.txt
```

Using Pipenv

```shell
> pipenv install --three
```

### Web

To run the Flask app execute:

```shell
> MONGODB_URI='mongodb://localhost/tracking-covid19-pr' FLASK_DEBUG=1 FLASK_APP=app/app.py flask run
```

### Scraper

To run the JSON scrapper execute:

```shell
> MONGODB_URI='mongodb://localhost/tracking-covid19-pr' python -m app.scraper
```
