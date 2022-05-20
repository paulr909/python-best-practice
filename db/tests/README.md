# Pytest and Coverage

To run unit tests, the test database needs to be created and seeded. Use seed directory files before beginning tests. For details seed/README.md

## Disable Deprecation Warning while running pytest on database

[https://docs.pytest.org/en/stable/warnings.html](https://docs.pytest.org/en/stable/warnings.html)

```shell
pytest test_db.py --disable-warnings
```

With the pytest.ini file warnings can also be disabled, switch on and off to check you are only disabling Deprecation Warnings.

```shell
pytest db/tests/test_db.py
```

Run with coverage from root directory.
```shell
coverage report -m
```

### As the seed db tests can run with GitHub Actions we use "root" for username and password as they are generic