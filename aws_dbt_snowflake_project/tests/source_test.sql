{{ config
    (
        severity='warn'
    )
}}

select
    *
from {{ source('staging', 'bookings') }}
where booking_amount < 200