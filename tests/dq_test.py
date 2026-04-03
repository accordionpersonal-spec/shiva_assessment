assert spark.table("1_dev.bronze.sales").count() > 0
assert spark.table("1_dev.silver.sales_cleaned").count() > 0
assert spark.table("1_dev.gold.total_sales_product").count() > 0


expected_cols = ["product_id", "total_sales"]
assert all(col in df.columns for col in expected_cols)