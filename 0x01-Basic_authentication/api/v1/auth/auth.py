#!/usr/bin/env python3
""" A class that manages authentiction
"""


from typing import List, TypeVar
from flask import request


class Auth:
    """A class that manages authenticatoin

    Methods:
            def require_auth(self, path: str, excluded_paths: List([str]) -> bool:
            def authorization_header(self, request=None) -> sr:
            def current_user(self, request=None) -> str:
    """
    
    #Athentication required
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

    def authorization_header(self, request=None) -> str:
        """Authorization header
        """
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """A function that returns the current user
        """
        return None
