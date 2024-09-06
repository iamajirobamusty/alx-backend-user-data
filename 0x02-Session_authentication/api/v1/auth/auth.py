#!/usr/bin/env python3
""" A class that manages authentication
"""


from typing import List, TypeVar
import os
from flask import request


class Auth:
    """A class that manages authentication
    Methods:
            def require_auth(self, path: str,
                             excluded_paths: List[str]) -> bool:
            def authorization_header(self, request=None) -> str:
            def current_user(self, request=None) -> str:
    """

    # Authentication required
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """A function that makes sure a user is required
        Returns:
                True: if path is None
                True: if excluded_paths is None or empty
                False: if path is in excluded_paths
        """
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if path in excluded_paths:
            return False

        else:
            for i in excluded_paths:
                if i.startswith(path):
                    return False
                elif path.startswith(i):
                    return False
                elif i[-1] == "*":
                    if path.startswith(i[:1]):
                        return False

        return True

    def authorization_header(self, request=None) -> str:
        """Authorization header
            Returns:
                    The value of the authorization header
        """
        if request is None:
            return None
        result = request.headers.get('Authorization')

        if result is None:
            return None

        return result

    def current_user(self, request=None) -> TypeVar('User'):
        """A function that returns the current user
        """
        return None

    def session_cookie(self, request=None):
        """A function that returns a cookie from a request"""
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)
