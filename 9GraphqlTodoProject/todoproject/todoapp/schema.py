
import graphene
from graphene_django import DjangoObjectType
from .models import  Todo


# Defining the Todo_type or let's say the schema
class TodoType(DjangoObjectType):
    class Meta:
        model=Todo
        fields=("id","title","description","completed","created_at")

#Now defining the queries
class Query(graphene.ObjectType):
    all_todos=graphene.List(TodoType)  #fetching the all to_do's  from the server
    todo=graphene.Field(TodoType,id=graphene.ID(required=True)) # fetching the single to_do

    def resolve_all_todos(root,info): #function for fetching all the to-do's
        return Todo.objects.all()

    def resolve_single_todo(root,info,id): #function for fetching the single to-do
        try:
            return Todo.objects.get(pk=id)
        except Todo.DoesNotExist:
            return None




#Now creating the mutations for the rest actions such as creating, deleting and updating the database.
class CreateTodo(graphene.Mutation):
    todo=graphene.Field(TodoType)
    class Arguments:
        title=graphene.String(required=True)
        description=graphene.String()
    def mutate(self, info, title, description=None):
        todo = Todo(title=title, description=description)  # creating the object of newly created todo
        todo.save()  # saving it in the database.
        return CreateTodo(todo=todo)



class UpdateTodo(graphene.Mutation):
    todo=graphene.Field(TodoType)
    class Arguments:
        id=graphene.ID(required=True)
        title=graphene.String()
        description=graphene.String()
        completed=graphene.Boolean()

    def mutate(self, info, id, title=None, description=None, completed=None):
        try:
            todo = Todo.objects.get(pk=id)
        except Todo.DoesNotExist:
            raise Exception("Todo not found in database")
        if title is not None:  # if i got some arguments for update then update.
            todo.title = title
        if description is not None:
            todo.description = description
        if completed is not None:
            todo.completed = completed

        todo.save()  # after updating saving the data in db.
        return UpdateTodo(todo=todo)


class DeleteTodo(graphene.Mutation):
    ok=graphene.Boolean()
    class Arguments:
        id=graphene.ID(required=True)
    def mutate(self,info,id):
        try:
            todo=Todo.objects.get(pk=id)
            todo.delete() #deleting the to-do after getting it from the id .
            return DeleteTodo(ok=True)
        except Todo.DoesNotExist:
            return DeleteTodo(ok=False)


#now finally i am defining the mutation class .

class Mutation (graphene.ObjectType):
    create_todo=CreateTodo.Field()
    update_todo=UpdateTodo.Field()
    delete_todo=DeleteTodo.Field()

#Defining the schema

schema=graphene.Schema(query=Query,mutation=Mutation)