
import json

month_table = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}

def convert_season(season):
    if season == "Year-round":
        return list(range(1, 13))
    months = season.split(' - ')
    return [month_table[month] for month in months]

def convert_duration(duration):
    if 'week' in duration:
        return [int(x) for x in duration.split(' ')[0].split('-')]
    elif 'month' in duration:
        weeks = [int(x) * 4 for x in duration.split(' ')[0].split('-')]
        return weeks

def convert_price(price):
    return [float(x) for x in price.split(' - ')]

def convert_harvest_time(harvest_time):
    if harvest_time == "Continuous harvest":
        return "Continuous"
    elif 'week' in harvest_time:
        return [int(x) for x in harvest_time.split(' ')[0].split('-')]
    elif 'month' in harvest_time:
        try:
            months = [int(x) for x in harvest_time.split(' ')[0].split('-')]
            return [month * 4 for month in months]
        except ValueError:
            return harvest_time
    else:
        try:
            return [int(x) for x in harvest_time.split('-')]
        except ValueError:
            return harvest_time

data = [
    {
        "Vegetable Name": "Morning Glory (Trakuon)",
        "Planting Season": ["Year-round"],
        "Harvest Time": convert_harvest_time("Continuous harvest"),
        "Growth Duration": convert_duration("3-4 weeks"),
        "Price per KG (USD)": convert_price("1.00 - 1.50"),
        "Notes": "Fast-growing, grows in water"
    },
    {
        "Vegetable Name": "Bok Choy (Pak Choi)",
        "Planting Season": convert_season("Nov - Mar"),
        "Harvest Time": convert_harvest_time("6 weeks"),
        "Growth Duration": convert_duration("4-6 weeks"),
        "Price per KG (USD)": convert_price("1.20 - 1.60"),
        "Notes": "Needs irrigation in dry season"
    },
    {
        "Vegetable Name": "Chinese Cabbage",
        "Planting Season": convert_season("Nov - Feb"),
        "Harvest Time": convert_harvest_time("8 weeks"),
        "Growth Duration": convert_duration("6-8 weeks"),
        "Price per KG (USD)": convert_price("1.50 - 2.00"),
        "Notes": "Cooler season crop"
    },
    {
        "Vegetable Name": "Tomatoes",
        "Planting Season": convert_season("Nov - Mar"),
        "Harvest Time": convert_harvest_time("Continuous harvest"),
        "Growth Duration": convert_duration("2-3 months"),
        "Price per KG (USD)": convert_price("1.20 - 1.80"),
        "Notes": "Requires irrigation"
    },
    {
        "Vegetable Name": "Green Beans",
        "Planting Season": convert_season("Nov - Feb"),
        "Harvest Time": convert_harvest_time("Continuous harvest"),
        "Growth Duration": convert_duration("2 months"),
        "Price per KG (USD)": convert_price("1.50 - 2.00"),
        "Notes": "Grows well in dry conditions"
    },
    {
        "Vegetable Name": "Cucumbers",
        "Planting Season": convert_season("Nov - Mar"),
        "Harvest Time": convert_harvest_time("Continuous harvest"),
        "Growth Duration": convert_duration("6-8 weeks"),
        "Price per KG (USD)": convert_price("0.80 - 1.20"),
        "Notes": "Needs trellis support"
    },
    {
        "Vegetable Name": "Chili Peppers",
        "Planting Season": convert_season("Nov - Apr"),
        "Harvest Time": convert_harvest_time("Continuous harvest"),
        "Growth Duration": convert_duration("2-3 months"),
        "Price per KG (USD)": convert_price("1.50 - 2.50"),
        "Notes": "Requires controlled watering"
    },
    {
        "Vegetable Name": "Eggplant (Trorlong)",
        "Planting Season": ["Year-round"],
        "Harvest Time": convert_harvest_time("Continuous harvest"),
        "Growth Duration": convert_duration("3-4 months"),
        "Price per KG (USD)": convert_price("1.50 - 2.00"),
        "Notes": "Prefers warm temperatures"
    },
    {
        "Vegetable Name": "Cassava",
        "Planting Season": convert_season("Dec - Mar"),
        "Harvest Time": convert_harvest_time("6-8 months"),
        "Growth Duration": convert_duration("6-9 months"),
        "Price per KG (USD)": convert_price("0.70 - 1.00"),
        "Notes": "Drought-resistant"
    },
    {
        "Vegetable Name": "Sweet Potatoes",
        "Planting Season": convert_season("Dec - Mar"),
        "Harvest Time": convert_harvest_time("3-5 months"),
        "Growth Duration": convert_duration("3-5 months"),
        "Price per KG (USD)": convert_price("1.00 - 1.50"),
        "Notes": "Requires little water"
    },
    {
        "Vegetable Name": "Corn",
        "Planting Season": convert_season("Dec - Feb"),
        "Harvest Time": convert_harvest_time("2-3 months"),
        "Growth Duration": convert_duration("2-3 months"),
        "Price per KG (USD)": convert_price("0.80 - 1.20"),
        "Notes": "Needs irrigation"
    },
    {
        "Vegetable Name": "Mango",
        "Planting Season": convert_season("Dec - Jan"),
        "Harvest Time": convert_season("Mar - May"),
        "Growth Duration": convert_duration("3-5 months"),
        "Price per KG (USD)": convert_price("1.50 - 3.00"),
        "Notes": "Peak fruit season"
    },
    {
        "Vegetable Name": "Banana",
        "Planting Season": ["Year-round"],
        "Harvest Time": ["Year-round"],
        "Growth Duration": convert_duration("4-6 months"),
        "Price per KG (USD)": convert_price("0.50 - 1.00"),
        "Notes": "Grows well in dry season"
    },
    {
        "Vegetable Name": "Papaya",
        "Planting Season": ["Year-round"],
        "Harvest Time": convert_harvest_time("Before ripe (6-9m)"),
        "Growth Duration": convert_duration("6-9 months"),
        "Price per KG (USD)": convert_price("0.90 - 1.30"),
        "Notes": "High demand for green papaya"
    },
    {
        "Vegetable Name": "Lemongrass",
        "Planting Season": ["Year-round"],
        "Harvest Time": convert_harvest_time("Continuous harvest"),
        "Growth Duration": convert_duration("8-10 months"),
        "Price per KG (USD)": convert_price("0.50 - 0.80"),
        "Notes": "Drought-tolerant"
    },
    {
        "Vegetable Name": "Kaffir Lime Leaves",
        "Planting Season": ["Year-round"],
        "Harvest Time": ["Continuous"],
        "Growth Duration": "Continuous",
        "Price per KG (USD)": convert_price("0.30 - 0.50"),
        "Notes": "Used for curries"
    },
    {
        "Vegetable Name": "Peanuts",
        "Planting Season": convert_season("Nov - Feb"),
        "Harvest Time": convert_harvest_time("Harvest 3-4 months"),
        "Growth Duration": convert_duration("3-4 months"),
        "Price per KG (USD)": convert_price("1.20 - 1.60"),
        "Notes": "Requires well-drained soil"
    },
    {
        "Vegetable Name": "Taro",
        "Planting Season": convert_season("Dec - Mar"),
        "Harvest Time": convert_harvest_time("6-9 months"),
        "Growth Duration": convert_duration("6-9 months"),
        "Price per KG (USD)": convert_price("1.50 - 2.50"),
        "Notes": "Grows near water sources"
    }
]

with open('d:/Learn Year 2/OOP_Project/vegetables.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)