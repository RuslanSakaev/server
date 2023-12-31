# Компьютерные сети (семинары)
## Урок 6. Основы компьютерных сетей. Транспортный уровень. UDP и TCP.
1. Напишите свою программу сервер и запустите её. 
   ```
   https://github.com/RuslanSakaev/Weblayout.git
   ```
   - (если опыта в python нет, запустите готовый код и разберитесь, как он работает:
   - файл с кодом готового клиента: https://disk.yandex.ru/d/cAfsjjG_mLqF3A 
   - файл с кодом готового сервера: https://disk.yandex.ru/d/qrj4qpiXhXVwgw ) 
   - '** попробуйте улучшить код, опишите что сделали, какие фичи добавили.
2. Запустите несколько клиентов. Симитируйте чат.
   ![чат](./img/1.bmp)
    ![чат](./img/2.bmp)
     ![чат](./img/3.bmp)
      ![чат](./img/4.bmp)
       ![чат](./img/5.bmp)
3. Отправьте мне код написанного сервера __(можете через github, если удобно или прямо здесь в txt формате)__ и скриншоты работающего чата.
    ![чат](./img/6.bmp)
    ```
     https://github.com/RuslanSakaev/Weblayout.git
    ```
4. Отследите сокеты с помощью команды netstat. __(тоже пришлите скриншот именно сокетов вашего чата)__
   ![чат](./img/4.bmp)
5. Перехватите трафик своего чата в Wireshark и cшейте сессию. Пришлите скриншот сшитой сессии с диалогом.
   ![чат](./img/7.bmp)
   ![чат](./img/8.bmp)
6. Посмотрите скринкаст с практикой перед следующим семинаром.
   - Практика NAT. https://disk.yandex.ru/i/xD314SQzMEF2mA
   - Практика GRE. https://disk.yandex.ru/i/rhl3uDdyZ1VdjA
   - Установка OpenVPN. https://disk.yandex.ru/i/fzwkRatuYrsrew
7. ** Заведите себе машину в облаке, будем разбирать как работает VPN. Можно yandex cloud (2 мес бесплатно). Можно timeweb.cloud (188 р/мес). Или любую другую на ваш выбор.

Улучшения, которые можно внести:

- __Использование потоков для клиентов__: 
    
    В моём коде каждый клиент обрабатывается в отдельном потоке. Это улучшает параллелизм и позволяет обслуживать несколько клиентов одновременно.

- __Обработка отключения клиента__: 
  
    В моей реализации клиент будет ожидать ввода сообщения бесконечно. Добавлена проверка на отключение клиента и соответствующее завершение работы.

- __Обработка исключений__: 
    
    Необходимо добавить обработку исключений для сетевых операций, чтобы программа не завершалась при возникновении ошибок. В коде клиента добавлена проверка на ввод "exit" для выхода из цикла ввода сообщений. Также, в случае исключения (например, KeyboardInterrupt), клиент всегда закроет сокет перед завершением. В коде сервера также добавлена обработка исключения ConnectionResetError, которое может возникнуть, когда клиент внезапно отключается. При возникновении этой ошибки, сервер прекращает обработку данного клиента.


- __Добавление идентификаторов клиентов__:
    
    Для симуляции чата можно добавить идентификаторы (имена) для каждого клиента и включать их в сообщения, чтобы было понятно, кто отправил какое сообщение.

- __Защита от инъекций и буферных переполнений__: 
    
    Реальный чат-протокол должен учитывать защиту от инъекций и буферных переполнений. 

    __Защита от инъекций__: 
    - Добавлено замещение символов < и > в сообщениях, чтобы предотвратить возможные инъекции HTML или другие виды атак.

    __Пропуск пустых сообщений__: 
    - Клиент теперь пропускает отправку пустых сообщений, чтобы избежать лишних операций и сообщений.

- Сервер использует блокировку ___message_lock___ для добавления сообщений в очередь и обеспечивает безопасное обновление данных. Каждый новый клиент теперь видит последние 10 сообщений, хранящихся в очереди.  Клиентское приложение использует отдельный поток ___message_receiver___ для непрерывного приема сообщений от сервера и вывода их на экран.
- Сервер сохраняет все сообщения в файл "chat_history.txt", а клиенты периодически читают этот файл и выводят последние сообщения на экран.
Сервер сохраняет все сообщения в файл "chat_history.txt", а клиенты периодически читают этот файл и выводят последние сообщения на экран.
****
Создаём фаил __server.py__ и клиентский код __client.py__. Запускаем серверный файл в одной командной строке и несколько клиентских файлов в разных командных строках для симуляции чата.
```
py server.py
py client.py
```