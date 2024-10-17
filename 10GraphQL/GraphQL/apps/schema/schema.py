import graphene
from graphene_django import DjangoObjectType
from apps.users.models import User
from apps.decks.models import Deck
from apps.cards.models import Card


class UserType(DjangoObjectType):
    class Meta:
        model = User


class DeckType(DjangoObjectType):
    class Meta:
        model = Deck


class CardType(DjangoObjectType):
    class Meta:
        model = Card


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    decks = graphene.List(DeckType)
    cards = graphene.List(CardType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_decks(self, info, **kwargs):
        return Deck.objects.all()

    def resolve_cards(self, info, **kwargs):
        return Card.objects.all()


class CreateCard(graphene.Mutation):
    card = graphene.Field(CardType)  # empty field like structure

    class Arguments:
        question = graphene.String()
        answer = graphene.String()
        deck_id = graphene.Int()

    def mutate(self, info, question, answer, deck_id):
        try:
            singledeck = Deck.objects.get(id=deck_id)
        except Deck.DoesNotExist:
            raise Exception("Deck with given id does not exist")
        card = Card(question=question, answer=answer, deck=singledeck)  # object made
        card.save()
        return CreateCard(card=card)  # and returned.


class CreateDeck(graphene.Mutation):
    deck = graphene.Field(DeckType)  # empty field like structure

    class Arguments:
        title = graphene.String()
        description = graphene.String()

    def mutate(
        self,
        info,
        title,
        description,
    ):
        d = Deck(title=title, description=description)
        d.save()
        return CreateDeck(deck=d)


class UpdateCard(graphene.Mutation):
    card = graphene.Field(CardType)

    class Arguments:
        card_id = graphene.Int(required=True)
        question = graphene.String()
        answer = graphene.String()
        deck_id = graphene.Int()

    def mutate(self, info, card_id, question=None, answer=None, deck_id=None):
        try:
            card = Card.objects.get(id=card_id)
        except Card.DoesNotExist:
            raise Exception("Card with given id doesnot exist")
        if question:
            card.question = question
        if answer:
            card.answer = answer
        if deck_id:
            try:
                deck = Deck.objects.get(id=deck_id)
                card.deck = deck
            except Deck.DoesNotExist:
                raise Exception("Deck with given id doesnot exist")
        card.save()
        return UpdateCard(card=card)


class DeleteCard(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        card_id = graphene.Int(required=True)

    def mutate(self, info, card_id):
        try:
            card = Card.objects.get(id=card_id)
            card.delete()
            return DeleteCard(success=True)
        except Card.DoesNotExist:
            raise Exception("Car with given id does not exist")


class Mutation(graphene.ObjectType):
    create_card = CreateCard.Field()
    create_deck = CreateDeck.Field()
    update_card = UpdateCard.Field()
    delete_card = DeleteCard.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
