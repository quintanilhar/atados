import datetime
from haystack import indexes
from atados.organisation.models import Organisation


class ProjectIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='name')

    def get_model(self):
        return Organisation
