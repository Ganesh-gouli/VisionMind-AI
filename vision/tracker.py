from collections import OrderedDict

class CentroidTracker:
    def __init__(self, max_disappeared=40):
        self.nextObjectID = 0
        self.objects = OrderedDict()
        self.disappeared = OrderedDict()
        self.max_disappeared = max_disappeared

    def update(self, rects):
        return self.objects
