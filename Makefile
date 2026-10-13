FORCE:



open_db: FORCE
	@ sudo -u postgres psql

create_db: FORCE
	sudo -u postgres psql -d postgres -c "CREATE DATABASE dhcp_store;"
	sudo -u postgres psql -d dhcp_store -c "CREATE SCHEMA IF NOT EXISTS dhcp_store; SET search_path TO dhcp_store, public;"

drop_db: FORCE
	sudo -u postgres psql -d postgres -c "DROP DATABASE IF EXISTS dhcp_store WITH (FORCE);"

create_tables: FORCE
	sudo -u postgres psql -d dhcp_store -f database/ddl/catalog.sql
	sudo -u postgres psql -d dhcp_store -f database/ddl/inventory.sql
	sudo -u postgres psql -d dhcp_store -f database/ddl/orders_and_configs.sql
	sudo -u postgres psql -d dhcp_store -f database/ddl/sales_and_requests.sql
	sudo -u postgres psql -d dhcp_store -f database/ddl/build_and_tests.sql

add_start_data: FORCE
	sudo -u postgres psql -d dhcp_store -f database/init/start_data.sql

generate_test_data: FORCE
	python3 scripts/fill_database_test_data.py
	sudo -u postgres psql -d dhcp_store -f database/init/generated_test_data.sql

pipeline: drop_db
	@ make create_db
	@ make create_tables
	@ make add_start_data

pipeline_test: pipeline
	@ make generate_test_data
	