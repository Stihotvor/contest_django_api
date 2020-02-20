import requests
import csv

from netcovapp.models import Coverage, Operator, City
from netcovapp.services.location_tools import lambert93_to_gps


def __request_list() -> list:
    CSV_URL = 'https://www.data.gouv.fr/s/resources/monreseaumobile/20180228-174515/2018_01_Sites_mobiles_2G_3G_4G_France_metropolitaine_L93.csv'

    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=';')
        my_list = list(cr)
        my_list.pop(0)

    return my_list


def __location_to_city(x: float, y: float) -> str:
    URL = f"https://api-adresse.data.gouv.fr/reverse/?lon={y}&lat={x}"
    response = requests.get(URL).json()
    return response['features'][0]['properties']['city']


def update_coverage():
    my_list = __request_list()[:10]

    Coverage.objects.all().delete()

    obj_list = []
    for line in my_list:
        try:
            x_wsg, y_wsg = lambert93_to_gps(float(line[1]), float(line[2]))
            operator = Operator.objects.get(code=int(line[0]))
            city, created = City.objects.get_or_create(name=__location_to_city(x_wsg, y_wsg))

            coverage_obj = Coverage(operator=operator,
                                    city=city,
                                    net_2g=(line[3] == '1'),
                                    net_3g=(line[4] == '1'),
                                    net_4g=(line[5] == '1'))
            obj_list.append(coverage_obj)
        except Exception as e:
            pass

    Coverage.objects.bulk_create(obj_list)