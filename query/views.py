from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuerySerializer
from backend_script import count_topic_wiki_occurences


# Create your views here.
class Query:
    def __init__(self, topic, section=None):
        self.topic = topic
        self.section = section
        self.hits = 0

    def execute_query(self):
        self.hits = count_topic_wiki_occurences(self.topic, self.section)


@api_view()
def query_view(request):
    topic = request.GET.get("topic")
    section = request.GET.get("section", None)

    query = Query(topic, section)
    query.execute_query()

    serializer = QuerySerializer(query)
    return Response(serializer.data)