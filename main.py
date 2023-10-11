from typing import List, Tuple

MAX_PROFIT_SHOP_POSITION = 0


def calculate_profit_for_shopping(
        shopping_list: List[str], price_list: List[Tuple[str, List[Tuple[str, int]]]]
) -> Tuple[List[Tuple[str, int, List[str]]], str, int]:
    total_prices_of_shops = []

    for price_info in price_list:
        total_price = 0
        not_found_products_in_shop = []
        shop_name, prices = price_info

        for product in shopping_list:
            is_product_found = False

            for product_info in prices:
                product_name, product_price = product_info

                if product == product_name:
                    total_price += product_price
                    is_product_found = True
                    break

            if not is_product_found:
                not_found_products_in_shop.append(product)

        total_prices_of_shops.append((shop_name, total_price, not_found_products_in_shop))
        total_prices_of_shops.sort(key=lambda shop: shop[1])

    max_profit_shop_name, profit_price, _ = total_prices_of_shops[MAX_PROFIT_SHOP_POSITION]

    return total_prices_of_shops, max_profit_shop_name, profit_price


def user_input():
    my_price_list = []
    print('Введите желаемые покупки через пробел. Пример ввода: банан макароны яблоки сыр морковь молоко рыба')
    my_shopping_list = input().split()
    print('Введите количество магазинов в списке цен. Пример ввода: 2')
    len_price_list = int(input())

    if len_price_list < 1:
        print('Недостаточное количество магазинов для сравнения. Необходимо минимум 1')
        return

    for i in range(len_price_list):
        print(f'Введите список цен в магазине {i + 1}.')
        print('Введите наименование магазина. Пример ввода: вкусвилл')
        shop_name = input()
        print(f'Введите цены в магазине {i + 1}. Пример ввода: банан 23, молоко 60, рыба 300, яблоки 240')
        raw_price_info = input().split(', ')
        price_info = []

        for raw_price in raw_price_info:
            product_name, price = raw_price.split()
            price_info.append((product_name, int(price)))

        print('---------------------------------------')

        my_price_list.append((shop_name, price_info))

    return my_shopping_list, my_price_list


if __name__ == '__main__':
    my_shopping_list, my_price_list = user_input()

    shops_info, max_profit_shop_name, profit_price = calculate_profit_for_shopping(
        shopping_list=my_shopping_list, price_list=my_price_list
    )

    print('Итоговая стоимость покупок в магазинах:')
    for shop in shops_info:
        shop_name, price_info, not_found_products = shop
        print(f'Наименование магазина: {shop_name}, Общая цена покупок: {price_info}, Ненайденные продукты: {not_found_products}')
        print('---------------------------------------')

    print(f'Вы потратите меньше всего денег в магазине: {max_profit_shop_name}\nОбщая цена покупок составит: {profit_price} руб.')
