# -*- coding: utf-8 -*-
__author__ = "Isakov Anton"

"""
Main file. Contains program execution logic.
"""

from commands import (
    ListCommand,
    NewCommand,
    ExitCommand,
    DoneCommand,
    UnDoneCommand,
    UserExitException,
)
from models import (
    Storage,
)

def get_routes():
    """
    This function contains the dictionary of possible commands.
    :return: `dict` of possible commands, with the format: `name -> class`
    """

    return {
        ListCommand.label(): ListCommand,
        NewCommand.label(): NewCommand,
        ExitCommand.label(): ExitCommand,
        DoneCommand.label(): DoneCommand,
        UnDoneCommand.label(): UnDoneCommand,
    }


def perform_command(command):
    """
    Performs the command by name.
    Stores the result in `Storage()`.
    :param command: command name, selected by user.
    """

    command = command.lower()
    routes = get_routes()

    try:
        command_class = routes[command]
        command_inst = command_class()

        storage = Storage()
        command_inst.perform(storage.items)
    except KeyError:
        print('Bad command, try again.')
    except UserExitException as ex:
        print(ex)
        raise


def parse_user_input():
    """
    Gets the user input.
    :return: `str` with the user input.
    """

    input_function = input

    message = 'Input your command: (%s): ' % '|'.join(
        {
            ListCommand.label(): ListCommand,
            NewCommand.label(): NewCommand,
            ExitCommand.label(): ExitCommand,
            DoneCommand.label(): DoneCommand,
            UnDoneCommand.label(): UnDoneCommand
        }.keys()
    )
    return input_function(message)


def main():
    """
    Main method, works infinitelly until user runs `exit` command.
    Or hits `Ctrl+C` in the console.
    """

    while True:
        try:
            command = parse_user_input()
            perform_command(command)
        except UserExitException:
            break
        except Exception as e:
            print('You have done something wrong!', e)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Shutting down, bye!')
