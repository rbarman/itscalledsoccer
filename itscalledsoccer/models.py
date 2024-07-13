from pydantic import BaseModel, RootModel
from typing import Optional, List, Union, Dict


class Manager(BaseModel):
    manager_id: str
    manager_name: Optional[str] = None
    nationality: Optional[str] = None


class Managers(RootModel):
    root: List[Manager]


class Referee(BaseModel):
    referee_id: str
    referee_name: Optional[str] = None
    nationality: Optional[str] = None


class Referees(RootModel):
    root: List[Referee]


class Stadium(BaseModel):
    stadium_id: str
    stadium_name: Optional[str] = None
    capacity: Optional[int] = None
    year_built: Optional[int] = None
    roof: Optional[bool] = None
    turf: Optional[bool] = None
    street: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    field_x: Optional[int] = None
    field_y: Optional[int] = None


class Stadia(RootModel):
    root: List[Stadium]


class Team(BaseModel):
    team_id: str
    team_name: Optional[str] = None
    team_short_name: Optional[str] = None
    team_abbreviation: Optional[str] = None


class Teams(RootModel):
    root: List[Team]


class Player(BaseModel):
    player_id: str
    player_name: Optional[str] = None
    birth_date: Optional[str] = None
    height_ft: Optional[int] = None
    height_in: Optional[int] = None
    weight_lb: Optional[int] = None
    nationality: Optional[str] = None
    primary_broad_position: Optional[str] = None
    primary_general_position: Optional[str] = None
    secondary_broad_position: Optional[str] = None
    secondary_general_position: Optional[str] = None
    season_name: Optional[Union[List[str], Dict, str]] = None


class Players(RootModel):
    root: List[Player]


class Game(BaseModel):
    game_id: str
    date_time_utc: Optional[str] = None
    home_score: Optional[int] = None
    away_score: Optional[int] = None
    home_team_id: Optional[str] = None
    away_team_id: Optional[str] = None
    referee_id: Optional[str] = None
    stadium_id: Optional[str] = None
    home_manager_id: Optional[str] = None
    away_manager_id: Optional[str] = None
    expanded_minutes: Optional[int] = None
    season_name: Optional[str] = None
    matchday: Optional[int] = None
    attendance: Optional[int] = None
    knockout_game: Optional[bool] = None
    last_updated_utc: Optional[str] = None


class Games(RootModel):
    root: List[Game]
