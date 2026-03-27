# Simple shopping list manager
import json
from pathlib import Path

class ShoppingList:
    def __init__(self, filename=None):
        base_folder = Path(__file__).resolve().parent
        self.path = base_folder / (filename or 'shopping_list.json')
        self.items = []
        self.load()

    def load(self):
        if self.path.exists():
            try:
                with self.path.open('r', encoding='utf-8') as f:
                    self.items = json.load(f)
                    if not isinstance(self.items, list):
                        self.items = []
            except (json.JSONDecodeError, IOError):
                self.items = []
        else:
            self.items = []

    def save(self):
        with self.path.open('w', encoding='utf-8') as f:
            json.dump(self.items, f, ensure_ascii=False, indent=2)

    def add_item(self, item: str):
        item = item.strip()
        if item and item not in self.items:
            self.items.append(item)
            self.save()

    def remove_item(self, item: str):
        item = item.strip()
        if item in self.items:
            self.items.remove(item)
            self.save()

    def clear(self):
        self.items = []
        self.save()

    def get_items(self):
        return list(self.items)


if __name__ == '__main__':
    shopping_list = ShoppingList()

    print('Simple Shopping List Manager')
    print('Commands: add <item>, remove <item>, list, clear, exit')

    while True:
        command = input('> ').strip()
        if command == 'exit':
            break
        if command == 'list':
            print('\n'.join(f'- {i}' for i in shopping_list.get_items()) or '(empty)')
            continue
        if command == 'clear':
            shopping_list.clear()
            print('List cleared.')
            continue

        if command.startswith('add '):
            shopping_list.add_item(command[4:])
            print('Added.')
            continue

        if command.startswith('remove '):
            shopping_list.remove_item(command[7:])
            print('Removed (if existed).')
            continue

        print('Unknown command, try add/remove/list/clear/exit')
