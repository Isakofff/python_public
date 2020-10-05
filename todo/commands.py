# -*- coding: utf-8 -*-

from custom_exceptions import UserExitException
from utils import get_input_function


class BaseCommand(object):
    @staticmethod
    def label():
        raise NotImplemented()

    def perform(self, objects, *args, **kwargs):
        raise NotImplemented()


class ListCommand(BaseCommand):
    @staticmethod
    def label():
        return 'list'

    def perform(self, objects, *args, **kwargs):
        if len(objects) == 0:
            print('There are no items in storage.')
            return

        for index, obj in enumerate(objects):
            print(f'{index}: {str(obj)}')


class NewCommand(BaseCommand):
    @staticmethod
    def label():
        return 'new'

    @staticmethod
    def _load_item_classes():
        from models import ToDoItem, ToBuyItem, ToReadItem

        return {
            'ToDoItem': ToDoItem,
            'ToBuyItem': ToBuyItem,
            'ToReadItem': ToReadItem
        }

    def perform(self, objects, *args, **kwargs):
        classes = self._load_item_classes()

        print('Select item type:')
        for index, name in enumerate(classes.keys()):
            print(f'{index}: {name}')

        input_function = get_input_function()
        selection = None
        selected_key = None

        while True:
            try:
                selection = int(input_function('Input number: '))
                selected_key = list(classes.keys())[selection]
                break
            except ValueError:
                print('Bad input, try again.')
            except IndexError:
                print('Wrong index, try again.')

        selected_class = classes[selected_key]
        print(f'Selected: {selected_class.__name__}')
        print()

        new_object = selected_class.construct()

        objects.append(new_object)
        print(f'Added {str(new_object)}')
        print()
        return new_object


class ExitCommand(BaseCommand):
    @staticmethod
    def label():
        return 'exit'

    def perform(self, objects, *args, **kwargs):
        raise UserExitException('See you next time!')


class DoneCommand(BaseCommand):
    state = True

    @staticmethod
    def label():
        return 'done'

    def perform(self, objects, *args, **kwargs):
        # debug
        # check arguments
        # print(self, objects, args, kwargs)
        # check the lenght - it will be more and more after each 'new'
        #print(self, len(objects))
        # iterate all the objects in storage
        # for obj in objects:
        #     print(obj, obj.done)

        ListCommand().perform(objects)

        try:
            index = int(input('Input object index: '))
            objects[index].done = self.state
        except IndexError:
            print('Wrong index!')
        except ValueError:
            print('Input number!')

class UnDoneCommand(DoneCommand):
    state = False

    @staticmethod
    def label():
        return 'undone'


