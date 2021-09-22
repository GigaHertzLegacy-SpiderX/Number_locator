#phone_information

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from geopy.geocoders import Nominatim
from countryinfo import CountryInfo

#Font
color_start = '\033[1;36m'
color_end = '\033[1;0m'

bold_start = '\033[1m'
bold_end = '\033[0m'

#Getting_number

try:
    print()
    user_input = input(f"{color_start}Enter the User Number With Country Code : {color_end}")
    user_mobile_number = phonenumbers.parse(user_input)

#getting_info for capitaol
    country_name = geocoder.description_for_number(user_mobile_number, 'en')
    capital = CountryInfo(country_name).capital()

#Country, Sim Provider
    print("")
    print(bold_start, "Country      : ", bold_end, end=" ")
    print(geocoder.description_for_number(user_mobile_number, "en"))
    print(bold_start, "Capital City : ", bold_end, end=" ")
    print(capital)
    print(bold_start, "Sim Provider : ", bold_end, end=" ")
    print(carrier.name_for_number(user_mobile_number, "en"))
# initialize Nominatim API
    geolocator = Nominatim(user_agent="NumberTracer")

    location = geolocator.geocode(geocoder.description_for_number(user_mobile_number, 'en'))
    # print(location.latitude, location.longitude)
    print(bold_start, f"Latitude     :", bold_end, f" {location.latitude} ")
    print(bold_start, f"Longtitude   :", bold_end, f" {location.longitude} ")

    location = geolocator.reverse(str(location.latitude) + "," + str(location.longitude))

    address = location.raw['address']

    # traverse the data
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    code = address.get('country_code')
    zipcode = address.get('postcode')
    print(bold_start, 'City         : ', bold_end, f"{city}")
    print(bold_start, 'State        : ', bold_end, f"{state}")
    print(bold_start, 'Country      : ', bold_end, f"{country}")
    print(bold_start, 'Zip Code     : ', bold_end, f"{zipcode}")
    print("\n")
    print("   -----Attack Done!-----")

    print("              *  ")
    print("            ** **")
    print("          ***   *** ")
    print("            ** ** ")
    print("              * ")
    print("              *")
    print("              *")
    print("             ***")
    print("            * * *")
    print("          *   *   *")
    print("         *    *     *")
    print("     *  *     *      *  *")
    print("      *       *        *")
    print("              *        ")
    print("              *        ")
    print("              *        ")
    print("            *   *       ")
    print("          *       *      ")
    print("        *           *    ")
    print("      *               *   ")
    print("    *                   *    ")

except:
    print("\n")
    print(bold_start, "-------------------------------Error !-------------------------------", bold_end)
    print()
    print(bold_start, "                   $ Write The Number Correctly $", bold_end)
    print("\n")
