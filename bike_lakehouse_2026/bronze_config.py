# bronze_config.py

## 1. Define the Root Path (Where your files ACTUALLY are)
# Make sure this matches your Volume path exactly!
BASE_PATH = "/Volumes/workspace/bronze/source_systems"

# 2. The Configuration List
INGESTION_CONFIG = [
    # --- CRM DATA ---
    {
        "source": "crm",
        "path": f"{BASE_PATH}/cust_info.csv",  
        "table": "bronze.crm_cust_info"
    },
    {
        "source": "crm",
        "path": f"{BASE_PATH}/prd_info.csv",
        "table": "bronze.crm_prd_info"
    },
    {
        "source": "crm",
        "path": f"{BASE_PATH}/sales_details.csv",
        "table": "bronze.crm_sales_details"
    },
    
    # --- ERP DATA ---
    {
        "source": "erp",
        "path": f"{BASE_PATH}/CUST_AZ12.csv", 
        "table": "bronze.erp_cust_az12"
    },
    {
        "source": "erp",
        "path": f"{BASE_PATH}/LOC_A101.csv",
        "table": "bronze.erp_loc_a101"
    },
    {
        "source": "erp",
        "path": f"{BASE_PATH}/PX_CAT_G1V2.csv",
        "table": "bronze.erp_px_cat_g1v2"
    }
]