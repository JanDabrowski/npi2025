#NOWATORSKI PROJEKT JEDNOSOBOWY - Jan Dąbrowski 49452

#Uruchamienie środowiska lokalnego

```
docker compose up --watch --no-attach npi_pgadmin --build
```

Uruchomione zostanie lokalne środowisko składające się z:

- `app_backend` - serwisu backendowego (port 80)
- `app_frontend` - serwisu frontendowego (port 3000)
- `app_database` - bazy danych
- `app_pgadmin` - managera bazy danych (port 8080)
