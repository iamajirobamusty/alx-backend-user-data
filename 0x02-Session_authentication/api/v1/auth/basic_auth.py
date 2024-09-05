#!/usr/bin/env python3
"""Basic Authentication
"""


from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


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

    # base64.decode
    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """A function that returns the deocded value of base64 
            Returns:
                    base64.decode()
            Usage:
                a = BasicAuth()

                print(a.decode_base64_authorization_header(None))
                print(a.decode_base64_authorization_header(89))
                print(a.decode_base64_authorization_header("Holberton School"))
                print(a.decode_base64_authorization_header("SG9sYmVydG9u"))
                print(a.decode_base64_authorization_header("SG9sYmVydG9uIFNjaG9vbA=="))
                print(a.decode_base64_authorization_header(a.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA==")))
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            utfdecode = base64_authorization_header.encode('utf-8')
            b64 = base64.b64decode(utfdecode)
            return b64.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
            decode_base64_authorization_header: str) -> (str, str):
        """Extract User Credential from Authorization header
        Return:
                None if not present
                None if not string
                None if not properly formatted
                user credentials
        Usage:
                from api.v1.auth.basic_auth import BasicAuth

                a = BasicAuth()

                print(a.extract_user_credentials(None))
                print(a.extract_user_credentials(89))
                print(a.extract_user_credentials("Holberton School"))
                print(a.extract_user_credentials("Holberton:School"))
                print(a.extract_user_credentials("bob@gmail.com:toto1234"))
        """
        if decode_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decode_base64_authorization_header,
                str):
            return (None, None)
        if ":" not in decode_base64_authorization_header:
            return (None, None)

        value = decode_base64_authorization_header.split(':')
        return (value[0], value[1])
    
    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """A function that returns the user instance based on the email and password
            Return:
                    None if user_email is None
                    None if user_pwd is None
                    None if no user in the DB or user not in the DB
                    None if user_pwd is not the password of the user foud
                    User instance
        """
        if not isinstance(user_email, str):
            return None
        if not isinstance(user_pwd, str):
            return None

        try:
            user = User.search({"email": user_email})
            if not user or user == []:
                return None
            for user in user:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """A function that overloads the authroization and retrieve hte user instance
        """
        header = self.authorization_header(request)
        if header is not None:
            extract = self.extract_base64_authorization_header(header)
            if extract is not None:
                decode = self.decode_base64_authorization_header(extract)
                if decode is not None:
                    email, password = self.extract_user_credentials(decode)
                    if email is not None:
                            return self.user_object_from_credentials(email, password)
