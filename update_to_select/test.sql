update sandbox.marts_generic_dimensions 
set 
sales_opportunity_owner_name = sfc.sales_agent_name 
, sales_opportunity_owner_team = sfc.sales_agent_role 
, sales_opportunity_owner_role = sfc.user_role 
, sales_opportunity_owner_country = sfc.sales_agent_country 
from 
mart.sales_agent_product_acquiring sfc
where 
sandbox.marts_generic_dimensions.merchant_id = sfc.outlet_mid
