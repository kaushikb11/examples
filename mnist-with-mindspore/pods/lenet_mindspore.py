from jina.executors.encoders.frameworks import BaseMindsporeEncoder
from jina.executors.crafters.image.io import ImageReader

import sys
sys.path.append('..')

import numpy as np

from lenet import *


class LeNetImageEncoder(BaseMindsporeEncoder):
    def encode(self, data, *args, **kwargs):
        from mindspore import Tensor
        return self.model(Tensor(data.astype('float32'))).asnumpy()

    def get_model(self):
        return LeNet5()


class MnistImageReader(ImageReader):
    def craft(self, blob, *args, **kwargs):
        # convert buffer to blob
        return dict(weight=1., blob=np.stack(blob.reshape(28, 28)))
