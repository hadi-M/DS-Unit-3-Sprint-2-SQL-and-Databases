
CREATE TABLE IF NOT EXISTS titanic (
    id SERIAL PRIMARY KEY,
    Survived boolean,
    Pclass int4,
    "Name" VARCHAR(255),
    Sex VARCHAR(6),
    "Siblings/Spouses Aboard" int4,
    "Parents/Children Aboard" int4,
    Fare float8
)