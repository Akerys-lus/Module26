import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def find_key(struct, key, meaning):
    if key in struct:
        struct[key] = meaning
        return site_copy

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, meaning)
            if result:
                return site


site_copy = copy.deepcopy(site)
number_sites = int(input('Сколько сайтов: '))
for _ in range(number_sites):
    product_name = input('Введите название продукта для нового сайта: ')
    key_sites = {'title': f'Куплю/продам {product_name} недорого', 'h2': f'У нас самая низкая цена на {product_name}'}
    for i in key_sites:
        find_key(site_copy, i, key_sites[i])

    print(f'Сайт для {product_name}:')
    print(site)
