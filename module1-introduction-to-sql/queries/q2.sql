SELECT
	sub1.cleric_count,
	sub2.fighter_count,
	sub3.mage_count,
	sub4.necromancer_count,
	sub5.thief_count
FROM
	(
		SELECT
			count(*) AS cleric_count
		FROM
			charactercreator_cleric
	) AS sub1,
	(
		SELECT
			count(*) AS fighter_count
		FROM
			charactercreator_fighter
	) AS sub2,
	(
		SELECT
			count(*) AS mage_count
		FROM
			charactercreator_mage
	) AS sub3,
	(
		SELECT
			count(*) AS necromancer_count
		FROM
			charactercreator_necromancer
	) AS sub4,
	(
		SELECT
			count(*) AS thief_count
		FROM
			charactercreator_thief
	) AS sub5