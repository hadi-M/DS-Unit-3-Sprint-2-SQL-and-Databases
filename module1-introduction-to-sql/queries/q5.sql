SELECT
    character_id,
    count(item_id) as "count_each_character_items"
FROM
    charactercreator_character_inventory cci
GROUP BY
    character_id
LIMIT
    20