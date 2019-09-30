class connections:
    '''This class ensures that multiple connections are not
    established. It stores objects in memory so reconnections to server
    can't be established.
    
    There needs to be some "metadata" to check if the object does exist.
    '''
    
    _spc_objects = []
    
    def append_spc_object(self, obj):
       self._spc_objects.append(obj)
    
    def search_spc_objects(self, val):
        pass
