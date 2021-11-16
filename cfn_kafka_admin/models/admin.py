# generated by datamodel-codegen:
#   filename:  aws-cfn-kafka-admin-provider-schema.json
#   timestamp: 2021-11-16T22:30:02+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Extra, Field, constr


class DeletionPolicy(Enum):
    Retain = "Retain"
    Delete = "Delete"


class CompatibilityMode(Enum):
    BACKWARD = "BACKWARD"
    BACKWARD_TRANSITIVE = "BACKWARD_TRANSITIVE"
    FORWARD = "FORWARD"
    FORWARD_TRANSITIVE = "FORWARD_TRANSITIVE"
    FULL = "FULL"
    FULL_TRANSITIVE = "FULL_TRANSITIVE"
    NONE = "NONE"


class SerializerDef(Enum):
    AVRO = "AVRO"
    JSON = "JSON"
    PROTOBUF = "PROTOBUF"


class TopicSchemaDef(BaseModel):
    Serializer: SerializerDef
    Definition: Optional[Union[str, Dict[str, Any]]] = None
    CompatibilityMode: Optional[CompatibilityMode] = None


class BootstrapServers(BaseModel):
    __root__: str = Field(
        ..., description="Endpoint URL of the Kafka cluster in the format hostname:port"
    )


class SecurityProtocol(Enum):
    PLAINTEXT = "PLAINTEXT"
    SSL = "SSL"
    SASL_PLAINTEXT = "SASL_PLAINTEXT"
    SASL_SSL = "SASL_SSL"


class SASLMechanism(Enum):
    PLAIN = "PLAIN"
    GSSAPI = "GSSAPI"
    OAUTHBEARER = "OAUTHBEARER"
    SCRAM_SHA_256 = "SCRAM-SHA-256"
    SCRAM_SHA_512 = "SCRAM-SHA-512"


class SASLUsername(BaseModel):
    __root__: str = Field(..., description="Kafka SASL username for Authentication")


class SASLPassword(BaseModel):
    __root__: str = Field(..., description="Kafka SASL password for Authentication")


class RegistryUrl(BaseModel):
    __root__: str = Field(..., description="Schema registry URL")


class RegistryUsername(BaseModel):
    __root__: str = Field(..., description="Schema registry username")


class RegistryPassword(BaseModel):
    __root__: str = Field(..., description="Schema registry password")


class RegistryUserInfo(BaseModel):
    __root__: str = Field(
        ...,
        description="The username and password together in the form of username:password",
    )


class Name(BaseModel):
    __root__: constr(regex=r"^[a-zA-Z0-9_.-]+$", min_length=1) = Field(
        ..., description="Kafka topic name"
    )


class PartitionsCount(BaseModel):
    __root__: int = Field(
        ..., description="Number of partitions for the new Kafka topic"
    )


class ReplicationFactor(BaseModel):
    __root__: int = Field(..., description="Kafka topic replication factor")


class TopicSchemas(BaseModel):
    Key: Optional[TopicSchemaDef] = None
    Value: Optional[TopicSchemaDef] = None
    Header: Optional[TopicSchemaDef] = None


class PatternType(Enum):
    LITERAL = "LITERAL"
    PREFIXED = "PREFIXED"
    MATCH = "MATCH"


class ResourceType(Enum):
    CLUSTER = "CLUSTER"
    DELEGATION_TOKEN = "DELEGATION_TOKEN"
    GROUP = "GROUP"
    TOPIC = "TOPIC"
    TRANSACTIONAL_ID = "TRANSACTIONAL_ID"


class Action(Enum):
    ALL = "ALL"
    READ = "READ"
    WRITE = "WRITE"
    CREATE = "CREATE"
    DELETE = "DELETE"
    ALTER = "ALTER"
    DESCRIBE = "DESCRIBE"
    CLUSTER_ACTION = "CLUSTER_ACTION"
    DESCRIBE_CONFIGS = "DESCRIBE_CONFIGS"
    ALTER_CONFIGS = "ALTER_CONFIGS"
    IDEMPOTENT_WRITE = "IDEMPOTENT_WRITE"


class Effect(Enum):
    DENY = "DENY"
    ALLOW = "ALLOW"


