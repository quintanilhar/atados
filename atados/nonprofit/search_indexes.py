import datetime
from haystack import indexes
from atados.nonprofit.models import Nonprofit


class ProjectIndex(indexes.RealTimeSearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='name')

    def get_model(self):
        return Nonprofit
