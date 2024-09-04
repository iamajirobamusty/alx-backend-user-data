#!/usr/bin/env python3
"""Basic Authentication
"""


from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """A class that implement the basic form of authentication
    """

    # base64
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """A function that encode the authorizaton
        header
        Return:
                None for now
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        value = authorization_header.split()
        return value[1]
