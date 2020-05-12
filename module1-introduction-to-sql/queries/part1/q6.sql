SELECT
    character_id,
    count(aw.item_ptr_id) as "character_weapon_count"
FROM
    charactercreator_character_inventory AS cci
    LEFT JOIN armory_weapon AS aw ON cci.item_id = aw.item_ptr_id
GROUP BY
    character_id
LIMIT
    20