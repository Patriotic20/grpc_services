import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PermissionData(_message.Message):
    __slots__ = ("id", "name", "resource", "action", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    resource: str
    action: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., resource: _Optional[str] = ..., action: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RolePermissionData(_message.Message):
    __slots__ = ("role_id", "role_name", "permission_id", "permission_name", "assigned_at")
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_NAME_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_AT_FIELD_NUMBER: _ClassVar[int]
    role_id: int
    role_name: str
    permission_id: int
    permission_name: str
    assigned_at: _timestamp_pb2.Timestamp
    def __init__(self, role_id: _Optional[int] = ..., role_name: _Optional[str] = ..., permission_id: _Optional[int] = ..., permission_name: _Optional[str] = ..., assigned_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PermissionCreateRequest(_message.Message):
    __slots__ = ("name", "resource", "action", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    resource: str
    action: str
    description: str
    def __init__(self, name: _Optional[str] = ..., resource: _Optional[str] = ..., action: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class PermissionCreateResponse(_message.Message):
    __slots__ = ("success", "data", "message", "error_code")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    data: PermissionData
    message: str
    error_code: str
    def __init__(self, success: bool = ..., data: _Optional[_Union[PermissionData, _Mapping]] = ..., message: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...

class PermissionListRequest(_message.Message):
    __slots__ = ("page", "limit", "search", "resource", "action")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    page: int
    limit: int
    search: str
    resource: str
    action: str
    def __init__(self, page: _Optional[int] = ..., limit: _Optional[int] = ..., search: _Optional[str] = ..., resource: _Optional[str] = ..., action: _Optional[str] = ...) -> None: ...

class PermissionListResponse(_message.Message):
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
    data: _containers.RepeatedCompositeFieldContainer[PermissionData]
    message: str
    def __init__(self, success: bool = ..., total: _Optional[int] = ..., page: _Optional[int] = ..., limit: _Optional[int] = ..., data: _Optional[_Iterable[_Union[PermissionData, _Mapping]]] = ..., message: _Optional[str] = ...) -> None: ...

class PermissionDetailRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class PermissionDetailResponse(_message.Message):
    __slots__ = ("success", "data", "message", "error_code")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    data: PermissionData
    message: str
    error_code: str
    def __init__(self, success: bool = ..., data: _Optional[_Union[PermissionData, _Mapping]] = ..., message: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...

class PermissionUpdateRequest(_message.Message):
    __slots__ = ("id", "name", "resource", "action")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    resource: str
    action: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., resource: _Optional[str] = ..., action: _Optional[str] = ...) -> None: ...

class PermissionUpdateResponse(_message.Message):
    __slots__ = ("success", "data", "message", "error_code")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    data: PermissionData
    message: str
    error_code: str
    def __init__(self, success: bool = ..., data: _Optional[_Union[PermissionData, _Mapping]] = ..., message: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...

class PermissionDeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class PermissionDeleteResponse(_message.Message):
    __slots__ = ("success", "message", "error_code")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    error_code: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...

class AssignPermissionToRoleRequest(_message.Message):
    __slots__ = ("role_id", "permission_ids")
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_IDS_FIELD_NUMBER: _ClassVar[int]
    role_id: int
    permission_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, role_id: _Optional[int] = ..., permission_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class AssignPermissionToRoleResponse(_message.Message):
    __slots__ = ("success", "data", "message", "error_code")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    data: _containers.RepeatedCompositeFieldContainer[RolePermissionData]
    message: str
    error_code: str
    def __init__(self, success: bool = ..., data: _Optional[_Iterable[_Union[RolePermissionData, _Mapping]]] = ..., message: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...

class RevokePermissionFromRoleRequest(_message.Message):
    __slots__ = ("role_id", "permission_ids")
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_IDS_FIELD_NUMBER: _ClassVar[int]
    role_id: int
    permission_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, role_id: _Optional[int] = ..., permission_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class RevokePermissionFromRoleResponse(_message.Message):
    __slots__ = ("success", "message", "error_code")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    error_code: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...

class GetRolePermissionsRequest(_message.Message):
    __slots__ = ("role_id",)
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    role_id: int
    def __init__(self, role_id: _Optional[int] = ...) -> None: ...

class GetRolePermissionsResponse(_message.Message):
    __slots__ = ("success", "role_id", "role_name", "permissions", "message", "error_code")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    role_id: int
    role_name: str
    permissions: _containers.RepeatedCompositeFieldContainer[PermissionData]
    message: str
    error_code: str
    def __init__(self, success: bool = ..., role_id: _Optional[int] = ..., role_name: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[PermissionData, _Mapping]]] = ..., message: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...
