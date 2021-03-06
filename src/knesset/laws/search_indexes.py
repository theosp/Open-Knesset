import datetime
from haystack import indexes
from haystack import site
from knesset.laws.models import Vote, Bill


class VoteIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    time = indexes.DateTimeField(model_attr='time')
    title = indexes.CharField(model_attr='title')

    def get_queryset(self):
        """Used when the entire index for model is updated."""
        return Vote.objects.all() 


site.register(Vote, VoteIndex)

class BillIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')

    def get_queryset(self):
        """Used when the entire index for model is updated."""
        return Bill.objects.all() 

site.register(Bill, BillIndex)

