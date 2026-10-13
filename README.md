



## Как работать с базой данных

- Запустить сборку базы данных магазина DHCP

```Shell
make pipeline
```

- Запустить сборку базы данных с тестовыми данными

```Shell
make pipeline_test
```

- Добавить тестовые данные

```Shell
make generate_test_data
```

- Открыть консоль PostgreSQL

```Shell
make open_bd
```

- Создать базу данных dhcp_store

```Shell
make create_db
```

- Удалить базу данных dhcp_store

```Shell
make drop_db
```

- Создать сущности

```Shell
make create_tables
```

- Добавить начальные данные

```Shell
make add_start_data
```
