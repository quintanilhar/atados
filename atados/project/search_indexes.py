import datetime
from haystack import indexes
from atados.project.models import ProjectWork, ProjectDonation


class ProjectDonationIndex(indexes.RealTimeSearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='details')

    def get_model(self):
        return ProjectDonation

class ProjectWorkIndex(indexes.RealTimeSearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, model_attr='details')

    def get_model(self):
        return ProjectWork
