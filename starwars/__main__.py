from unittest import main
import sys
import io

if





def tests():
    # Suppress output.
    suppress_text = io.StringIO()
    sys.stdout = suppress_text

    # Run tests
    main(module='Test_Plan', exit=False)

    # Release output.
    sys.stdout = sys.__stdout__
