# INFLU-ヤン (Influyan)

> A recovered, pre-model prototype of a public influenza surveillance and forecasting application for Japan's Kansai region.

## Project overview

INFLU-ヤン was designed as a public medical-information application that makes regional influenza activity easier to understand. The system combines official case data, geographic boundaries, and prediction graphs so that users can identify areas with higher influenza activity, make informed health decisions, and take appropriate precautions when planning travel.

Its primary audience is the general public, and the interface was designed to work in both English and Japanese without requiring prior training.

## Original system vision

The project documentation describes a complete system that would:

- Collect validated influenza data from Japan's Ministry of Health, Labour and Welfare (MHLW) and prefectural infectious-disease surveillance centers.
- Refresh official datasets weekly and normalize source files supplied in different PDF, Excel, and HTML formats.
- Combine influenza case counts with geographic data to create color-coded choropleth maps.
- Let users search for a city, regional surveillance group, or prefecture in English or Japanese.
- Display historical statistics and predicted influenza trends for a selected area.
- Help users identify infection hotspots and understand regional differences.
- Support future personal risk assessment and environmental-correlation features.

The final report confirms that official prefectural sources were preferred because they provided consistent weekly updates. Hospital data and `disease.sh` were investigated but were not used in the final data source selection.

## Recovered prototype features

The files in this repository demonstrate part of that vision:

- An interactive map covering Osaka, Kyoto, and Nara.
- Color-coded regional case counts.
- City, surveillance-region, and prefecture selection.
- City and region search.
- Location details and case counts for a selected area.
- English and Japanese interface modes.
- Region-specific forecast-image display.
- Flask JSON endpoints for case and forecast data.

The case values and forecast images in this recovered version are placeholders. They are not live surveillance data or output from a trained forecasting model.

## Data and geographic scope

The original Software Requirements Specification proposed a public map covering Kyoto, Osaka, Hyogo, Nara, and Shiga. Its ingestion requirements also discussed Wakayama. The recovered prototype contains geographic overlays for Osaka, Kyoto, and Nara only.

The final project work included researching how cities map to official influenza-surveillance regions. These regions do not always match ordinary administrative boundaries. Duplicate place names also required special handling; for example, `北区` (`Kita-ku`) occurs in both Osaka City and Sakai City. The team redefined ambiguous names so that GeoPandas could distinguish them correctly.

## Documented system workflow

The original documentation describes this intended workflow:

1. Download or scrape weekly official data published as Excel, PDF, or HTML.
2. Clean, convert, validate, and normalize the different prefectural formats.
3. Store processed datasets in a shared data store and aggregate them by time, age group, and surveillance region.
4. Match regional case values to geographic boundaries using GeoPandas.
5. Render an interactive choropleth map and historical statistics.
6. Apply time-series forecasting and display a prediction graph for the selected region.

The final report confirms the data collection and normalization work, GeoPandas-based regional classification, choropleth preparation, and bilingual search work. Other components below were specified in the SRS but are not available in this repository.

## Technologies

### Present in the recovered repository

| Area | Technology | Purpose |
| --- | --- | --- |
| Backend | Python and Flask | Serves the interface and JSON endpoints |
| Frontend | HTML, CSS, and JavaScript | Implements the user interface and interactions |
| Interactive map | Leaflet 1.9.3 | Renders geographic layers and map controls |
| Base map | OpenStreetMap | Supplies the underlying map tiles |
| Geographic data | GeoJSON | Stores the Osaka, Kyoto, and Nara boundaries |
| Data loading | jQuery 3.7.1 and Fetch API | Loads overlays and requests backend data |
| Image utilities | Pillow | Creates placeholder forecast PNG files |
| Data exchange | JSON | Transfers case and forecast information |

### Described in the final report or original SRS

| Area | Technology | Documentation status |
| --- | --- | --- |
| Geospatial processing | GeoPandas | Its use for city and surveillance-region classification is confirmed in the final report |
| Map generation | Folium | Specified in the SRS; the recovered frontend uses Leaflet instead |
| Official-data download | `urllib.request` | Specified in the SRS; implementation is missing from this repository |
| Web scraping | Beautiful Soup | Specified for Osaka data in the SRS; implementation is missing |
| PDF preparation | Adobe PDF API | Specified for cleaning and converting prefectural PDFs; implementation is missing |
| Dataset storage | Amazon S3 and a pointer database | Specified in the SRS; storage code and configuration are missing |
| Forecasting | ARIMA | Specified for weekly time-series forecasts; model code and trained artifacts are missing |
| Graph generation | Matplotlib | Specified for historical and forecast plots; generation code is missing |

## Planned features not contained here

The original SRS includes requirements that cannot be verified as completed and are not present in this repository:

- Automatic weekly ingestion from official sources.
- Historical views with weekly, monthly, and yearly controls.
- Live ARIMA forecasts and adjustable forecast ranges.
- Comparison of multiple regions and threshold alerts.
- Personal influenza-risk assessment using health, location, and transport factors.
- Hyogo, Shiga, and Wakayama data and geographic coverage.
- Population-density adjustment.
- Environmental correlation analysis using temperature, air quality, and humidity.
- Pearson-correlation, line, and scatter plots.

## Available API endpoints

| Endpoint | Description |
| --- | --- |
| `GET /api/total_cases` | Returns placeholder influenza case counts grouped by region |
| `GET /api/forecast?region=<region>` | Returns the placeholder forecast-image path for a selected region |

## Project files

- `app.py` contains the Flask server, endpoints, dummy case data, and forecast-image mappings.
- `merged_map_v1.4.1.html` contains the map interface and frontend logic.
- `kyoto_overlay.json`, `osaka_overlay.json`, and `nara_overlay.json` contain regional boundary data.
- `forecast_plot_*.png` files are placeholder forecast charts.
- `create_dummy_plots.py` creates placeholder forecast images.
- `DemoVideo_Influyan.mp4` demonstrates the completed version of the system before its original files were lost.

## Run the recovered prototype

Python 3 is required.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install Flask Pillow
python app.py
```

The Flask development server normally starts at `http://127.0.0.1:5000`.

## Current limitations

This repository does not contain the original database, official-data pipeline, forecasting model, model-training code, risk-assessment feature, or the rest of the completed application.

The recovered frontend also contains development-specific localhost and private IP addresses. Its static-file route conflicts with Flask's default static route, and the Forecast and Risk Assessment navigation links do not have corresponding Flask routes. These issues may need to be corrected before the recovered version works fully in a browser.

The available reports do not provide a forecasting accuracy score, evaluation dataset, or other quantitative model results, so no model-performance claim is made here.

## Project recovery and demonstration video

The complete project folder was stored only on a laptop and was lost when the laptop broke. Unfortunately, there was no other backup of that folder.

A demonstration video of the complete version survived because it was saved in a different environment. It provides the best remaining visual reference for the completed system.

[Watch the Influyan demonstration video](DemoVideo_Influyan.mp4) (2 minutes 46 seconds, 1280×720, H.264/AAC MP4, approximately 30 MB).





