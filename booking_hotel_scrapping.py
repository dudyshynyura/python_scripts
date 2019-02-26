import requests
from bs4 import BeautifulSoup

"""
Getting hotel data by url from booking.com
"""

def set_data_to_dict(dict, data, title, check_string):
    """Create dict and set data to it.
    Getting:
    dict - destination dictionary,
    data - value,
    title - key,
    check_string - for boolean type string to check for present in data
    """
    try:
        if check_string:
            dict.update({title: check_string in data.text})
        else:
            dict.update({title: ' '.join(data.text.split())})
    except AttributeError:
        if check_string:
            dict.update({title: "False"})
        else:
            dict.update({title: "None"})

def get_hotel_information(url):
    """Parsing html page and getting data. Getting url of hotel page.
    Return: dict or None. None if hotel already saved.
    """
    hotel = {}
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    name = html.find("h2", {"id": "hp_hotel_name"})
    address = html.find("span", {"class": "hp_address_subtitle js-hp_address_subtitle jq_tooltip"})
    children = html.find("div", {"id": "children_policy"})
    mark = html.find("div", {"class": "bui-review-score__badge"})
    pets = html.find("div", {"data-section-id": "-2"})
    restaurant = html.find("div", {"data-section-id": "7"})
    pool_and_spa = html.find("div", {"data-section-id": "21"})
    shuttle = html.find("span", {"class": "facility-badge__tooltip-title"})
    description = html.find("div", {"id": "summary"})
    preview_img_url = html.find("img", {"alt": "Gallery image of this property"})

    set_data_to_dict(hotel, name, "name", None)
    set_data_to_dict(hotel, address, "address", None)
    set_data_to_dict(hotel, description, "description", None)
    set_data_to_dict(hotel, mark, "mark", None)
    set_data_to_dict(hotel, shuttle, "shuttle", None)
    set_data_to_dict(hotel, children, "children_allowed", "All children are welcome.")
    set_data_to_dict(hotel, pets, "pets_allowed", "Pets are not allowed.")
    set_data_to_dict(hotel, restaurant, "has_restaurant", "Restaurant")
    set_data_to_dict(hotel, pool_and_spa, "has_pool", "Swimming pool")
    set_data_to_dict(hotel, pool_and_spa, "has_spa", "Spa")

    hotel.update({"img_url": preview_img_url["src"]})

    return hotel

def main():
    hotel_url = """ https://www.booking.com/hotel/ua/hostel-sun.html?aid=304142;
    label=gen173nr-1FCAso6QFCBnRhdXJ1c0gzWARo6QGIAQGYATG4ARnIAQzYAQHoAQH4AQKIAg
    GoAgM;sid=c4b6bd482c32ffd883bb8d1fed21a034;dest_id=-1045268;dest_type=city;
    dist=0;group_adults=2;hapos=1;hpos=1;room1=A%2CA;sb_price_type=total;
    sr_order=popularity;srepoch=1551114961;srpvid=a5497968a83a0001;type=total;
    ucfs=1&#hotelTmpl
    """

    data = get_hotel_information(hotel_url)
    print(data)

if __name__ == "__main__":
    main()
