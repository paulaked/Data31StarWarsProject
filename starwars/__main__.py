from unittest import main
import sys
import io
from starwars.app import requesting_sw



if __name__ == '__main__':
    db_name = input()
    db = requesting_sw.db_link(db_name)
    requesting_sw.tform_in(db)
    requesting_sw.read_db(db)