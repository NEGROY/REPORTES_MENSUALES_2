# CLASE BASE PARA EL SELECT DE LOS MODELOS 
class BaseSelectService:
    model = None
    order_by = ()
    fields = ()
    filters = {}

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def get_filters(self):
        return self.filters

    def get_queryset(self):
        if self.model is None:
            raise NotImplementedError('Debe definir model.')

        queryset = self.model.objects.filter(**self.get_filters())

        if self.order_by:
            queryset = queryset.order_by(*self.order_by)

        if self.fields:
            queryset = queryset.values(*self.fields)

        return queryset

    def execute(self):
        return list(self.get_queryset())

# AGREGAREMOS EN UN FUTURO LAS CLASES DE UPDATE Y DELETE A MEDIDA QUE LAS NECESITEMOS   

# DELETE 

# UPDATE 