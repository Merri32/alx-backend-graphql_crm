import graphene
from crm.schema import CRMQuery  # make sure CRMQuery comes from your crm app

class Query(CRMQuery, graphene.ObjectType):
    hello = graphene.String(default_value="Hello World")

schema = graphene.Schema(query=Query)
