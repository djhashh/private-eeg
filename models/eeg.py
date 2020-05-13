import torch
from torch import nn, optim
import torch.nn.functional as F


class EEG_CNN(nn.Module):
    def __init__(self):
        super(EEG_CNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 64, 3, 1)
        self.conv2 = nn.Conv2d(64, 64, 3, 1)
        self.fc1 = nn.Linear(4*4*50, 64)
        self.fc2 = nn.Linear(64, 7)

    def forward(self, x):
        x = x.view(-1, 3, 224, 224)
        x = self.conv1(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2, 2)
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, 2, 2)
        x = x.view(-1, 4*4*50)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)
#
#
# def build_model():
#     net = {}
#     net['input'] = InputLayer((None, 3, 224, 224), input_var=input_var)
#     net['conv1_1'] = ConvLayer(
#         net['input'], 64, 3, pad=1, flip_filters=False)
#
#     net['conv1_2'] = ConvLayer(
#         net['conv1_1'], 64, 3, pad=1, flip_filters=False)
#
#     net['pool1'] = PoolLayer(net['conv1_2'], 2)
#     net['conv2_1'] = ConvLayer(
#         net['pool1'], 128, 3, pad=1, flip_filters=False)
#
#     net['conv2_2'] = ConvLayer(
#         net['conv2_1'], 128, 3, pad=1, flip_filters=False)
#     net['pool2'] = PoolLayer(net['conv2_2'], 2)
#
#     net['conv3_1'] = ConvLayer(et['pool2'], 256, 3, pad=1, flip_filters=False)
#     net['conv3_2'] = ConvLayer(
#         net['conv3_1'], 256, 3, pad=1, flip_filters=False)
#     net['conv3_3'] = ConvLayer(
#         net['conv3_2'], 256, 3, pad=1, flip_filters=False)
#     net['pool3'] = PoolLayer(net['conv3_3'], 2)
#     net['conv4_1'] = ConvLayer(
#         net['pool3'], 512, 3, pad=1, flip_filters=False)
#     net['conv4_2'] = ConvLayer(
#         net['conv4_1'], 512, 3, pad=1, flip_filters=False)
#     net['conv4_3'] = ConvLayer(
#         net['conv4_2'], 512, 3, pad=1, flip_filters=False)
#     net['pool4'] = PoolLayer(net['conv4_3'], 2)
#     net['conv5_1'] = ConvLayer(
#         net['pool4'], 512, 3, pad=1, flip_filters=False)
#     net['conv5_2'] = ConvLayer(
#         net['conv5_1'], 512, 3, pad=1, flip_filters=False)
#     net['conv5_3'] = ConvLayer(
#         net['conv5_2'], 512, 3, pad=1, flip_filters=False)
#     net['pool5'] = PoolLayer(net['conv5_3'], 2)
#     net['fc6'] = DenseLayer(net['pool5'], num_units=4096)
#     net['fc6_dropout'] = DropoutLayer(net['fc6'], p=0.5)
#     net['fc7'] = DenseLayer(net['fc6_dropout'], num_units=4096)
#     net['fc7_dropout'] = DropoutLayer(net['fc7'], p=0.5)
#     net['fc8'] = DenseLayer(
#         net['fc7_dropout'], num_units=output_nodes, W=lasagne.init.GlorotNormal(), nonlinearity=None)
#     net['prob'] = NonlinearityLayer(net['fc8'], softmax)
#     l_out = net['prob']