SELECT
    count_all_not_weapons,
    count_all_is_weapons
FROM
    (
        SELECT
            count(*) AS count_all_not_weapons
        FROM
            charactercreator_character_inventory AS cci
        WHERE
            cci.item_id NOT IN (
                SELECT
                    aw.item_ptr_id
                FROM
                    armory_weapon AS aw
            )
    ),
    (
        SELECT
            count(*) AS count_all_is_weapons
        FROM
            charactercreator_character_inventory AS cci
        WHERE
            cci.item_id IN (
                SELECT
                    aw.item_ptr_id
                FROM
                    armory_weapon AS aw
            )
    )