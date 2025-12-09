import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RoleData(_message.Message):
    __slots__ = ("id", "name", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UserRoleData(_message.Message):
    __slots__ = ("user_id", "username", "role_id", "role_name", "assigned_at")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_AT_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    username: str
    role_id: int
    role_name: str
    assigned_at: _timestamp_pb2.Timestamp
    def __init__(self, user_id: _Optional[int] = ..., username: _Optional[str] = ..., role_id: _Optional[int] = ..., role_name: _Optional[str] = ..., assigned_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RoleCreateRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class RoleCreateResponse(_message.Message):
    __slots__ = ("success", "data", "message", "error_code")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    data: RoleData
    message: str
    error_code: str
    def __init__(self, success: bool = ..., data: _Optional[_Union[RoleData, _Mapping]] = ..., message: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...

class RoleListRequest(_message.Message):
    __slots__ = ("page", "limit", "search")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    page: int
    limit: int
    search: str
    def __init__(self, page: _Optional[int] = ..., limit: _Optional[int] = ..., search: _Optional[str] = ...) -> None: ...

class RoleListResponse(_message.Message):
    __slots__ = ("success", "total", "page", "limit", "data", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    total: int
    page: int
    limit: int
    data: _containers.RepeatedCompositeFieldContainer[RoleData]
    message: str
    def __init__(self, success: bool = ..., total: _Optional[int] = ..., page: _Optional[int] = ..., limit: _Optional[int] = ..., data: _Optional[_Iterable[_Union[RoleData, _Mapping]]] = ..., message: _Optional[str] = ...) -> None: ...

class RoleDetailRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class RoleDetailResponse(_message.Message):
    __slots__ = ("success", "data", "message", "error_code")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    data: RoleData
    message: str
    error_code: str
    def __init__(self, success: bool = ..., data: _Optional[_Union[RoleData, _Mapping]] = ..., message: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...

class RoleUpdateRequest(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class RoleUpdateResponse(_message.Message):
    __slots__ = ("success", "data", "message", "error_code")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    data: RoleData
    message: str
    error_code: str
    def __init__(self, success: bool = ..., data: _Optional[_Union[RoleData, _Mapping]] = ..., message: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...

class RoleDeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class RoleDeleteResponse(_message.Message):
    __slots__ = ("success", "message", "error_code")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    error_code: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...

class AssignRolesToUserRequest(_message.Message):
    __slots__ = ("user_id", "role_ids")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    role_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, user_id: _Optional[int] = ..., role_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class AssignRolesToUserResponse(_message.Message):
    __slots__ = ("success", "data", "message", "error_code")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    data: _containers.RepeatedCompositeFieldContainer[UserRoleData]
    message: str
    error_code: str
    def __init__(self, success: bool = ..., data: _Optional[_Iterable[_Union[UserRoleData, _Mapping]]] = ..., message: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...

class RevokeRolesFromUserRequest(_message.Message):
    __slots__ = ("user_id", "role_ids")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    role_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, user_id: _Optional[int] = ..., role_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class RevokeRolesFromUserResponse(_message.Message):
    __slots__ = ("success", "message", "error_code")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    error_code: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...

class GetUserRolesRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class GetUserRolesResponse(_message.Message):
    __slots__ = ("success", "user_id", "username", "roles", "message", "error_code")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    user_id: int
    username: str
    roles: _containers.RepeatedCompositeFieldContainer[RoleData]
    message: str
    error_code: str
    def __init__(self, success: bool = ..., user_id: _Optional[int] = ..., username: _Optional[str] = ..., roles: _Optional[_Iterable[_Union[RoleData, _Mapping]]] = ..., message: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...

class GetRoleUsersRequest(_message.Message):
    __slots__ = ("role_id", "page", "limit")
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    role_id: int
    page: int
    limit: int
    def __init__(self, role_id: _Optional[int] = ..., page: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class GetRoleUsersResponse(_message.Message):
    __slots__ = ("success", "role_id", "role_name", "total", "page", "limit", "users", "message", "error_code")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_NAME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    role_id: int
    role_name: str
    total: int
    page: int
    limit: int
    users: _containers.RepeatedCompositeFieldContainer[UserRoleData]
    message: str
    error_code: str
    def __init__(self, success: bool = ..., role_id: _Optional[int] = ..., role_name: _Optional[str] = ..., total: _Optional[int] = ..., page: _Optional[int] = ..., limit: _Optional[int] = ..., users: _Optional[_Iterable[_Union[UserRoleData, _Mapping]]] = ..., message: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...
