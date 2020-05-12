SELECT
    AVG(count_each_character_items) as "average_character_item"
FROM
    (
        SELECT
            character_id,
            count(item_id) AS "count_each_character_items"
        FROM
            charactercreator_character_inventory cci
        GROUP BY
            character_id
    )