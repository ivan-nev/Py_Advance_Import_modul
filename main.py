from application.salary import calculate_salary as cal
from application.db.people import get_employees, Lion
import openweather_api



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cal('Bob')
    get_employees()
    Lion()

    print(openweather_api.__version__)
