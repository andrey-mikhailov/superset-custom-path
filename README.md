It is a common requirement to have superset running under a base url, (https://mydomain.at/analytics/ instead of https://mydomain.at/). I created the script to add "/analytics" prefix to all python and js codes. The script is tested with Superset 1.3.2

## Resources
  * https://github.com/apache/incubator-superset/pull/1866#issuecomment-347310860
  * https://github.com/amancevice/docker-superset/blob/master/examples/postgres/docker-compose.yml
  * https://github.com/komoot/superset-reverse-nginx-example
  * https://docs.altinity.com/integrations/clickhouse-and-superset/connect-clickhouse-to-superset/
  
## How to run

Build and run docker containers
```
docker-compose up --build --force-recreate
```

Exec to to the running superset container
```
docker exec -it superset-custom-path_superset_1 bash
```

```
# Initialize the database
superset db upgrade

# Create an admin user (you will be prompted to set a username, first and last name before setting a password)
superset fab create-admin

# Optional step. Load some data to play with (it requires few minutes and ~80 mbytes of disk space)
superset load_examples

# Create default roles and permissions
superset init
```

Open http://localhost:8080 in your browser

Optional step. Connect to the demo ClickHouse dataset
Data -> Databases -> +Database

Find ClickHouse database in the select box, paste SQL Alchemy URI:
```
clickhouse+native://demo:demo@github.demo.trial.altinity.cloud/default?secure=true
```
Read more here 
https://docs.altinity.com/integrations/clickhouse-and-superset/connect-clickhouse-to-superset/
