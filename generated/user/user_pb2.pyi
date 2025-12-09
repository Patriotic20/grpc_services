import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserData(_message.Message):
    __slots__ = ("id", "username", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    username: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., username: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UserWithRoles(_message.Message):
    __slots__ = ("id", "username", "roles", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    username: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., username: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UserListRequest(_message.Message):
    __slots__ = ("page", "limit", "search", "role_ids", "sort_by", "sort_order")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    page: int
    limit: int
    search: str
    role_ids: _containers.RepeatedScalarFieldContainer[int]
    sort_by: str
    sort_order: str
    def __init__(self, page: _Optional[int] = ..., limit: _Optional[int] = ..., search: _Optional[str] = ..., role_ids: _Optional[_Iterable[int]] = ..., sort_by: _Optional[str] = ..., sort_order: _Optional[str] = ...) -> None: ...

class UserListResponse(_message.Message):
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
    data: _containers.RepeatedCompositeFieldContainer[UserWithRoles]
    message: str
    def __init__(self, success: bool = ..., total: _Optional[int] = ..., page: _Optional[int] = ..., limit: _Optional[int] = ..., data: _Optional[_Iterable[_Union[UserWithRoles, _Mapping]]] = ..., message: _Optional[str] = ...) -> None: ...

class UserDetailRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class UserDetailResponse(_message.Message):
    __slots__ = ("success", "data", "message", "error_code")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    data: UserWithRoles
    message: str
    error_code: str
    def __init__(self, success: bool = ..., data: _Optional[_Union[UserWithRoles, _Mapping]] = ..., message: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...

class UserUpdateRequest(_message.Message):
    __slots__ = ("id", "username")
    ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    username: str
    def __init__(self, id: _Optional[int] = ..., username: _Optional[str] = ...) -> None: ...

class UserUpdateResponse(_message.Message):
    __slots__ = ("success", "data", "message", "error_code")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    data: UserData
    message: str
    error_code: str
    def __init__(self, success: bool = ..., data: _Optional[_Union[UserData, _Mapping]] = ..., message: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...

class UserDeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class UserDeleteResponse(_message.Message):
    __slots__ = ("success", "message", "error_code")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    error_code: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...
