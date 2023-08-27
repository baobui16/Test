import sys
sys.path.append('.\\assets')
sys.path.append('D:\FDE 2\etl_pipeline')

from dagster import Definitions
from bronze import bronze_olist_order_items_dataset,bronze_olist_order_payments_dataset,bronze_olist_orders_dataset,bronze_olist_products_dataset,bronze_product_category_name_translation
from silver import dim_products, fact_sales
from gold import sales_values_by_category

from resources.minio_io_manager import MinIOIOManager
from resources.mysql_io_manager import MySQLIOManager
from resources.psql_io_manager import PostgreSQLIOManager


MYSQL_CONFIG = {
    "host": "localhost",
    "port": 3307,
    "database": "brazillian_ecommerce",
    "user": "admin",
    "password": "admin123",
}
MINIO_CONFIG = {
    "endpoint_url": "localhost:9000",
    "bucket": "warehouse",
    "aws_access_key_id": "minio",
    "aws_secret_access_key": "minio123",
}
PSQL_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "demo_pg",
    "user": "admin",
    "password": "admin123",
}

defs = Definitions(
    assets=[fact_sales, dim_products, sales_values_by_category, bronze_olist_products_dataset, bronze_product_category_name_translation, bronze_olist_order_payments_dataset, bronze_olist_order_items_dataset, bronze_olist_orders_dataset],
    resources={
        "mysql_io_manager": MySQLIOManager(MYSQL_CONFIG),
        "minio_io_manager": MinIOIOManager(MINIO_CONFIG),
        "psql_io_manager": PostgreSQLIOManager(PSQL_CONFIG),
    },
)