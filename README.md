Запуск образа:

```
docker build -t test_serialization .
docker run -i -t test_serialization
```

Запуск программы внутри запущенного образа:

```
python3 test_serialization.py --file {filename} --test_type {datatype}
```

```{filename}``` - это путь к json-файлу (предлагается использовать "data/test.json"), но можно добавить и свои файлы.

```{datatype}``` - это расширение, которое хочется протестировать. Может принимать следующие значения: "native", "xml", "json", "avro", "yaml"

Программа возвращает количество байт, занимаемых переданной структурой в выбранном расширении.
