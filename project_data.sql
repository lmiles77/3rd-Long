CREATE TABLE "Game3" (
    "GameId" int   NOT NULL,
    "GameDate" date   NOT NULL,
    CONSTRAINT "pk_Game3" PRIMARY KEY (
        "GameId"
     )
);

create TABLE "Play3" (
    "PlayId" serial   NOT NULL,
    "GameId" int   NOT NULL,
    "Quarter" int   NOT NULL,
    "Minute" int   NOT NULL,
    "Second" int   NOT NULL,
    "OffenseTeam" varchar(50),
    "DefenseTeam" varchar(50),
    "Down" int   NOT NULL,
    "ToGo" int   NOT NULL,
    "Yards" int   NOT NULL,
    "YardsPlusMinus" int   NOT NULL,
    "Successful3rdDown" varchar(50)   NOT NULL,
    "YardLine" int   NOT NULL,
    "SeriesFirstDown" bit   NOT NULL,
    "NextScore" int   NOT NULL,
    "Description" varchar(1000)   NOT NULL,
    "TeamWin" bit   NOT NULL,
    "SeasonYear" int   NOT NULL,
    "Formation" varchar(50),
    "PlayType" varchar(50),
    "IsRush" bit   NOT NULL,
    "IsPass" bit   NOT NULL,
    "IsIncomplete" bit   NOT NULL,
    "IsTouchdown" bit   NOT NULL,
    "PassType" varchar(50),
    "IsSack" bit   NOT NULL,
    "IsChallenge" bit   NOT NULL,
    "IsChallengeReversed" bit   NOT NULL,
    "IsMeasurement" bit   NOT NULL,
    "IsInterception" bit   NOT NULL,
    "IsFumble" bit   NOT NULL,
    "IsPenalty" bit   NOT NULL,
    "IsTwoPointConversion" bit   NOT NULL,
    "IsTwoPointConversionSuccessful" bit   NOT NULL,
    "RushDirection" varchar(50),
    "YardLineFixed" int   NOT NULL,
    "YardLineDirection" varchar(50)   NOT NULL,
    "IsPenaltyAccepted" bit   NOT NULL,
    "PenaltyTeam" varchar(50),
    "IsNoPlay" bit   NOT NULL,
    "PenaltyType" varchar(100),
    "PenaltyYards" int   NOT NULL,
    CONSTRAINT "pk_Play3" PRIMARY KEY (
        "PlayId"
     )
);

CREATE TABLE "Temp3" (
    "GameId" int  ,
	"GameDate" date,
    "Quarter" int  ,
    "Minute" int  ,
    "Second" int  ,
	"OffenseTeam" varchar(50),
	"DefenseTeam" varchar(50),
    "Down" int  ,
    "ToGo" int  ,
    "Yards" int  ,
    "YardsPlusMinus" int  ,
    "Successful3rdDown" varchar(50)  ,
    "YardLine" int  ,
    "SeriesFirstDown" bit  ,
    "NextScore" int  ,
    "Description" varchar(1000)  ,
    "TeamWin" bit  ,
    "SeasonYear" int  ,
    "Formation" varchar(50)  ,
    "PlayType" varchar(50)  ,
    "IsRush" bit  ,
    "IsPass" bit  ,
    "IsIncomplete" bit  ,
    "IsTouchdown" bit  ,
    "PassType" varchar(50)  ,
    "IsSack" bit  ,
    "IsChallenge" bit  ,
    "IsChallengeReversed" bit  ,
    "IsMeasurement" bit  ,
    "IsInterception" bit  ,
    "IsFumble" bit  ,
    "IsPenalty" bit  ,
    "IsTwoPointConversion" bit  ,
    "IsTwoPointConversionSuccessful" bit  ,
    "RushDirection" varchar(50)  ,
    "YardLineFixed" int  ,
    "YardLineDirection" varchar(50)  ,
    "IsPenaltyAccepted" bit  ,
    "PenaltyTeam" varchar(50)  ,
    "IsNoPlay" bit  ,
    "PenaltyType" varchar(100)  ,
    "PenaltyYards" int
);


-- load Game table
insert into public."Game3" ("GameId", "GameDate")
select DISTINCT "GameId", "GameDate" from public."Temp3";


-- load Play table
insert into public."Play3" ("GameId", "Quarter", "Minute", "Second", "OffenseTeam", "DefenseTeam", "Down", "ToGo", "Yards", "YardsPlusMinus", "Successful3rdDown", "YardLine", "SeriesFirstDown", "NextScore", "Description", "TeamWin", "SeasonYear", "Formation", "PlayType", "IsRush", "IsPass", "IsIncomplete", "IsTouchdown", "PassType", "IsSack", "IsChallenge", "IsChallengeReversed", "IsMeasurement", "IsInterception", "IsFumble", "IsPenalty", "IsTwoPointConversion", "IsTwoPointConversionSuccessful", "RushDirection", "YardLineFixed", "YardLineDirection", "IsPenaltyAccepted", "PenaltyTeam", "IsNoPlay", "PenaltyType", "PenaltyYards")
SELECT                       "GameId", "Quarter", "Minute", "Second", "OffenseTeam", "DefenseTeam", "Down", "ToGo", "Yards", "YardsPlusMinus", "Successful3rdDown", "YardLine", "SeriesFirstDown", "NextScore", "Description", "TeamWin", "SeasonYear", "Formation", "PlayType", "IsRush", "IsPass", "IsIncomplete", "IsTouchdown", "PassType", "IsSack", "IsChallenge", "IsChallengeReversed", "IsMeasurement", "IsInterception", "IsFumble", "IsPenalty", "IsTwoPointConversion", "IsTwoPointConversionSuccessful", "RushDirection", "YardLineFixed", "YardLineDirection", "IsPenaltyAccepted", "PenaltyTeam", "IsNoPlay", "PenaltyType", "PenaltyYards"
	FROM public."Temp3";
	
	
	
	
	
	
-- Check table counts
select 'temp3', count(*) as Total from public."Temp99"
union all
select 'play3', count(*) as Total from public."Play99"
union all
select 'game3', count(*) as Total from public."Game99";


