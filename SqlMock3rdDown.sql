create table "Player_Stats"(
"game_id" int pk NOTNULL,
"Offense" int  NOTNULL,
"rush_yards" int NOTNULL, 
"rec_air_yards" int NOTNULL,
"combo_pass_rush" int NOTNULL,
"player_id" int Notnull
);

CREATE TABLE "Team" (
    "Home_team" varchar    NOTNULL,
    "opponent" varchar   NOTNULL,
    "team_id" varchar   NOTNULL,
    CONSTRAINT "pk_Team" PRIMARY KEY (
        "index"
     )
);

CREATE TABLE "Weather" (
    "surface" int   NOT NULL,
    "Temperature" varchar   NOT NULL,
    "Humidity" varchar   NOT NULL,
    "Wind_speed" varchar   NOT NULL,
    CONSTRAINT "pk_Weather" PRIMARY KEY (
        "index"
     )
);



