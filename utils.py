# utils.py

import logging
import os
import re
from typing import List, Tuple, Optional

from user_dashboard.config import Config
from user_dashboard.database import Database

class Utils:
    @staticmethod
    def get_database_connection() -> Database:
        return Database(Config.DATABASE_URL)

    @staticmethod
    def validate_email(email: str) -> bool:
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_password(password: str) -> bool:
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
        return bool(re.match(pattern, password))

    @staticmethod
    def get_user_data_from_token(token: str) -> Optional[dict]:
        try:
            user_id = token.split('.')[1]
            return {
                'user_id': int(user_id),
                'username': 'username_placeholder',
                'email': 'email_placeholder'
            }
        except (IndexError, ValueError):
            return None

    @staticmethod
    def get_current_directory() -> str:
        return os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def get_project_root() -> str:
        return os.path.dirname(Utils.get_current_directory())

    @staticmethod
    def get_assets_path() -> str:
        return os.path.join(Utils.get_project_root(), 'assets')

    @staticmethod
    def get_static_path() -> str:
        return os.path.join(Utils.get_project_root(), 'static')