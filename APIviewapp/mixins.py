from django.core.serializers import serialize
import json
class SerializeMixin(object):
    def serialize(self, qs, json_data=None):
        pdict=json.loads(json_data)
        final_list=[]
        for  object in pdict:
            final_list.append(object['fields'])
        json_data=json.dumps(final_list)
        return json_data
from django.http import HttpResponse
class HttpResponseMixin(object):
    def render_to_http_response(self,data,status=200):
        return HttpResponse(data,content_type='application/json',status=status)