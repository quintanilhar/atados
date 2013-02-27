import datetime
from haystack import indexes
from atados.project.models import Project


class ProjectIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='details')

    def get_model(self):
        return Project
