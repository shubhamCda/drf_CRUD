import json
from django.core.serializers import serialize



class SerializeMixin(object):
    def serialize(self, emps):
        json_data = serialize('json', emps)
        p_data = json.loads(json_data)
        final_list = []
        for obj in p_data:
            emp_data = obj['fields']
            final_list.append(emp_data)
        json_data = json.dumps(final_list)
        return json_data