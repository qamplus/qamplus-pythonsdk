
class VoiceClient(object):


    def __init__(self, base_obj):
        self.base_obj = base_obj
        self.api_resource = "/voice/v1/{}"

    def create(self,
               direction,
               to,
               caller_id,
               execution_logic,
               reference_logic='',
               country_iso2='us',
               technology='pstn',
               status_callback_uri=''):

        api_resource = self.api_resource.format(direction)
        return self.base_obj.post(api_resource=api_resource, direction=direction, to=to,
            caller_id=caller_id, execution_logic=execution_logic, reference_logic=reference_logic,
            country_iso2=country_iso2, technology=technology, status_callback_uri=status_callback_uri)


    def update(self, reference_id, execution_logic):
        api_resource = self.api_resource.format(reference_id)
        return self.base_obj.put(api_resource=api_resource,
                                  execution_logic=execution_logic)

    def delete(self, reference_id):
        api_resource = self.api_resource.format(reference_id)
        return self.base_obj.delete(api_resource=api_resource)

    def get_status(self, reference_id):
        api_resource = self.api_resource.format(reference_id)
        return self.base_obj.get(api_resource=api_resource)




