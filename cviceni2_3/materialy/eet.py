import json
import os

DATA_PATH = './data.json'


def is_int(x):
    return str(x).isnumeric()


def is_float(x):
    parts = x.split('.')
    return len(parts) == 2 and parts[0].isnumeric() and (parts[1].isnumeric or parts[1] == '')


def print_options():
    print('h - print this window\n'
          'l - list stock\n'
          'as - add/update stock\n'
          'am - add money\n'
          'd - delete money\n'
          's - sell stock\n'
          'q - quit')


def _load_data():
    if not os.path.exists(DATA_PATH):
        return {}
    with open(DATA_PATH, 'r') as data_file:
        return json.load(data_file)


def _unify_stock_list(stock_data):
    result = []
    added = set()
    for good in stock_data:
        d = {'stock_name': good['stock_name'], 'stock_price': int(good['stock_price']), 'stock_quantity': 0.0,
             'quantity_unit': good['quantity_unit']}
        for other in stock_data:
            if d['stock_name'] in added:
                break
            if other['stock_name'] == d['stock_name']:
                d['stock_quantity'] += float(other['stock_quantity'])
        else:
            added.add(d['stock_name'])
            if abs(d['stock_quantity']) > 1e-15:
                result.append(d)
    return result


def list_stock():
    data = _load_data()
    if not data:
        print('No data yet.')
    else:
        print(data)


def _write_to_file(stock):
    if isinstance(stock, list) and len(stock) == 0:
        return
    data = _load_data()
    if isinstance(stock, list):
        if not data:
            data = {'stock': _unify_stock_list(stock)}
        else:
            if 'stock' in data:
                stock += data['stock']
            data['stock'] = _unify_stock_list(stock)
    elif isinstance(stock, int):
        if not data:
            data['cash_desk'] = stock
        else:
            if 'cash_desk' in data:
                stock = int(stock) + int(data['cash_desk'])
            data['cash_desk'] = int(stock)
    with open(DATA_PATH, 'w') as data_file:
        json.dump(data, data_file)


def _get_input(input_text, error_text, *test_functions):
    while True:
        user_input = input(input_text)
        for func in test_functions:
            if not func(user_input):
                print(error_text)
                break
        else:
            return user_input


def add_stock():
    new_stock = []
    while True:
        stock = {'stock_name': input('Stock name: '),
                 'stock_price': _get_input('Stock price for 1 unit: ', 'Wrong price', is_int, lambda x: int(x) >= 0),
                 'stock_quantity': _get_input('Stock quantity: ', 'Wrong quantity', lambda x: is_int(x) or is_float(x),
                                              lambda x: float(x) >= 0.0),
                 'quantity_unit': input('Quantity unit: ')
                 }
        while True:
            next_stock = input('Do you want to add next stock? [y/n]: ')
            if next_stock.lower() not in ['y', 'n']:
                print('Please enter y or n')
            else:
                break
        new_stock.append(stock)
        if next_stock == 'n':
            break
    _write_to_file(new_stock)


def add_money():
    amount = _get_input('Enter amount: ', 'Amount is not valid', lambda x: is_int(x) and int(amount) >= 0)
    _write_to_file(int(amount))


def del_money():
    data = _load_data()
    if 'cash_desk' not in data:
        print('You have no money in cash desk')
        return
    amount = _get_input('Enter amount: ', 'Amount is not valid', lambda x: is_int(x) and int(x) >= 0,
                        lambda x: int(data['cash_desk']) >= int(x))
    _write_to_file(-int(amount))


def _get_stock(name, data=None):
    if not data:
        data = _load_data()
    if 'stock' in data:
        for good in data['stock']:
            if name == good['stock_name']:
                return good
    return {}


def sell_stock():
    while True:
        data = _load_data()
        if 'stock' not in data:
            print('You have no goods in stock')
            return
        stock = {
            'stock_name': input('Stock name: '),
        }
        good = _get_stock(stock['stock_name'], data)
        if not good:
            print('No good with this name')
            continue
        print('good: ', good)
        stock['stock_quantity'] = _get_input('Quantity: ', 'Wrong quantity', lambda x: is_float(x) or is_int(x),
                                             lambda x: good['stock_quantity'] >= float(x))
        good['stock_quantity'] = -float(stock['stock_quantity'])
        print(f'selling for {float(stock["stock_quantity"]) * float(good["stock_price"])}')
        _write_to_file([good])
        _write_to_file(int(float(stock["stock_quantity"]) * float(good["stock_price"])))
        while True:
            next_stock = input('Do you want to sell next stock? [y/n]: ')
            if next_stock.lower() not in ['y', 'n']:
                print('Please enter y or n')
            else:
                break
        if next_stock == 'n':
            break


def handle_input():
    user_input = input('Enter input option (h for help): ')
    if user_input in input_helper:
        input_helper[user_input]()
    else:
        print('Wrong option')
        print_options()


def quit_app():
    import sys
    sys.exit(0)


def app():
    while True:
        handle_input()


input_helper = {
    'h': print_options,
    'l': list_stock,
    'as': add_stock,
    'am': add_money,
    'd': del_money,
    's': sell_stock,
    'q': quit_app,
}

if __name__ == '__main__':
    app()
