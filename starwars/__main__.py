from etl import extract, transform
import requests

if __name__ == '__main__':
    starship_data = extract()
    trans_starship = transform(starship_data)
    load(trans_starship)