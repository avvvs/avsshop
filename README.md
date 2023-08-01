# avsshop

Интернет-магазин на django с системой "Умный консультант", работающей на основе ChatGPT.

Постановка задачи: ПО должно содержать в себе следующие функции:

Клиентская часть:
-  каталог товаров, в том числе возможность выбора категории необходимой продукции в навигационном меню;
-  формы для авторизации и регистрации пользователей, в том числе и для восстановления пароля по электронной почте, указанной при регистрации;
-  пользовательская корзина покупок;
-  информационная страница о магазине;
-  поиск товаров по ключевым словам;
-  функция голосового поиска;
-  чат-бот на основе искусственного интеллекта, который должен в любое время консультировать пользователей и на основе запроса и передающегося списка товаров в магазине рекомендовать подходящий для них товар.
  
Административная часть:
-  возможность создавать, редактировать и удалять товар в интернет-магазине;
-  просмотр списка заказов, в том числе историю списка товаров, которые пользователи добавляют в корзину.
# ДЛЯ ПОДКЛЮЧЕНИЯ "УМНОГО КОСНУЛЬТАНТА"

Необходимо зарегестрироваться на OpenAi platform и получить уникальный API ключ, который необхоимо вставить в файл chat.html на 101 строке вместо "YOUR API KEY".
