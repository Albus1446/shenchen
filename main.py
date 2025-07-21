import argparse
import ee
import geemap.core as geemap

def beichen(longitude: str, latitude: str) -> str:
    longitude = float(longitude)
    latitude = float(latitude)

    ee.Authenticate()
    ee.Initialize(project='astro-465808')

    jan_2022_nightcitylight = (
        ee.ImageCollection("NOAA/VIIRS/DNB/MONTHLY_V1/VCMSLCFG")
        .filterDate('2022-12-01', '2023-01-01')
        .select("avg_rad")
        .first()
    )

    cities = ee.FeatureCollection([
        ee.Feature(ee.Geometry.Point(longitude, latitude), {'city': 'Test Point'}),
    ])

    night_city_light = jan_2022_nightcitylight.reduceRegions(cities, ee.Reducer.first())
    result = ee.data.computeFeatures({'expression': night_city_light, 'fileFormat': 'PANDAS_DATAFRAME'})
    return str(result)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--longitude', type=str, required=True)
    parser.add_argument('--latitude', type=str, required=True)
    parser.add_argument('--output', type=str, default="result.txt")
    args = parser.parse_args()

    result = beichen(args.longitude, args.latitude)

    with open(args.output, 'w') as f:
        f.write(result)

if __name__ == "__main__":
    main()