class PolicyDef(BaseModel):
    class Config:
        extra = Extra.forbid

    Resource: str = Field(..., description="Name of the resource to apply the ACL for")
    PatternType: Optional[PatternType] = Field(
        "LITERAL", description="Pattern type for resource value"
    )
    Principal: str = Field(..., description="Kafka user to apply the ACLs for.")
    ResourceType: ResourceType = Field(
        ..., description="Kafka user to apply the ACLs for."
    )
    Action: Action = Field(..., description="Access action allowed.")
    Effect: Effect = Field(..., description="Effect for the ACL.")
    Host: Optional[str] = Field(
        "*", description="Specify the host for the ACL. Defaults to '*'"
    )


class EwsKafkaSchema(BaseModel):
    RegistryUrl: Optional[RegistryUrl] = None
    RegistryUsername: Optional[RegistryUsername] = None
    RegistryPassword: Optional[RegistryPassword] = None
    RegistryUserInfo: Optional[RegistryUserInfo] = None
    Subject: Optional[str] = None
    Serializer: Optional[SerializerDef] = None
    Definition: Optional[Union[str, Dict[str, Any]]] = None
    CompatibilityMode: Optional[CompatibilityMode] = None
    ServiceToken: Optional[str] = Field(None, description="The Lambda Function ARN")
    PermanentlyDelete: Optional[bool] = Field(
        False,
        description="If set to true, the Schema is set to hard delete. Use carefully",
    )


class EwsKafkaAcl(BaseModel):
    Policies: Optional[List[PolicyDef]] = None


class Schemas(BaseModel):
    FunctionName: Optional[str] = Field(
        None, description="Name or ARN of the Schema Registry function to use"
    )
    RegistryUrl: Optional[str] = None
    RegistryUsername: Optional[RegistryUsername] = None
    RegistryPassword: Optional[RegistryPassword] = None
    RegistryUserInfo: Optional[RegistryUserInfo] = None
    CompatibilityMode: Optional[CompatibilityMode] = None


class EwsKafkaParameters(BaseModel):
    BootstrapServers: Optional[BootstrapServers] = None
    SecurityProtocol: Optional[SecurityProtocol] = None
    SASLMechanism: Optional[SASLMechanism] = None
    SASLUsername: Optional[SASLUsername] = None
    SASLPassword: Optional[SASLPassword] = None
    RegistryUrl: Optional[RegistryUrl] = None
    RegistryUsername: Optional[RegistryUsername] = None
    RegistryPassword: Optional[RegistryPassword] = None
    CompatibilityMode: Optional[CompatibilityMode] = None


class EwsKafkaTopic(BaseModel):
    Name: Name
    PartitionsCount: PartitionsCount
    ReplicationFactor: Optional[ReplicationFactor] = None
    BootstrapServers: Optional[BootstrapServers] = None
    SecurityProtocol: Optional[SecurityProtocol] = None
    SASLMechanism: Optional[SASLMechanism] = None
    SASLUsername: Optional[SASLUsername] = None
    SASLPassword: Optional[SASLPassword] = None
    Schema: Optional[TopicSchemas] = None


class Policies(BaseModel):
    __root__: List[PolicyDef]


class SchemasDef(BaseModel):
    __root__: EwsKafkaSchema


class AclsModel(BaseModel):
    __root__: EwsKafkaAcl


class Topics(BaseModel):
    Topics: Optional[List[EwsKafkaTopic]] = None
    ReplicationFactor: Optional[ReplicationFactor] = None
    FunctionName: Optional[str] = Field(
        None,
        description="Name or ARN of the Lambda function to use for Custom::KafkaTopic",
    )
    DeletionPolicy: Optional[DeletionPolicy] = "Retain"
    ImportExisting: Optional[bool] = Field(
        True,
        description="Whether to import existing topics on Create. Fails if set to false",
    )


class ACLs(BaseModel):
    Policies: Optional[Policies] = None
    FunctionName: Optional[str] = Field(
        None,
        description="Name or ARN of the Lambda function to use for Custom::KafkaACL",
    )


class Model(BaseModel):
    Globals: EwsKafkaParameters
    Topics: Optional[Topics] = None
    ACLs: Optional[ACLs] = None
    Schemas: Optional[Schemas] = None
