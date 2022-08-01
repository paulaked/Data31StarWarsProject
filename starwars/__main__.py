from etl import extract
import requests

if __name__ == '__main__':
    starship_data = extract()
    print(starship_data)