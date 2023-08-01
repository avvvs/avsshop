# graph_models.py
from django_extensions.management.commands.graph_models import Command as GraphModelsCommand
from django.core.management import call_command
import os


def generate_graph_models():
    command = GraphModelsCommand()
    options = {
        'all_applications': True,
        'output': os.path.join(os.getcwd(), 'db_schema.dot')
    }
    command.run_from_argv(['manage.py', 'graph_models'], options)


generate_graph_models()
