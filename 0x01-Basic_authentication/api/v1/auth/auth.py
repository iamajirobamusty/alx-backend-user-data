#!/usr/bin/env python3
""" A class that manages authentiction
"""


from flask import request


class Auth:
    """A class that manages authenticatoin

    Methods:
            def require_auth(self, path: str, excluded_paths: List([str]) -> bool:
            def authorization_header(self, request=None) -> sr:
            def current_user(self, request=None) -> str:
    """
    
    #Athentication required
    def require_auth(self, path: str, excluded_path: List[str]) -> bool:
        """A function that makes sure a user is required
        Returns:
                None, if auth is not required
        """
        return False


    def authorization_eheader(self, request=None) -> str:
        """Authorization header
        """
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """A function that returns the current user
        """
        return None
