from dataclasses import dataclass


@dataclass(frozen=True)
class Constants:
    APP_NAME: str = "Smart City Traffic Pattern Forecasting System"
    APP_ICON: str = "🚦"

