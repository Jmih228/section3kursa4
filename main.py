import json
from datetime import *


def load_operations():
    with open("operations.json", encoding="utf-8") as operations:
        return json.load(operations)


operations_wo_empty_dict = [transaction for transaction in load_operations() if transaction]


def operation_sort(collection):

    sorted_operations = sorted(collection, key=lambda x: datetime.strptime(x['date'][:-7], '%Y-%m-%dT%H:%M:%S'), reverse=True)

    print(sorted_operations[:5])

    for operation in sorted_operations[:5]:
        print(f'{".".join(operation["date"][:10].split("-")[::-1])} {operation["description"]}')
        sendler = operation.get('from', '')
        reciver = operation["to"].split()

        if sendler and sendler.startswith('Счет'):
            print(f'Счет **{sendler[-4:]}', end=' -> ')
        elif sendler:
            hidden_sendler_number = sendler[-16:-10] + '*' * 6 + sendler[-4:]
            print(*sendler.split()[:-1], end=' ')
            [print(hidden_sendler_number[i:i + 4], end=" ") for i in range(0, 13, 4)]
            print('-> ', end='')
        if reciver[0] == ("Счет"):
            print(f'Счет **{reciver[1][-4:]}')
        else:
            hidden_reciver_number = reciver[-1][:6] + '*'*6 + reciver[-1][-4:]
            print(*reciver[:-1], end=' ')
            [print(hidden_reciver_number[i:i + 4], end=" ")for i in range(0, 13, 4)]
            print()
        print(f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}', end='\n\n')

    return sorted_operations[:5]
