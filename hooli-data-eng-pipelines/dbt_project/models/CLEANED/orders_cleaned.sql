select
        user_id,
        quantity,
        purchase_price,
        sku,
        dt,
        cast(dt as datetime) as order_date,
        quantity * purchase_price as order_total
from {{ source("RAW_DATA", "orders") }}
{% if is_incremental() %}
WHERE dt = '{{ var('datetime_to_process') }}'
{% endif %}