#!/usr/bin/env python3
"""Session Authentication"""


from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """A class that implements session based authentication
    """
    user_id_by_session_id = {}

    def create_session(
            self,
            user_id: str = None) -> str:
        """A function that creates a session ID for a user id"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None

        session_id = uuid.uuid4()
        self.user_id_by_session_id[str(session_id)] = user_id
        return str(session_id)

    def user_id_for_session_id(
            self,
            session_id: str = None) -> str:
        """A function that returns a session ID"""
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
