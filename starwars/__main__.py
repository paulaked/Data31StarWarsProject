from app import requesting_sw
from unittest import main
import sys
import io

if __name__ == '__main__':

    # Set up database.
    db = requesting_sw.set_up_db()

    # Download, transform and insert data.
    requesting_sw.dl_trans_ins(db)

    # Output transformed series.
    requesting_sw.read_from_db(db)

    # Suppress output.
    suppress_text = io.StringIO()
    sys.stdout = suppress_text

    # Run tests
    main(module='Test_Plan', exit=False)

    # Release output.
    sys.stdout = sys.__stdout__
