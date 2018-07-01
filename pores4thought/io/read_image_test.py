import unittest
import numpy as np
from PIL import Image
import os


class RemoteImageReadTest(unittest.TestCase):

    def setUp(self):
        self.path = "external/s3_test_files"
        self.files = ["ThreePhase_dseg.tif", "ThreePhase.tif"]

    def test_read(self):
        for f in self.files:
            im = Image.open(os.path.join(self.path, f))
            imarray = np.array(im)
            assert imarray.shape == (256, 256)


if __name__ == "__main__":
    unittest.main()
