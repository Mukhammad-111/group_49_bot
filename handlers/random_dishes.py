from aiogram import Router, types, F
from random import choice

random_dishes_router = Router()


@random_dishes_router.callback_query(F.data == "random_dish")
async def random_dishes_handler(callback: types.CallbackQuery):
    random_recipes = {
        "alivia": {
            "caption": """Рецепт 'Оливье' (традиционный)
    Картофель (среднего размера) — 4 шт.
    Морковь — 2 шт.
    Яйца куриные — 4 шт.
    Колбаса варёная (или куриное филе) — 300 г.
    Огурцы маринованные — 4 шт.
    Горох консервированный — 1 банка (200–250 г).
    Майонез — по вкусу.
    Соль, перец — по вкусу.
    Зелень (укроп или петрушка) — для украшения.""",
            "image": "images/alivia.webp"
        },
        "beshbarmak": {
            "caption": """Рецепт "Бешбармак" (кыргызский традиционный)
    Мясо (баранина, говядина или конина) — 1,5 кг
    Лук репчатый — 3-4 шт.
    Лапша (для бешбармака) — 500 г
    Картофель (по желанию) — 4-5 шт.
    Чеснок — 2-3 зубчика
    Мука — 300 г (для домашней лапши, если делаете её сами)
    Яйцо — 1 шт. (для лапши)
    Вода — для бульона и теста
    Соль, перец — по вкусу
    Зелень (укроп, петрушка) — для подачи""",
            "image": "images/beshbarmak.jpg"
        },
        "borsh": {
            "caption": """Рецепт Борща (классический)
    Говядина на кости (или свинина) — 500-700 г
    Капуста белокочанная — 300-400 г
    Свёкла — 2 шт. (среднего размера)
    Картофель — 3-4 шт.
    Морковь — 1 шт.
    Лук репчатый — 1 шт.
    Томатная паста — 2 ст. ложки
    Помидоры (по желанию) — 1-2 шт.
    Чеснок — 2 зубчика
    Лавровый лист — 2-3 шт.
    Растительное масло — для жарки
    Соль, перец — по вкусу
    Уксус или лимонный сок — 1 ч. ложка (для сохранения цвета свёклы)
    Сметана — для подачи
    Зелень (укроп, петрушка) — для украшения""",
            "image": "images/borsh.jpg"
        },
        "fruktovyi": {
            "caption": """Рецепт Фруктового салата
    Яблоко — 1 шт.
    Банан — 1 шт.
    Апельсин — 1 шт.
    Киви — 2 шт.
    Виноград (зелёный или чёрный) — 100 г
    Клубника (по сезону) — 100 г
    Натуральный йогурт (или сметана) — 100 мл
    Мёд — 1-2 ч. ложки (по желанию)
    Лимонный сок — 1 ст. ложка (для предотвращения потемнения фруктов)""",
            "image": "images/fruktovyi.jpg"
        },
        "kuurdak": {
            "caption": """Рецепт "Куурдак" (традиционный кыргызский)
    Мясо (баранина, говядина или конина) — 500-700 г
    Лук репчатый — 3-4 шт.
    Картофель — 3-4 шт.
    Жир (курдючный или растительное масло) — 3-4 ст. ложки
    Чеснок — 2-3 зубчика
    Лавровый лист — 2 шт.
    Зира — 1 ч. ложка
    Соль, перец — по вкусу
    Зелень (укроп, петрушка) — для подачи""",
            "image": "images/kuurdak.png"
        },
        "manty": {
            "caption": """Рецепт Мантов (традиционный)
    Мука — 500 г
    Вода (тёплая) — 200 мл
    Яйцо — 1 шт.
    Соль — 1 ч. ложка
    Ингредиенты для начинки:

    Мясо (баранина или говядина с жиром) — 500 г
    Лук репчатый — 4-5 шт.
    Курдючный жир (по желанию) — 100 г
    Соль, перец чёрный молотый — по вкусу
    Зира — 1/2 ч. ложки""",
            "image": "images/manty.jpg"
        },
        "morkownyi": {
            "caption": """Рецепт Морковного салата (классический)
    Морковь — 3-4 шт. (среднего размера)
    Чеснок — 2-3 зубчика
    Майонез (или сметана) — 2-3 ст. ложки
    Соль — по вкусу
    Сахар — щепотка (по желанию)
    Лимонный сок — 1 ч. ложка (по желанию)""",
            "image": "images/morkownyi.jpg"
        },
        "pelmen": {
            "caption": """Рецепт Пельменей (классический)
    Мука — 500 г
    Вода (тёплая) — 200 мл
    Яйцо — 1 шт.
    Соль — 1 ч. ложка
    Ингредиенты для начинки:

    Говядина — 300 г
    Свинина — 200 г
    Лук репчатый — 1-2 шт.
    Чеснок — 2 зубчика
    Соль, перец — по вкусу
    Вода — 50 мл (для сочности начинки)""",
            "image": "images/pelmen.jpg"
        },
        "plow": {
            "caption": """Рецепт Плова (классический узбекский)
    Рис (длиннозёрный) — 500 г
    Мясо (баранина или говядина) — 500 г
    Лук репчатый — 2 шт.
    Морковь — 2-3 шт.
    Чеснок — 5-6 зубчиков
    Растительное масло — 100 мл
    Зира (кумин) — 1 ч. ложка
    Барбарис — 1 ч. ложка (по желанию)
    Соль — по вкусу
    Перец чёрный молотый — по вкусу
    Вода — около 1 литра (или по необходимости)""",
            "image": "images/plow.webp"
        },
        "shakarap": {
            "caption": """Рецепт Шакароба (узбекский)
    Помидоры — 4-5 шт.
    Огурцы — 2-3 шт.
    Лук репчатый — 1-2 шт.
    Сладкий перец — 1 шт.
    Кинза (петрушка) — небольшой пучок
    Чеснок — 2-3 зубчика
    Лимонный сок — 1-2 ст. ложки
    Соль — по вкусу
    Перец чёрный молотый — по вкусу
    Оливковое или растительное масло — 2-3 ст. ложки
    Вода (если нужно) — 100-150 мл""",
            "image": "images/shakarap.jpg"
        },
        "shorpo": {
            "caption": """Рецепт Супа с говядиной (кыргызский)
    Говядина (на кости) — 500 г
    Картофель — 4-5 шт.
    Морковь — 2 шт.
    Лук репчатый — 1-2 шт.
    Чеснок — 2-3 зубчика
    Помидоры — 2-3 шт.
    Лавровый лист — 2 шт.
    Соль, перец — по вкусу
    Растительное масло — 2 ст. ложки
    Зелень (петрушка или укроп) — по вкусу
    Вода — 2-2,5 литра""",
            "image": "images/shorpo.jpg"
        }
    }
    random_name = choice(list(random_recipes.keys()))
    recipe = random_recipes[random_name]
    photo = types.FSInputFile(recipe['image'])
    await callback.message.answer_photo(
        photo=photo,
        caption=recipe['caption']
    )
