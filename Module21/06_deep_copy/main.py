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
        return site

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, meaning)
            if result:
                return site


# site_copy = copy.deepcopy(site)  копировать надо каждый раз передавая данные функции find_key
number_sites = int(input('Сколько сайтов: '))
for _ in range(number_sites):
    product_name = input('Введите название продукта для нового сайта: ')
    key_sites = {'title': f'Куплю/продам {product_name} недорого', 'h2': f'У нас самая низкая цена на {product_name}'}
    for i in key_sites:
        new_site = find_key(copy.deepcopy(site), i, key_sites[i])  # показал

    print(f'Сайт для {product_name}:')
    print(new_site)
