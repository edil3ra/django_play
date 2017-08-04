from django.core.management.base import BaseCommand
from ...models import Note


class Command(BaseCommand):
    help = "My fixture for cookbook."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.stdout.write('start drop')
        self.drop()
        self.stdout.write('end drop')

        self.stdout.write('start create')
        self.create()
        self.stdout.write('end create')



        
    def create(self):
        note1 = Note(title='cherry', description='This is the most tastefull cherry you ever tasted')
        
        note2 = Note(title='pear', description='This pear will give you strange feeling in your belly')

        note3 = Note(title='banana', description='Try to talk with a banana in your mouth')

        for note in [note1, note2, note3]: note.save()
        

    def drop(self):
        Note.objects.all().delete()
